# Part 1 A -- Make a Line
def make_line(size):
   line = ""
   for i in range(size):
      line += "#"
   return line

print(make_line(5))


# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(size):
    square = ""
    for _ in range(size):
        square += make_line(size) + "\n"
    return square
print(make_square(5))


# Part 1 C -- Make a Rectangle
def make_rectangle(width, height):
    for i in range(height):
        print('*' * width)
make_rectangle(10, 5)        

# Part 2 A -- Make a Stairs
def make_stairs(steps):
    for i in range(1, steps + 1):
        print('*' * i)

# Example usage:
make_stairs(5)




# Part 2 B -- Make Space-Line 
def make_space_line(steps):
    for i in range(1, steps + 1):
        print(' ' * (steps - i) + '*' * i)

# Example usage:
make_space_line(5)




# Part 2 C -- Make Isosceles Triangle
def make_isosceles_triangle(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

# Example usage:
make_isosceles_triangle(5)




# Part 3 -- Make a Diamond
def make_diamond(n):
    # Top half of the diamond
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    
    # Bottom half of the diamond
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

make_diamond(5)





