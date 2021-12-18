
class Table:
    def __init__(self,table) -> None:
        self.table = table
    

    @staticmethod
    def is_distinct(subtable):
        if len({x for x in subtable if x !=0}) != len([x for x in subtable if x!=0]):
            return False
        return True
        

    def subtable_valid(self,row,col):
        row_start = (row//3)*3
        row_end = (row//3)*3+3
        col_start = (col//3)*3
        col_end = (col//3)*3+3
        subtable = []
        for i in range(row_start,row_end):
            for j in range(col_start,col_end):
                subtable.append(self.table[i][j])
        return self.is_distinct(subtable)

    def row_valid(self,row):
        self.is_distinct(self.table[row])

    def col_valid(self,col):
        col = []
        for i in range(len(self.table)):
            col.append(self.table[i])
        self.is_distinct(col)

    def is_valid(self):
        for row in range(len(self.table)):
            if not self.row_valid(row):
                return False
        for j in range(len(self.table[0])):
            if not self.col_valid(j):
                return False
        
        for i in range(0,len(self.table),3):
            for j in range(0,len(self.table[0]),3):
                if not self.subtable_valid(i,j):
                    return False
        return True






def back_track_solver(table: list[list[int]]):
    def is_valid(table: list[list[int]]):
        subtable3x3=[]
        for j in range(len(table[0])):
            col = []
            for i in range(len(table)):
                if j==0:
                    if len({x for x in table[i] if x != 0}) != len([x for x in table[i] if x != 0]):
                        return False
                if i%3==2 and j%3==2:
                    if len({x for x in subtable3x3 if x != 0}) != len([x for x in subtable3x3 if x != 0]):
                        return False
                    subtable3x3 = []
                else:
                    subtable3x3.append(table[i][j])
                col.append(table[i][j])
            if len({x for x in col if x != 0}) != len([x for x in col if x != 0]):
                return False
        return True
    return is_valid(table)



table=[
    [8,0,0 ,0,1,0, 0,0,9],
    [0,5,0 ,8,0,7, 0,1,0],
    [0,0,4 ,0,9,0, 7,0,0],
 
    [0,6,0 ,7,0,1, 0,2,0],
    [5,0,8 ,0,6,0, 1,0,7],
    [0,1,0 ,5,0,2, 0,9,0],
 
    [0,0,7 ,0,4,0, 6,0,0],
    [0,8,0 ,3,0,9, 0,4,0],
    [3,0,0 ,0,5,0, 0,0,8],
]

# print(back_track_solver(table))
t = Table(table)
print(t.is_valid())