import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']
        left, fleft, front, fright, right = lidar
        
        if velocity < 0.15 and front > 1.0:
            if left > right:
                return ('left', 'accelerate')
            elif right > left :
                return ('right', 'accelerate')
            else:
                return ('straight', 'accelerate')
        else:
            if left > right :
                return ('left', 'coast')
            elif right > left :
                return ('right', 'coast')
            else:
                return ('straight', 'coast')