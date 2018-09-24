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

#from queue import *
import sys
is_py2 = sys.version[0] == '2'
if is_py2:
    import Queue as queue
else:
    import queue as queue
from itertools import permutations

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
    visited = [[False for x in range(dimensions[1])] for y in range(dimensions[0])]
    path = []
    optimal = []
    prev_list = [[() for x in range(dimensions[1])] for y in range(dimensions[0])]
    num_states_explored = 0
    q = queue.Queue()
    q.put(cur_pos)
    visited[cur_pos[0]][cur_pos[1]] = True
    #path.append( (cur_pos[0], cur_pos[1]) )
    num_states_explored += 1
    prev = cur_pos
    #possibly use a queue to check which nodes we have visited
    #use
    if(maze.isObjective(cur_pos[0],cur_pos[1])):
        return(path,num_states_explored)

    while not q.empty():
        
        cur_pos = q.get()
        #prev_list[cur_pos[0]][cur_pos[1]] = prev
        neighbors = maze.getNeighbors(cur_pos[0],cur_pos[1])
        path.append( (cur_pos[0], cur_pos[1],prev) )
        num_states_explored += 1
        #prev = cur_pos
    
        if maze.isObjective( cur_pos[0],cur_pos[1]):
            optimal.append((cur_pos[0],cur_pos[1]))
            prev = cur_pos
            while prev != maze.getStart():
                prev = prev_list[prev[0]][prev[1]]
                optimal.append((prev[0],prev[1]))
            # optimal = reversed(optimal)
            return optimal,num_states_explored

        for i in neighbors:
            if visited[i[0]][i[1]] == False:
                q.put(i)
                visited[i[0]][i[1]] = True
                prev_list[i[0]][i[1]] = cur_pos
        
    


    return [], 0


def dfs(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    cur_pos = maze.getStart()
    dimensions = maze.getDimensions()
    visited = [[False for x in range(dimensions[1])] for y in range(dimensions[0])]
    path = []
    optimal = []
    prev = cur_pos
    prev_list = [[() for x in range(dimensions[1])] for y in range(dimensions[0])]
    num_states_explored = 0

    stack = [cur_pos]
    while stack:
        cur_pos = stack.pop()
        neighbors = maze.getNeighbors(cur_pos[0],cur_pos[1])

        if visited[cur_pos[0]][cur_pos[1]] == False:
            visited[cur_pos[0]][cur_pos[1]] = True
            path.append( (cur_pos[0], cur_pos[1]) )
            num_states_explored += 1  
            if(maze.isObjective(cur_pos[0],cur_pos[1])):
                prev = cur_pos
                # while prev != maze.getStart():
                #     prev = prev_list[prev[0]][prev[1]]
                #     optimal.append((prev[0],prev[1]))
                return(path,num_states_explored)

            for i in neighbors:
                stack.append(i)
                prev_list[i[0]][i[1]] = cur_pos
    return [], 0


def greedy(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    # use the manhattan distance from the current position to the goal as the heuristic function 
    # will need to use a priority queue

    cur_pos = maze.getStart() # is characterized as a tuple(row,column)
    dimensions = maze.getDimensions() # returns num of row,columns
    visited = [[False for x in range(dimensions[1])] for y in range(dimensions[0])]
    #came_from = [[() for x in range(dimensions[1])] for y in range(dimensions[0])]
    path = []
    optimal = []
    num_states_explored = 0
    priority_que = queue.PriorityQueue()
    distance = heuristic(maze,cur_pos)
    priority_que.put([distance,cur_pos])
    #came_from[cur_pos[0]][cur_pos[1]] = None
    #prev = cur_pos

    if(maze.isObjective(cur_pos[0],cur_pos[1])):
        return(path,num_states_explored)

    while not priority_que.empty():
        cur_pos = priority_que.get()
        location = cur_pos[1]
        num_states_explored += 1
        neighbors = maze.getNeighbors(location[0],location[1])

        if(maze.isObjective(location[0],location[1])):
            path.append( (location[0], location[1]) )
            return(path,num_states_explored)

        if(visited[location[0]][location[1]] == False):
            visited[location[0]][location[1]] = True
            path.append( (location[0], location[1]) )
            for i in neighbors:
                distance = heuristic(maze,i)
                priority_que.put([distance,i])
            

    return [], 0

# def astar(maze):
#     # TODO: Write your code here
#     # return path, num_states_explored
#     # use the manhattan distance from the current position to the goal as the heuristic function 
#     cur_pos = maze.getStart() # is characterized as a tuple(row,column)
#     dimensions = maze.getDimensions() # returns num of row,columns
#     visited = [[False for x in range(dimensions[1])] for y in range(dimensions[0])]
#     came_from = [[() for x in range(dimensions[1])] for y in range(dimensions[0])]
#     num_states_explored = 0;
#     frontier = queue.PriorityQueue()
#     path = []
#     distance = heuristic(maze,cur_pos)
#     frontier.put([distance,cur_pos])
#     came_from[cur_pos[0]][cur_pos[1]] = None
#     cost_so_far = {}
#     cost_so_far[cur_pos] = 0
#     prev = cur_pos
#     optimal = []
    

#     while not frontier.empty():

#         cur_pos = frontier.get()
#         num_states_explored += 1
#         location = cur_pos[1]
#         #path.append( (location[0], location[1]))
#         neighbors = maze.getNeighbors(location[0],location[1])

#         if(maze.isObjective(location[0],location[1])):
#             prev = location
#             while prev != maze.getStart():
#                 prev = came_from[prev[0]][prev[1]]
#                 optimal.append((prev[0],prev[1]))

#             optimal.append( (location[0], location[1]) )
#             return(optimal,num_states_explored)

#         if(visited[location[0]][location[1]] == False):
#             visited[location[0]][location[1]] = True
#             path.append( (location[0], location[1]) )

#         for i in neighbors:
#             new_cost = cost_so_far[location] + 1
#             if i not in cost_so_far or new_cost < cost_so_far[i]:
#                 cost_so_far[i] = new_cost
#                 distance = new_cost + heuristic(maze,i)
#                 frontier.put([distance,i])
#                 came_from[i[0]][i[1]] = location

#     return [], 0
def astar(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    # use the manhattan distance from the current position to the goal as the heuristic function 
    cur_pos = maze.getStart() # is characterized as a tuple(row,column)
    dimensions = maze.getDimensions() # returns num of row,columns
    visited = [[False for x in range(dimensions[1])] for y in range(dimensions[0])]
    came_from = [[() for x in range(dimensions[1])] for y in range(dimensions[0])]
    num_states_explored = 0;
    frontier = queue.PriorityQueue()
    path = []
    distance = heuristic(maze,cur_pos)
    frontier.put([distance,cur_pos])
    #came_from[cur_pos[0]][cur_pos[1]] = None
    cost_so_far = {}
    cost_so_far[cur_pos] = 0
    prev = cur_pos
    optimal = []
    obj_deleted = [cur_pos]
    obj_list = maze.getObjectives()
    count = 0

    while not frontier.empty():
        count +=1
        cur_pos = frontier.get()
        num_states_explored += 1
        location = cur_pos[1]
        neighbors = maze.getNeighbors(location[0],location[1])

        if(maze.isObjective(location[0],location[1])):
            obj_deleted.append((location[0],location[1]))
            objIndex  = obj_list.index(location)
            del obj_list[objIndex]
            prev = location
            if not obj_list:
                print(obj_deleted)
                for i in reversed(obj_deleted):
                    print(i)
                    print("deleted")
                    while prev != i:
                        print(prev)
                        print("check")
                        prev = came_from[prev[0]][prev[1]]
                        print(prev)
                        optimal.append((prev[0],prev[1]))

                    #optimal.append( (location[0], location[1]) )
                return(optimal,num_states_explored)

        if(visited[location[0]][location[1]] == False):
            visited[location[0]][location[1]] = True

        for i in neighbors:

            # if(count == 1):
            #     new_cost = 0 + 1
            # else:
            new_cost = cost_so_far[location] + 1

            if i not in cost_so_far or new_cost < cost_so_far[i]:
                cost_so_far[i] = new_cost
                distance = new_cost + astar_heuristic(maze,i,obj_list)
                frontier.put([distance,i])
                came_from[i[0]][i[1]] = location

    return [], 0

def heuristic(maze, cur_pos):
    objectives = maze.getObjectives()
    goal = objectives[-1]
    return abs(goal[0] - cur_pos[0]) + abs(goal[1] - cur_pos[1])

def manhattan(cur_pos,goal):
    return abs(goal[0] - cur_pos[0]) + abs(goal[1] - cur_pos[1])

def astar_heuristic(maze,cur_pos,objectives):
    distance = 0
    optimal = queue.PriorityQueue()
    path_list = permutations(objectives)
    for path in list(path_list):
        for index in range(0,len(path)-2):
            if index == 0:
                distance = manhattan(cur_pos,path[index])

            distance += manhattan(path[index],path[index+1])
        optimal.put(distance)
        distance = 0
    return optimal.get()
        
