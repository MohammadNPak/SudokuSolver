class Table:
    def __init__(self,table) -> None:
        self.table = table
    
    def __str__(self) -> str:
        output = ""
        horizontal_line = "-"*(2+len(self.table[1]))*2+"\n"
        for i in range(len(self.table)):
            if i%3==0:
                output+= horizontal_line
            for j in range(len(self.table[0])):
                if j%3==0:
                    output +="|"
                output +=str(self.table[i][j])+" "
            output +="|\n"
        output+= horizontal_line
        return output

    @staticmethod
    def is_distinct(subtable):
        if len({x for x in subtable if x !=0}) == len([x for x in subtable if x!=0]):
            return True
        return False
        
    def get_subtable(self,row,col):
        row_start = (row//3)*3
        row_end = (row//3)*3+3
        col_start = (col//3)*3
        col_end = (col//3)*3+3
        subtable = []
        for i in range(row_start,row_end):
            for j in range(col_start,col_end):
                subtable.append(self.table[i][j])
        return subtable

    def get_row(self,row):
        return self.table[row]

    def get_col(self,col_index):
        col = []
        for i in range(len(self.table)):
            col.append(self.table[i][col_index])
        return col

    def row_is_valid(self,row):
        return self.is_distinct(self.get_row(row))

    def col_is_valid(self,col):
        return self.is_distinct(self.get_col(col))

    def subtable_is_valid(self,row,col):
        return self.is_distinct(self.get_subtable(row,col))

    def choice_is_valid(self,row,col):
        if self.row_is_valid(row) and self.col_is_valid(col) and self.subtable_is_valid(row,col):
            return True
        return False


    def table_is_valid(self):
        for row in range(len(self.table)):
            if not self.row_is_valid(row):
                return False
        for j in range(len(self.table[0])):
            if not self.col_is_valid(j):
                return False
        
        for i in range(0,len(self.table),3):
            for j in range(0,len(self.table[0]),3):
                if not self.subtable_is_valid(i,j):
                    return False
        return True

    def posible_choices(self,row,col):
        if self.table[row][col]==0:
            not_posible_choice= {
                *{x for x in self.get_col(col) if x !=0} ,
                *{x for x in self.get_row(row) if x !=0} ,
                *{x for x in self.get_subtable(row,col) if x !=0} ,
            }
            posible_choice= set(range(1,10)).difference(not_posible_choice)
            if len(posible_choice)!=0:
                return posible_choice
        return None

    def get_candidate_position(self):
        # for i in range(len)
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                if self.table[i][j] == 0:
                    return (i,j)        
        return None


def back_track_solver(table: Table):
    pos=table.get_candidate_position() 
    if pos is None:
        print(table)
        return True
    else:
        row,col = pos
        choices = table.posible_choices(row,col)
        if choices is None:
            return False
        for choice in choices:
            table.table[row][col] = choice
            # if not table.choice_is_valid(row,col):
            #     table.table[row][col] = 0
            if  back_track_solver(table):
                return True
            
        table.table[row][col] = 0
        return False



    
if __name__ =="__main__":

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
    breakpoint()
    print(t.table_is_valid())
    print(t)
    back_track_solver(t)
    print(t)
