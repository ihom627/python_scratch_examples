#!/usr/bin/env python

#import pdb

grid = [[0 for x in range(3)] for x in range(3)] 


def print_grid(n):
    for i in range(0, n + 1):
        for j in range(0, n +1):
            print "grid[%d][%d] = %d" % (i, j, grid[i][j])


def robot_paths(x, y, n):

#    pdb.set_trace()

    #print "at grid[%d][%d] = %d" % (x, y, grid[x][y])
    print "at grid[%d][%d]" % (x, y)

    #reached end
    if x == n and y == n:
        print "\treached end"
        return 1

    #check top
    if y >= n + 1:  
        print "\ttop"
        return 0

    #check bot 
    elif y <= -1:
        print "\tbot"
        return 0

    #check left
    elif x <= -1:
        print "\tleft"
        return 0

    #check right
    elif x >= n + 1:
        print "\tright"
        return 0

    #return robot_paths(x + 1, y, n) + robot_paths(x, y + 1, n) + robot_paths(x + -1, y, n) + robot_paths(x, y - 1, n)

    return robot_paths(x + 1, y, n) + robot_paths(x, y + 1, n)



print_grid(2)
count = robot_paths(0, 0, 2)
print count






