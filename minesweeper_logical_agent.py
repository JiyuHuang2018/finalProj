from itertools import combinations
from minesweeper import play_minesweeper
import sat_interface
import random

#class minesweeper_logical_agent():
class minesweeper_logical_agent():
    def __init__(self, n, mines_no):
        self.moves = []
        self.n = n
        self.mines_no = mines_no
        clauses = []
        self.game = play_minesweeper(n, mines_no)
        self.game.make_move("88")
        self.game.print_mines_layout()
        while not self.game.over:
            
            self.add_knowledge()
            print(self.moves)
            if(self.moves):
                print("self move")
                while self.moves:
                    item = self.moves.pop()
                    self.ai_move(item)
                    self.game.print_mines_layout()
            else:
                print("random move")
                self.random_move()
                self.game.print_mines_layout()
        #neighbor = self.get_unopen_and_mines(0,0)


    def random_move(self):
        unopen = self.get_all_unopen()
        move = random.choice(unopen)
        print(move)
        self.game.make_move("%s%s" % (move[0]+1,move[1]+1))
        
    def ai_move(self,move):
        move_arr = move.split(' ')
        print(move_arr)
        if move_arr[0] == 'F':
            game_value = self.game.mine_values[int(move_arr[1])][int(move_arr[2])]
            print(game_value)
            if(game_value== ' '):
                self.game.make_move("%s%sF" % (str(int(move_arr[1])+1),str(int(move_arr[2])+1)))
                #print("move as %s%sF" % (move_arr[1],move_arr[2]))
        else:
            game_value = self.game.mine_values[int(move_arr[0])][int(move_arr[1])]
            print(game_value)
            if(game_value== ' '):
                self.game.make_move("%s%s" % (str(int(move_arr[0])+1), str(int(move_arr[1])+1)))
                #print("move as %s%s" % ((move_arr[0]),(move_arr[1]))
    
        
    def get_combination_knowledge(self,unopen_list):
        combos = list(combinations(unopen_list, len(unopen_list)))
        formatted_combinations = ['_'.join([f'~{x}{y}' for x, y in combo]) for combo in combos]
        print (formatted_combinations)
        return formatted_combinations
    
    def add_knowledge(self):
        # add knowledge about the block that adjacents next to unkown.
        for r in range(self.n):
            for col in range(self.n):
                if((not self.unopened(r,col)) and self.game.mine_values[r][col] != '0' and self.game.mine_values[r][col] != 'F'):
                    unopen, mines = self.get_unopen_and_mines(r,col)
                    if(unopen):
##                        if(int(self.game.mine_values[r][col]) - len(mines) != 0):
                        knowledge = self.get_combination_knowledge(unopen)
                        print(knowledge)
                                    
##                            for x in knowledge:
##                                if x.count('~') == int(self.game.mine_values[r][col]):
##                                    print(x.count('~'))
##                                    for val in unopen:
##                                        s = "F %s %s" % (val[0], val[1])
##                                        if s not in self.moves:
##                                            self.moves.append("F %s %s" % (val[0], val[1]))
##                        else:
##                            for m in unopen:
##                                s = "%s %s" % (m[0], m[1])
##                                if s not in self.moves:
##                                    self.moves.append("%s %s" % (m[0], m[1]))
                    

        
    def get_neighbors(self, row, col):
        neighbors = []
        rows = self.n
        cols = self.n
    
        # Define relative directions for neighbors
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (-1, -1), (-1, 1), (1, -1)]
    
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
        
            # Check if the new coordinates are within the grid boundaries
            if 0 <= new_row < rows and 0 <= new_col < cols:
                neighbors.append((new_row, new_col))
        return neighbors

    def unopened(self ,r,col):
        if(self.game.mine_values[r][col] == ' '):
            return True;
        else:
            return False;

    def get_all_unopen(self):
        unopen = []
        for r in range(self.n):
            for c in range(self.n):
                if self.game.mine_values[r][c] == ' ':
                    unopen.append((r,c))
        return unopen
        
    def get_unopen_and_mines(self,r,col):
        unopen_neighbor = []
        mines = []
        all_neighbor = self.get_neighbors(r,col)

        for neighbor in all_neighbor:
            row, col = neighbor
            if self.unopened(row, col):
                unopen_neighbor.append(neighbor)
            elif( self.game.mine_values[r][col] == 'F'):
                mines.append(neighbor)
    
        return unopen_neighbor, mines

               
        
##        #only 8 mines possible
##        variables = [(i, j) for i in range(n) for j in range(n)]
##        variable_strings= [f"{i+1}+{j+1}" for i, j in variables]
##        mine_combinations_as_strings = []
##        for combination in itertools.combinations(variable_strings, mines_no):
##            # Concatenate the selected strings within the combination
##            combination_string = " ".join(combination)
##    
##            print(combination_string)
##            mine_combinations_as_strings.append(combination_string)
        

# Call the play_minesweeper function with automated input
if __name__ == "__main__":
    minesweeper_logical_agent(8,8)
