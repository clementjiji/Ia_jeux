# Projet "robotique" IA&Jeux 2025
#
# Binome:
#  Prénom Nom No_étudiant/e : _________
#  Prénom Nom No_étudiant/e : _________
#
# check robot.py for sensor naming convention
# all sensor and motor value are normalized (from 0.0 to 1.0 for sensors, -1.0 to +1.0 for motors)

from robot import * 

nb_robots = 0

class Robot_player(Robot):

    team_name = "Les_vainqueurs!!!!!"  # vous pouvez modifier le nom de votre équipe
    robot_id = -1             # ne pas modifier. Permet de connaitre le numéro de votre robot.
    memory = 0                # vous n'avez le droit qu'a une case mémoire qui doit être obligatoirement un entier

    def __init__(self, x_0, y_0, theta_0, name="n/a", team="n/a"):
        global nb_robots
        self.robot_id = nb_robots
        nb_robots+=1
        super().__init__(x_0, y_0, theta_0, name="Robot "+str(self.robot_id), team=self.team_name)

    def step(self, sensors, sensor_view=None, sensor_robot=None, sensor_team=None):

        prio_max = 10
        prio_current = 0
        
        sensor_to_wall = []
        sensor_to_robot = []
        for i in range (0,8):
            if  sensor_view[i] == 1:
                sensor_to_wall.append( sensors[i] )
                sensor_to_robot.append(1.0)
            elif  sensor_view[i] == 2:
                sensor_to_wall.append( 1.0 )
                sensor_to_robot.append( sensors[i] )
            else:
                sensor_to_wall.append(1.0)
                sensor_to_robot.append(1.0)

        

        if(sensors[sensor_front]<0.3 or sensors[sensor_front_left]+sensors[sensor_front_right]<0.3): 
            prio_current = 100
            if prio_current > prio_max:
                prio_max = prio_current
                translation = sensor_to_wall[sensor_front]
                rotation = ((sensor_to_wall[sensor_front_left]) - (sensor_to_wall[sensor_front_right])) + (sensor_to_wall[sensor_front] - 1) * 0.5
        
        if(sensor_to_robot[sensor_front]<0.3 or sensor_to_robot[sensor_front_left]+sensor_to_robot[sensor_front_left] < 0.3):
            prio_current = 70
            if prio_current > prio_max:
                

        




        translation = sensors[sensor_front]
        rotation = 1.0 * sensors[sensor_front_left] - 1.0 * sensors[sensor_front_right] + (random.random()-0.5)*0.1
        return translation, rotation, False

