def fitness(received_outs, expected_outs, nodes=0):
    fitness_ = 0
    if len(received_outs) == 0:
        fitness_ -= 1000
        fitness_ -= nodes*5
        return max(fitness_, -1000000)
    fitness_ -= abs(received_outs[0] - expected_outs[0])
    fitness_ -= int((len(received_outs)-1)*20)

    return max(fitness_, -1000000)