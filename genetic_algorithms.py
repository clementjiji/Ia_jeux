
from robot import * 
import math

nb_robots = 0
debug = False

class Robot_player(Robot):

    team_name = "Optimizer"
    robot_id = -1
    iteration = 0

    param = []
    bestParam = []
    it_per_evaluation = 400
    trial = 0

    son_param = []

    x_0 = 0
    y_0 = 0
    theta_0 = 0 # in [0,360]

    current_run = 0
    accumulated_score = 0

    best_score = None
    best_param = None
    best_trial = -1

    def __init__(self, x_0, y_0, theta_0, name="n/a", team="n/a",evaluations=0,it_per_evaluation=0):
        global nb_robots
        self.robot_id = nb_robots
        nb_robots+=1
        self.x_0 = x_0
        self.y_0 = y_0
        self.theta_0 = theta_0
        self.param = [random.randint(-1, 1) for i in range(8)]
        self.it_per_evaluation = it_per_evaluation


        super().__init__(x_0, y_0, theta_0, name=name, team=team)

    def reset(self):
        super().reset()

    def step(self, sensors, sensor_view=None, sensor_robot=None, sensor_team=None):

        # cet exemple montre comment générer au hasard, et évaluer, des stratégies comportementales
        # Remarques:
        # - la liste "param", définie ci-dessus, permet de stocker les paramètres de la fonction de contrôle
        # - la fonction de controle est une combinaison linéaire des senseurs, pondérés par les paramètres (c'est un "Perceptron")

        # toutes les X itérations: le robot est remis à sa position initiale de l'arène avec une orientation aléatoire
        if self.iteration % self.it_per_evaluation == 0:
                if self.iteration > 0:
                    print ("\tparameters           =",self.param)
                    print ("\ttranslations         =",self.log_sum_of_translation,"; rotations =",self.log_sum_of_rotation) # *effective* translation/rotation (ie. measured from displacement)
                    print ("\tdistance from origin =",math.sqrt((self.x-self.x_0)**2+(self.y-self.y_0)**2))
                
                    self.score_run = self.log_sum_of_translation * (1-abs(self.log_sum_of_rotation))
                    self.accumulated_score += self.score_run
                    self.current_run += 1

                    if self.current_run < 3:
                        self.theta_0 = random.randint(0,360)
                        self.iteration = self.iteration + 1
                        return 0,0,True

                    

                    if self.best_score is None or self.accumulated_score > self.best_score :
                        self.best_score = self.accumulated_score
                        self.best_param = self.param[:]
                    else:
                        self.param = self.best_param[:]

                    if(self.trial >= 500):
                        self.param = self.best_param[:]
                    else:
                        random_param = random.randint(0,7)
                        self.son_param = self.param[:]
                        while True:
                            val = random.randint(-1, 1)
                            if val != self.son_param[random_param]:
                                self.son_param[random_param] = val
                                self.param = self.son_param[:]
                                break
                        
                        self.score_run = 0
                        self.accumulated_score = 0
                        self.current_run = 0

                #print("parametre =\n",self.param)
                #print("best_parametre =\n",self.best_param)
                    
                self.iteration = self.iteration + 1
                self.trial = self.trial + 1
                return 0, 0, True
                
                

        # fonction de contrôle (qui dépend des entrées sensorielles, et des paramètres)
        translation = math.tanh ( self.param[0] + self.param[1] * sensors[sensor_front_left] + self.param[2] * sensors[sensor_front] + self.param[3] * sensors[sensor_front_right] )
        rotation = math.tanh ( self.param[4] + self.param[5] * sensors[sensor_front_left] + self.param[6] * sensors[sensor_front] + self.param[7] * sensors[sensor_front_right] )

        if debug == True:
            if self.iteration % 100 == 0:
                print ("Robot",self.robot_id," (team "+str(self.team_name)+")","at step",self.iteration,":")
                print ("\tsensors (distance, max is 1.0)  =",sensors)
                print ("\ttype (0:empty, 1:wall, 2:robot) =",sensor_view)
                print ("\trobot's name (if relevant)      =",sensor_robot)
                print ("\trobot's team (if relevant)      =",sensor_team)

        self.iteration = self.iteration + 1
        #print("Total score =",self.best_score)
        

        return translation, rotation, False