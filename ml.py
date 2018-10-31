import random
import numpy

def dummy_model(n, size, theta, seed=None):
    # save the state of the rng
    randstate = random.getstate()
    if seed != None:
        random.seed(seed)
    # fill res with random numbers
    res = numpy.zeros((size, n))
    for i in range(size):
        for j in range(n):
            res[i][j] = random.uniform(0.0, theta)
    # restore state of rng
    random.setstate(randstate)
    return res

def thimming(data, size):
    # fill res with rows from data
    # each row is uniquely selected randomly
    res = numpy.zeros((size, data.shape[1]))
    selected_rows = []
    for i in range(size):
        selected_row = random.randint(0, size-1)
        while selected_row in selected_rows:
            selected_row = random.randint(0, size-1)
        selected_rows.append(selected_row)
        res[i] = data[selected_row]
    return res



# data = dummy_model(4, 16, 2, 1)
# print(data)
# thimmed_data = thimming(data, int(data.shape[0]/2))
# print(thimmed_data)

