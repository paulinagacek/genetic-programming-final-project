def fitness(received_outs, expected_outs):
    fitness = 0
    if len(received_outs) != 2:
        fitness += -(10e+9 * min(abs(len(received_outs) - 1),10))
        return int(fitness)
    try:
        fitness += -abs(received_outs[0] - expected_outs[0])
    except Exception:
        fitness += -10e+9

    return int(fitness)