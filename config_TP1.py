# Configuration file.

import arenas

# general -- first three parameters can be overwritten with command-line arguments (cf. "python tetracomposibot.py --help")

display_mode = 0
arena = 1
position = False 
max_iterations = 2500 #401*500

# affichage

display_welcome_message = False
verbose_minimal_progress = True # display iterations
display_robot_stats = True
display_team_stats = False
display_tournament_results = False
display_time_stats = True

# initialization : create and place robots at initial positions (returns a list containing the robots)

import robot_braitenberg_avoider
import robot_braitenberg_loveWall
import robot_braitenberg_hateWall
import robot_braitenberg_loveBot
import robot_braitenberg_hateBot
import robot_subsomption
import robot_dumb

def initialize_robots(arena_size=-1, particle_box=-1): # particle_box: size of the robot enclosed in a square
    x_center = arena_size // 2 - particle_box / 2
    y_center = arena_size // 2 - particle_box / 2
    robots = []
    #robots.append(robot_braitenberg_avoider.Robot_player(90, y_center, 0, name="My Robot", team="A"))
    #robots.append(robot_braitenberg_loveWall.Robot_player(4, y_center, 0, name="My Robot", team="A"))
    #robots.append(robot_braitenberg_hateWall.Robot_player(4, y_center, 0, name="HateWall", team="A"))
    #robots.append(robot_braitenberg_loveBot.Robot_player(50, y_center, 0, name="LoveBot", team="A"))
    #robots.append(robot_braitenberg_hateBot.Robot_player(50, y_center, 0, name="LoveBot", team="A"))
    robots.append(robot_subsomption.Robot_player(70, y_center, 180, name="Third robot", team="Team Dumb"))
    #robots.append(robot_dumb.Robot_player(x_center, y_center, 270, name="Fourth robot", team="Team Dumb"))
    robots.append(robot_subsomption.Robot_player(50, y_center+5, 0, name="LoveBot", team="A"))
    robots.append(robot_subsomption.Robot_player(50, y_center+20, 0, name="LoveBot", team="A"))
    robots.append(robot_subsomption.Robot_player(50, y_center+30, 0, name="LoveBot", team="A"))
    robots.append(robot_subsomption.Robot_player(50, y_center+40, 0, name="LoveBot", team="A"))
    

    return robots
