def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        rk,ck = king[0],king[1]
        r,c,col,row=8,8,8,8
        topr,leftc,topc,leftr = -1,-1,8,8
        left_topR,left_topC = -1,8
        left_downR,left_downC = 8,-1
        right_topR,right_topC = -1,8
        right_downR,right_downC = 8,8
        for cord in queens:
            rq,cq = cord[0],cord[1]
            diff = abs(rq-cq)
            
            if(rk==rq): # SAME ROW
                if(cq>ck):  # QUEEN IS RIGHT OF KING
                    if(cq<col):
                        r = rq
                        col = cq
                else: # QUEEN IS LEFT OF KING
                    if(cq>leftc):
                        leftc = cq
                        leftr = rq
                
            elif(ck==cq): # SAME COLUMN
                if(rq<rk):  # QUEEN IS TOP OF KING
                    if(rq>topr):
                        topr = rq
                        topc = cq
                else: # QUEEN IS DOWN OF KING
                    if(rq<row):
                        c = cq
                        row = rq
                
            elif(abs(rk-rq)==abs(ck-cq)): # DIAGNOL CASE
                if(rq>rk):
                    if(cq>ck):
                        if(right_downR>rq):
                            right_downR = rq
                            right_downC = cq
                    else:
                        if(left_downR>rq):
                            left_downR = rq
                            left_downC = cq
                else:
                    if(cq>ck):
                        if(right_topR<rq):
                            right_topR = rq
                            right_topC = cq
                    else:
                        if(left_topR<rq):
                            left_topR = rq
                            left_topC = cq
                            
        res = [[r,col],[row,c],[topr,topc],[left_topR,left_topC],
               [left_downR,left_downC],[right_topR,right_topC],[right_downR,right_downC],[leftr,leftc]
              ]
        for co in res:
            if(co[0]!=8 and co[1]!=8):
                ans.append(co)
                                    
        return ans
