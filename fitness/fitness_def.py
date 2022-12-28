import numpy as np
def fitness(received_outs, expected_outs):
    fitness = 0
    if len(received_outs) == 0:
        fitness += -10e+9
        return fitness
    try:
        fitness += -abs((np.min(np.array(received_outs) -
                        expected_outs[0]))*100//expected_outs[0])  # int division to prevent Overflow error
    except ValueError:
        fitness += -10e+9

    return fitness