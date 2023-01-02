def fitness(received_outs, expected_outs):
    fitness = 0
    if len(received_outs) != 2:
        fitness += -(10e+9 * abs(len(received_outs) - 2))
        return int(fitness)
    try:
        fitness += -abs(received_outs[0] - received_outs[1] - expected_outs[0])
    except Exception:
        fitness += -10e+9

    return int(fitness)