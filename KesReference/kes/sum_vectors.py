from sum_comp import *


def line():
    print("--------------------------------------------------------------------------------------------------")


def sum_test_vector(message: str, seed: str, h: int, t_range: list[int], test_number: int):
    line()
    print("Sum Test Vector: "+str(test_number))
    print("Seed String: \""+seed+"\"")
    print("Seed Bytes: ["+seed.encode().hex()+"]")
    print("h =", h)
    print("Message String: \"" + message + "\"")
    print("Message Bytes: ["+message.encode().hex()+"]")
    sum_key = key_gen_sum(seed.encode(), h)
    print("Sum Composition Verification Key:")
    print("["+verification_key_sum(sum_key).hex()+"]")
    print("Sum Composition Secret Key, t = 0:")
    print_vector(sum_key)
    line()
    for j in t_range:
        sum_key = key_update_sum(sum_key, j)
        sigma = sign_sum(sum_key, message.encode())
        print("sigma t = "+str(j)+":")
        sigma.print()
        line()
    print("Sum Composition Secret Key, t = "+str(key_time_sum(sum_key))+":")
    print_vector(sum_key)


sum_test_vector(messages[0], seeds[0], 1, [0, 1], 1)
sum_test_vector(messages[1], seeds[1], 2, [0, 1, 2, 3], 2)
sum_test_vector(messages[2], seeds[2], 3, [0, 2, 5, 7], 3)
sum_test_vector(messages[3], seeds[3], 4, [0, 5, 10, 15], 4)
sum_test_vector(messages[4], seeds[4], 5, [0, 10, 21, 31], 5)
sum_test_vector(messages[5], seeds[5], 6, [0, 21, 42, 63], 6)
sum_test_vector(messages[6], seeds[6], 7, [0, 42, 85, 127], 7)
sum_test_vector(messages[7], seeds[7], 8, [0, 85, 170, 255], 8)
sum_test_vector(messages[8], seeds[8], 9, [0, 170, 341, 511], 9)
sum_test_vector(messages[9], seeds[9], 10, [0, 341, 682, 1023], 10)

