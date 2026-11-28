class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        lw = len(word)
        def valid(i,j):
            return i >= 0 and i < r and j >= 0 and j < c
        
        direction = [(-1,0), (1,0), (0, -1), (0, 1)]

        def dfs(i,j, wi, visited):
            if wi >= lw:
                return True
            if board[i][j] != word[wi]:
                return False
            else:
                ans = False
                visited.add((i,j))
                wi += 1
                if wi >= lw:
                    return True
                for x, y in direction:
                    ni, nj = x+i, y+j
                    if valid(ni, nj) and (ni,nj) not in visited:
                        ans = ans or dfs(ni, nj,wi, visited)
                        if ans:
                            return True
                visited.remove((i,j))



        for i in range(r):
            for j in range(c):
                print("start")
                visited = set()
                
                if dfs(i,j,0, visited):
                    return True
                print("end")
        return False
        # return dfs(0, 0, "", 0)


        