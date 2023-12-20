# Importing packages
import random
import os


class play_minesweeper():


    def __init__(self, n, mines_no):
        
        self.n = n
        self.mines_no = mines_no
        self.over = False
        # The actual values of the grid
        self.numbers = [[0 for y in range(self.n)] for x in range(self.n)] 
        # The apparent values of the grid
        self.mine_values = [[' ' for y in range(self.n)] for x in range(self.n)]
        # The positions that have been flagged
        self.flags = []
        self.vis = []

        # Set the mines
        self.set_mines()

        # Set the values
        self.set_values()

        # Display the instructions
        #self.instructions()


    def print_mine(self):
        for r in range(self.n):
            rowval = ""
            for col in range(self.n):
                if(self.mine_values[r][col]!= ' '):
                    rowval = rowval+ str(self.mine_values[r][col]) + "  " 
                else:
                    rowval = rowval + "N "
            print(rowval)

    # Printing the Minesweeper Layout
    def print_mines_layout(self):
        print()
        print("\t\t\tMINESWEEPER\n")
    
        st = "   "
        for i in range(self.n):
            st = st + "     " + str(i + 1)
        print(st)   
    
        for r in range(self.n):
            st = "     "
            if r == 0:
                for col in range(self.n):
                    st = st + "______" 
                print(st)
    
            st = "     "
            for col in range(self.n):
                st = st + "|     "
            print(st + "|")
            
            st = "  " + str(r + 1) + "  "
            for col in range(self.n):
                st = st + "|  " + str(self.mine_values[r][col]) + "  "
            print(st + "|") 
    
            st = "     "
            for col in range(self.n):
                st = st + "|_____"
            print(st + '|')
    
        print()
    
    # Function for setting up Mines
    def set_mines(self):
    
        # Track of number of mines already set up
        count = 0
        while count < self.mines_no:
    
            # Random number from all possible grid positions 
            val = random.randint(0, self.n*self.n-1)
    
            # Generating row and column from the number
            r = val // self.n
            col = val % self.n
    
            # Place the mine, if it doesn't already have one
            if self.numbers[r][col] != -1:
                count = count + 1
                self.numbers[r][col] = -1
    
    # Function for setting up the other grid values
    def set_values(self):
    
        # Loop for counting each cell value
        for r in range(self.n):
            for col in range(self.n):
    
                # Skip, if it contains a mine
                if self.numbers[r][col] == -1:
                    continue
    
                # Check up  
                if r > 0 and self.numbers[r-1][col] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                # Check down    
                if r < self.n-1  and self.numbers[r+1][col] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                # Check left
                if col > 0 and self.numbers[r][col-1] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                # Check right
                if col < self.n-1 and self.numbers[r][col+1] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                # Check top-left    
                if r > 0 and col > 0 and self.numbers[r-1][col-1] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                # Check top-right
                if r > 0 and col < self.n-1 and self.numbers[r-1][col+1] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                # Check below-left  
                if r < self.n-1 and col > 0 and self.numbers[r+1][col-1] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                # Check below-right
                if r < self.n-1 and col < self.n-1 and self.numbers[r+1][col+1] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
    
    # Recursive function to display all zero-valued neighbours  
    def neighbours(self, r, col):

        # If the cell already not visited
        if [r,col] not in self.vis:
    
            # Mark the cell visited
            self.vis.append([r,col])
    
            # If the cell is zero-valued
            if self.numbers[r][col] == 0:
    
                # Display it to the user
                self.mine_values[r][col] = self.numbers[r][col]
    
                # Recursive calls for the neighbouring cells
                if r > 0:
                    self.neighbours(r-1, col)
                if r < self.n-1:
                    self.neighbours(r+1, col)
                if col > 0:
                    self.neighbours(r, col-1)
                if col < self.n-1:
                    self.neighbours(r, col+1)    
                if r > 0 and col > 0:
                    self.neighbours(r-1, col-1)
                if r > 0 and col < self.n-1:
                    self.neighbours(r-1, col+1)
                if r < self.n-1 and col > 0:
                    self.neighbours(r+1, col-1)
                if r < self.n-1 and col < self.n-1:
                    self.neighbours(r+1, col+1)  
    
            # If the cell is not zero-valued            
            if self.numbers[r][col] != 0:
                    self.mine_values[r][col] = self.numbers[r][col]
    
    # Function for clearing the terminal
    def clear(self):
        os.system("clear")      
    
    # Function to display the instructions
    def instructions(self):
        print("Instructions:")
        print("1. Enter row and column number to select a cell, Example \"2 3\"")
        print("2. In order to flag a mine, enter F after row and column numbers, Example \"2 3 F\"")
    
    # Function to check for completion of the game
    def check_over(self):
    
        # Count of all numbered values
        count = 0
    
        # Loop for checking each cell in the grid
        for r in range(self.n):
            for col in range(self.n):
    
                # If cell not empty or flagged
                if self.mine_values[r][col] != ' ' and self.mine_values[r][col] != 'F':
                    count = count + 1
        
        # Count comparison          
        if count == self.n * self.n - self.mines_no:
            return True
        else:
            return False
    
    # Display all the mine locations                    
    def show_mines(self):
    
        for r in range(self.n):
            for col in range(self.n):
                if self.numbers[r][col] == -1:
                    self.mine_values[r][col] = 'M'

    # # The actual values of the grid
    # numbers = [[0 for y in range(self.n)] for x in range(self.n)] 
    # # The apparent values of the grid
    # mine_values = [[' ' for y in range(self.n)] for x in range(self.n)]
    # # The positions that have been flagged
    # flags = []

    # # Set the mines
    # set_mines()

    # # Set the values
    # set_values()

    # # Display the instructions
    # instructions()

    # # Variable for maintaining Game Loop
    # over = False
        
    # The GAME LOOP
    # run game 
    def make_move(self,inp):

        # Standard input
        print(inp)
        if len(inp) == 2:
            try:
                val = list(map(int, inp))
            except ValueError:
                print("Wrong input!")
                return

        elif len(inp) == 3:
            if inp[2] != 'F' and inp[2] != 'f':
                print("Wrong Input!")
                return

            try:
                val = list(map(int, inp[:2]))
            except ValueError:
                print("Wrong input!")
                return

            if val[0] > self.n or val[0] < 1 or val[1] > self.n or val[1] < 1:
                print("Wrong input!")
                return

            r = val[0] - 1
            c = val[1] - 1

            if [r, c] in self.flags:
                print("Flag already set")
                return

            if self.mine_values[r][c] != ' ':
                print("Value already known")
                return

            if len(self.flags) < self.mines_no:
                print("Flag set")
                self.flags.append([r, c])
                self.mine_values[r][c] = 'F'
                return
            else:
                print("Flags finished")
                return

        else:
            print("Wrong input!")
            return

        if val[0] > self.n or val[0] < 1 or val[1] > self.n or val[1] < 1:
            print("Wrong Input!")
            return

        r = val[0] - 1
        c = val[1] - 1

        if [r, c] in self.flags:
            self.flags.remove([r, c])

        if self.numbers[r][c] == -1:
            self.mine_values[r][c] = 'M'
            self.show_mines()
            self.print_mines_layout()
            print("Landed on a mine. GAME OVER!!!!!")
            over = True
            return

        elif self.numbers[r][c] == 0:
            self.vis = []
            self.mine_values[r][c] = '0'
            self.neighbours(r, c)

        else:
            self.mine_values[r][c] = self.numbers[r][c]

        if self.check_over():
            self.show_mines()
            self.print_mines_layout()
            print("Congratulations!!! YOU WIN")
            self.over = True
            return

        
if __name__ == "__main__":
    play_minesweeper(n=8, mines_no=8)
