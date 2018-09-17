# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Michael Abir (abir2@illinois.edu) on 08/28/2018

"""
This is the main entry point for MP1. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
# Search should return the path and the number of states explored.
# The path should be a list of tuples in the form (row, col) that correspond
# to the positions of the path taken by your search algorithm.
# Number of states explored should be a number.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,greedy,astar)

from queue import *

def search(maze, searchMethod):    
    return {
        "bfs": bfs,
        "dfs": dfs,
        "greedy": greedy,
        "astar": astar,
    }.get(searchMethod)(maze)
   

def bfs(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    cur_pos = maze.getStart() # is characterized as a tuple(row,column)
    dimensions = maze.getDimensions() # returns num of row,columns
    visited[dimensions[0]][dimensions[1]] = [False]
    num_states_explored = 0;

    q = Queue()
    q.append(cur_pos)
    visited[cur_pos[0]][cur_pos[1]] = True
    num_states_explored++
    #possibly use a queue to check which nodes we have visited
    #use
    while(!q.empty()):
        
        cur_pos = q.pop()
        neighbors = maze.getNeighbors(cur_pos)

        #since it is bfs need to visit one entire layer first then move onto the next layer
        for i in neighbors:
            if visited[i[0]][i[1]] == False:
                q.append(i)
                visited[i[0]][i[1]] = True
                num_states_explored++
                if(maze.isObjective(i)):
                    return(visited,num_states_explored)
        
    


    return [], 0


def dfs(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    return [], 0


def greedy(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    return [], 0


def astar(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    return [], 0
