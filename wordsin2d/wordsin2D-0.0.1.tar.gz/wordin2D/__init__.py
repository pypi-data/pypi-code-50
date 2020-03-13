from nltk.corpus import words
p=[]
def check_word(grid,row,col,l):
    if row >= len(grid) or col >= len(grid[0]):
        return ""
    if l in words.words()  and len(l) > 2:
        if l not in p:
            p.append(l)
    if l[::-1] in words.words() and len(l) > 2:
        if l[::-1] not in p:
            p.append(l[::-1])
    if row+1 < len(grid) :
        check_word(grid,row+1,col,l+grid[row+1][col])
    if col+1 < len(grid[0]):
        check_word(grid,row,col+1,l+grid[row][col+1])
    if row+1 < len(grid) and col+1 < len(grid[0]):
        check_word(grid,row+1,col+1,l+grid[row+1][col+1])
    if row + 1 < len(grid) and col -1 >= 0:
        check_word(grid,row+1,col-1,l+grid[row+1][col-1])
def words_from_grid(grid):
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            check_word(grid,i,j,grid[i][j])
    return p
        
