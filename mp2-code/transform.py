
# transform.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains the transform function that converts the robot arm map
to the maze.
"""
import copy
from arm import Arm
from maze import Maze
from search import *
from geometry import *
from const import *
from util import *

def transformToMaze(arm, goals, obstacles, window, granularity):
    """This function transforms the given 2D map to the maze in MP1.
    
        Args:
            arm (Arm): arm instance
            goals (list): [(x, y, r)] of goals
            obstacles (list): [(x, y, r)] of obstacles
            window (tuple): (width, height) of the window
            granularity (int): unit of increasing/decreasing degree for angles

        Return:
            Maze: the maze instance generated based on input arguments.

    """
    dimensions = arm.getArmAngle()
    min_max = arm.getArmLimit()
    # if(len(min_max) == 1):
    #     offsets = [min_max[0][0],0]
    #     maze = Maze([0],offsets,granularity)
    #     column = 0
    #     row = (((min_max[0][1]-min_max[0][0])//granularity)+1)
    #     return maze
    
    offsets = [min_max[0][0],min_max[1][0]] #min value of alpha and beta
   
    row = (((min_max[0][1]-min_max[0][0])//granularity)+1)
    column = (((min_max[1][1]-min_max[1][0])//granularity)+1)
    input_map = [[SPACE_CHAR for i in range(column)] for j in range(row)]

    
    for i in range(0,row): # alpha
        for j in range(0,column): # beta
            alpha = i*granularity
            if(min_max[1][0]>=0):
                beta = j*granularity-min_max[1][0]
            else:
                beta = j*granularity+min_max[1][0]

            
            arm.setArmAngle((alpha,beta,0))
            armPos = arm.getArmPos()
            armEnd = arm.getEnd()
            if((doesArmTouchObstacles(armPos,obstacles)) and not(doesArmTouchGoals(armEnd,goals)) or not(isArmWithinWindow(armPos,window))):
                input_map[i][j] = WALL_CHAR
            elif(doesArmTouchGoals(armEnd,goals)):
                input_map[i][j] = OBJECTIVE_CHAR
            
    
    input_map[dimensions[0]//granularity][(dimensions[1]+min_max[1][1])//granularity] = START_CHAR

    maze = Maze(input_map,offsets,granularity)
     
    return maze

