class Solution:
    def lakeCount(self, field: List[str]) -> int:
        """
        :type field: List[str]
        :rtype: int
        """
        def searchField(y,x,field):
            raw = len(field)
            col = len(field[0])
            self.flag[y][x] = 0
            for i_ in range(y-1,y+2):
                for j_ in range(x-1,x+2):
                    if 0<=i_<raw and 0<=j_<col:
                        if self.flag[i_][j_]:
                            searchField(i_,j_,field)
                        
        count = 0
        raw = len(field)
        col = len(field[0])
        self.flag = [[0 for i in range(col)] for j in range(raw)]
        for i in range(raw):
            for j in range(col):
                if field[i][j] == 'W':
                    self.flag[i][j] = 1
        for i in range(raw):
            for j in range(col):
                if self.flag[i][j]:
                    searchField(i,j,field)
                    count+=1
        return count