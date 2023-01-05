import numpy as np


def fitness(received_outs, expected_outs, nodes=0):
    fitness_ = 0
    if len(received_outs) == 0:
        fitness_ -= 1000
        fitness_ -= nodes * 5
        return max(fitness_, -1000000)

    expe = expected_outs[0]
    got = received_outs[0]
    diff = int(np.log(((got**2 - expe**2)**2+(got-expe)**2) + 1)*100)
    if diff == 0:
        return fitness_
    fitness_ -= diff
    fitness_ -= nodes*5

    return max(fitness_, -1000000)