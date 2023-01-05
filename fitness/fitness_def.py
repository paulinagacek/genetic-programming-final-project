import numpy as np
def fitness(received_outs, expected_outs, nodes=0):
    fitness_ = 0
    if len(received_outs) == 0:
        fitness_ -= 1000
        fitness_ -= nodes*5
        return max(fitness_, -1000000)
    try:
        fitness_ -= abs((np.min(np.array(received_outs) -
                        expected_outs[0])))
        fitness_ -= (len(received_outs)-1)*20
    except ValueError:
        fitness_ -= 1000

    return max(fitness_, -1000000)