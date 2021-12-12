class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def check_row(b,a):
            for x in b:
                if x == a * 3:
                    return True 
            return False 

        def check_col(b,a):
            for i in range(3):
                if b[0][i] == a and (b[0][i] == b[1][i] == b[2][i]):
                    return True 
            return False 
        
        def check_tri(b,a):
            if b[0][0] == a and (b[0][0] == b[1][1] == b[2][2]) \
            or b[2][0] == a and (b[2][0] == b[1][1] == b[0][2]): 
                return True 
            return False 
        
       # check special case for double winners
        if (check_row(board,'O') and check_row(board,'X')) or (check_col(board,'O') and check_col(board,'X')):
           return False 
        
        ocnt,xcnt = 0,0
        for temp in board:
            for e in temp:
                if e == 'X':
                    xcnt += 1
                elif e == 'O':
                    ocnt += 1
        if ocnt > xcnt:
            return False 
        if check_row(board,'O') or check_col(board,'O') or check_tri(board,'O'):
            # there is one winner 
            if ocnt != xcnt:
                
                return False 
        elif check_row(board,'X') or check_col(board,'X') or check_tri(board,'X'):
            if xcnt - ocnt != 1:
                return False 
        else:
            if abs(ocnt - xcnt) >= 2:
                return False 
        return True 
        