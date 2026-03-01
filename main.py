import random

print("helo")

for i in range(10):
    print(i)

# Import random module for generating random numbers
import random

print ("Random number between 1 and 100:", random.randint(1, 100))
for i in range(5):
    print ("Random number between 1 and 100:", random.randint(1, 100))

# configuration
rows = 5
cols = 7
min_val = 0
max_val = 99

# generate 2D list of random numbers
matrix = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# determine width for each cell based on max value
cell_width = len(str(max_val))

# helper to print a horizontal separator line

def print_separator():
    print("+" + "-" * (cell_width + 2) + "+" * cols)

# print the grid
for r_idx, row in enumerate(matrix):
    # separator before each row
    print_separator()
    # print values
    line = ""
    for val in row:
        line += f"| {str(val).rjust(cell_width)} "
    line += "|"
    print(line)
# final separator
print_separator()
