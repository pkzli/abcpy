import random
import numpy

def dummy_model(n, theta, seed=None):
    if seed != None:
        randstate = random.getstate()
        random.seed(seed)
    # fill res with random numbers
    #res = numpy.zeros((M, n))
    #for i in range(M):
    res = numpy.zeros(n)
    for i in range(n):
        res[i] = random.uniform(0.0, theta)
    if seed != None:
        random.setstate(randstate)
    return res

def thimming(data, new_size):
    res = numpy.zeros(new_size)
    selected_numbers = []
    for i in range(new_size):
        selected_number = random.randint(0, data.size-1)
        while selected_number in selected_numbers:
            selected_number = random.randint(0, data.size-1)
        res[i] = data[selected_number]
    return res

def stat(data):
    return numpy.mean(data)

def distance(ysim, yobs):
    return abs(stat(ysim)-stat(yobs))

def a(ysim, yobs, epsilon):
    return sum([distance(ysim[i], yobs) < epsilon for i in range(len(ysim))]) / len(ysim)

# define parameters
i = 2
npmax = pow(i, 12)
k = 10
M = 10000
theta = 3
yobs = theta / 2
epsilon = 0.1


# first step
nj = int(npmax / pow(i, k))
Mj = int(M / pow(i, 0))
print("nj ", nj, ", Mj ", Mj)
ys = [dummy_model(nj, theta) for i in range(Mj)]
bk = a(ys, yobs, epsilon)
b = bk
print("a(ys) : ", a(ys, yobs, epsilon))
print("bk ", bk)
print("b ", b)
print('===================')

# remaining steps
for j in range(1, k):
    nj = int(npmax / pow(i, k-j))
    njb = int(npmax / pow(i, k-j+1))
    Mj = M#int(M / pow(i, j))
    print("nj ", nj, "njb ", njb, ", Mj ", Mj)
    ys = [dummy_model(nj, theta) for i in range(Mj)]
    ybs = [thimming(ys[i], njb) for i in range(Mj)]
    bk = a(ys, yobs, epsilon) - a(ybs, yobs, epsilon)
    print("a(ys) : ", a(ys, yobs, epsilon))
    print("a(ybs) : ", a(ybs, yobs, epsilon))
    b += bk
    print("bk ", bk)
    print("b ", b)
    print('===================')


