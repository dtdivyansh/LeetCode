#https://leetcode.com/problems/divisor-game/

# DIVISOR GAME DP

def game2(n,alice):
            mem = [[0 for j in range(2)] for i in range(n+1)]
            for i in range(n+1):
                for j in range(2):
                    if(i==1):
                        if(j):
                            mem[i][j] = 1-j
                        else:
                            mem[i][j] = j
                    elif(i==2):
                        if(j):
                            mem[i][j] = j
                        else:
                            mem[i][j] = 1-j
                    else:
                        win = 1 if(j) else 0
                        for x in range(1,i//2):
                            if(i%x==0 and mem[i-x][1-j]==win):
                                mem[i][j] = win
                                break
                        else:
                            mem[i][j] = 1-win
            if(mem[n][1]):
                return True
            else:
                return False
