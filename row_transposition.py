def rearrange(block, key):
    ans = [''] * len(key)

    for i in range(len(key)):
        ans[key[i]] = block[i]
    
    return ans

def row_transposition(ciphertext, key):
    ans = ""
    columns = len(ciphertext) // len(key)
    grid = []

    for i in range(0, len(ciphertext), columns):
        grid.append(ciphertext[i:i+columns])
    
    grid = rearrange(grid, key)
    ans = ""

    for i in range(columns):
        for j in range(len(key)):
            ans += grid[j][i]

    return ans

def block_row_transposition(ciphertext, block_size, key):
    block_columns = block_size // len(key)
    grid = []
    
    for start in range(0, len(ciphertext), len(key) * block_columns):
        curr_block = [ciphertext[i:i+block_columns] for i in range(start, start + len(key) * block_columns, block_columns)]
        grid.append(rearrange(curr_block, key))
    
    ans = ""
    
    for grid_block in grid:
        for col in range(len(grid_block[0])):  
            for row in grid_block:             
                ans += row[col]
    
    return ans
