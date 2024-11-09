def rearrange(row, key):
    ans = [0] * len(key)
    
    for i in range(len(key)):
        ans[key[i]] = row[i]
    
    return ans
        
def columnar_transposition(ciphertext, key):
    ans = ""
    
    for i in range(0, len(ciphertext), len(key)):
        ans += ''.join(rearrange(list(ciphertext[i:i+len(key)]), key))
    
    return ans
