import inspect

# This function recursively flattens objects so that fields are at the top level
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