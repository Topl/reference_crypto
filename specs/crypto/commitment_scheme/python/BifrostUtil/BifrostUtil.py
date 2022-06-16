import jcs
import json
import base58
import sys
import os
import string
import hashlib
from graph import Graph

from graph import Graph
import inspect

from Crypto.Hash import BLAKE2b

# import MerkleTree
import inspect
from dotty_dict import dotty
# import flattenObj
# toFlatObject = flattenObj.toFlatObject

def toFlatObject(inputName, fieldName, input, index, flatObj):
    # if input is an array
    if(isinstance(input, list)):
        if index is not None:
            inputName = inputName + '.' + str(index)
        for subIndex, elem in enumerate(input):
            flatObj = toFlatObject(inputName, fieldName, elem, subIndex, flatObj)
        return flatObj

    # if input is an object
    elif(isinstance(input, dict)):
        # Add index to inputName
        if index is not None:
            inputName = inputName + '.' + index
        # Add fieldName to inputName
        if (fieldName) is not None:
            inputName = inputName + '.' + fieldName
        # flatten object fields
        for objFieldName in input:
            flatObj = toFlatObject(inputName, objFieldName, input[objFieldName], None, flatObj)
        return flatObj
    
    #if input is a simple field
    if index is not None and fieldName is not None:
       flatObj[inputName + '.' + fieldName + '.' + str(index)] = input
    if index is not None and fieldName is None:
        flatObj[inputName + '.' + str(index)] = input
    else:
        flatObj[inputName + '.' + fieldName] = input

    return flatObj

# Merkle Tree
def merkle_tree(data_blocks):
    g = Graph()

    # initial hash:
    leaves = []
    for block in data_blocks:
        assert isinstance(block, bytes)
        # todo: update this so that is uses blake2b256 since we need second preimage attack resistance
        hash_func = hashlib.sha3_256()
        hash_func.update(block)
        uuid = hash_func.hexdigest()
        leaves.append(uuid)
        g.add_node(node_id=uuid)

    # populate graph
    while leaves:
        if len(leaves) == 1:
            return g  # <--- point of return.

        c1, c2 = leaves[:2]
        leaves = leaves[2:]

        hash_func = hashlib.sha3_256()
        hash_func.update(bytes(c1, 'utf-8') + bytes(c2, 'utf-8'))
        uuid = hash_func.hexdigest()
        leaves.append(uuid)
        g.add_node(node_id=uuid)
        g.add_edge(c1, uuid)
        g.add_edge(c2, uuid)


# handle case where selection is not present in object default-None or default={}???
def getSubset(obj, keys):
    # allows access to deeply nested data.
    keySelectionTuples = []
    dot = dotty(obj)
    for key in keys:
        keySelectionTuples.append((key,dot.get(key, default={})))
    objSubset = dict(keySelectionTuples)
    return objSubset

# hash function used to hash inner nodes
def hashFunction():
    pass

class BifrostUtil:

    def __init__(self):
        pass

    hashFunc = BLAKE2b.new(digest_bits=256, update_after_digest=True)
    
    @staticmethod
    def getCommitData(obj, pages):
        leaves = []
        for page in pages:
            if (page['keyLoc'] == 'internal'):
                selection = getSubset(obj, page['keys'])
                for fieldName in selection:
                    # if the the field is an array
                    if (isinstance(selection[fieldName], list)):
                        # flatten arrays
                        # todo: determine if the empty object at the end will work
                        selection[fieldName] = toFlatObject(fieldName, None, selection, None, {})
                    # if the selection is an object
                    elif (inspect.isclass(selection[fieldName])):
                        selection[fieldName] = toFlatObject(fieldName, None, selection, None, {})
                
                canonTopSelection = jcs.canonicalize(selection)
                hash = BifrostUtil.hashFunc.update(canonTopSelection)
                base58Hash = base58.b58encode(hash.digest()).decode('utf-8')
                topLvlData = base58Hash
                # todo: figure out if top level should be bytes or encoded string
                topLeaf = {
                    'root': topLvlData,
                    'inputs': {
                        topLvlData: canonTopSelection
                    }
                }
                leaves.append(topLeaf)
            elif (page['keyLoc'] == 'reference'):
                firstSplitKey = page['keys'][0].split('.')
                currentReference = obj[firstSplitKey[0]]
                subLevelKeys = []
                # strip the reference field name from the keys
                for key in page['keys']:
                    subLevelKeys.append(key.replace(firstSplitKey[0] + '.', ''))
                # if the referenceSelection is an array
                if (isinstance(currentReference, list)):
                    # get subset selection for each object in the array of objects
                    refSelection = []
                    for subObj in currentReference:
                        refSelection.append(getSubset(subObj, subLevelKeys))
                    flatRefSelection = toFlatObject(firstSplitKey[0], None, refSelection, None, {})
                # if the referenceSelection is an object
                else:
                    referenceSelection = getSubset(currentReference, subLevelKeys)
                    flatRefSelection = toFlatObject(firstSplitKey[0], None, referenceSelection, None, {})
                
                canonRefSelection = jcs.canonicalize(flatRefSelection)
                hash = BifrostUtil.hashFunc.update(canonRefSelection)
                base58Hash = base58.b58encode(hash.digest()).decode('utf-8')
                flatRefHash = base58Hash
                # todo: determine if this is 
                refLeaf = {
                    'root': flatRefHash,
                    'inputs': {
                        flatRefHash: canonRefSelection
                    }
                }
                leaves.append(refLeaf)
        # todo: determine if this needs to be flattened
        return leaves

    @staticmethod
    def createBifrostTree(leaves):
        # turning leafs into bytes
        byteLeaves = []
        for leaf in leaves:
            # todo determine if string should be turned into bytes here or in getCommitData
            byteLeaves.append(bytes(leaf, 'utf-8'))
        tree = merkle_tree(byteLeaves)
        return tree

    @staticmethod
    def processCommitDefinition(obj, pages):
        commitSummary = BifrostUtil.getCommitData(obj, pages)

        roots = []
        inputs = []

        for keyCommits in commitSummary:
            roots.append(keyCommits['root'])
            inputs.append(keyCommits['inputs'])

        commitDefinition = {
            'newTreeLeaves': roots,
            'childInputs': inputs
        }
        return commitDefinition

    # "entrypoint for creating commitment"
    @staticmethod
    def createCommitment(obj, pages):
        data = BifrostUtil.processCommitDefinition(obj, pages)
        tree = BifrostUtil.createBifrostTree(data['newTreeLeaves'])
        
        commitment = {
            'inputs': data['childInputs'],
            'securityRoot': []
        }
        return commitment
