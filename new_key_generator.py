"""
NOT BACKWARDS COMPATABLE BUT LOTS OF SPEEDUP
"""


from itertools import product
def generate_keys(start_num, end_num, length):
    keys = product([i for i in range(start_num, end_num+1)], repeat=length)
    return keys


"""example usage"""
"""Generates all keys from (1,1,1,1,1) to (26,26,26,26,26) and tests the function works"""
"""
def sanity_check(key):
  if key == (8,16,1,2,26):
    print("Completed Sanity Check")
    return True

def main():
    keys = generate_keys(1, 26, 5)
    for key in keys:
        #decomment line below for type help.
        #print(key)
        if sanity_check(key) == True:
            return
    print("HMM, this should never execute")
    raise TypeError("Help")
    return

main()
"""




