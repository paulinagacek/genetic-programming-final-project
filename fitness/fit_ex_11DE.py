def fitness(received_outs, expected_outs):
    fitness = 0
    if len(received_outs) == 0:
        fitness += -10e+9
        return fitness
    try:
        fitness += -abs(received_outs[0] -expected_outs[0])
    except ValueError:
        fitness += -10e+9

    return fitness