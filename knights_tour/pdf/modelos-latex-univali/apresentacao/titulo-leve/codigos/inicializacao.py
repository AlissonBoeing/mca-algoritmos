x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

size = int(input("\n Choose board size (NxN)\n"))

if (size <= 3):
    print("Size must be greater than 3")
    sys.exit()

x = int(input("\n Choose initial X position\n"))
y = int(input("\n Choose initial y position\n "))

if not ((x >= 0 and x < size) and (y >= 0 and y < size)):
    print("Inititial position must be within board limits") 
    sys.exit() 

knights_tour(size, x, y)
