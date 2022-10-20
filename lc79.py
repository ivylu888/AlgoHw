class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        yL = len(board) #row
        xL = len(board[0]) #col
        
        def fn(i,j,idx):
            if(idx==len(word)):
                return True
            board[i][j], temp = -1,board[i][j]
            for a,b in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                if(a>=0 and b>=0 and a<yL and b<xL and board[a][b]==word[idx] and fn(a,b,idx+1)):
                    return True
            board[i][j]= temp
            return False 
        for i in range(yL):
            for j in range(xL):
                if(board[i][j]==word[0] and fn(i,j,1)):
                        return True
        return False
