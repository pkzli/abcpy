import numpy as np

# define observation for true parameters mean=170, std=15
height_obs = [160.82499176]

# define prior
from abcpy.continuousmodels import Uniform

mu = Uniform([[150], [200]], name='mu')
sigma = Uniform([[5], [25]], name='sigma')

# define the model
from abcpy.continuousmodels import Normal

height = Normal([mu, sigma], name = 'height')


# define statistics
from abcpy.statistics import Identity
statistics_calculator = Identity(degree=2, cross=False)

# define distance
from abcpy.distances import Euclidean
distance_calculator = Euclidean(statistics_calculator)

# define kernel
from abcpy.perturbationkernel import DefaultKernel
kernel = DefaultKernel([mu, sigma])

# define backend
# Note, the dummy backend does not parallelize the code!
# from abcpy.backends import BackendDummy as Backend
from abcpy.backends import BackendDummy as Backend

backend = Backend()

## PMC with synlik
# Define the likelihood function
from abcpy.approx_lhd import SynLiklihood
likfun = SynLiklihood(statistics_calculator)

from abcpy.inferences import PMC
T, n_sample, n_samples_per_param = 2, 3, 10000
sampler = PMC([height], [likfun], backend, seed=1)
print('PMC Inferring')
journal = sampler.sample([height_obs], T, n_sample, n_samples_per_param, covFactors=np.array([.1, .1]), iniPoints=None)
print('PMC done')
mu_sample = np.array(journal.get_parameters()['mu'])
sigma_sample = np.array(journal.get_parameters()['sigma'])
#import matplotlib.pyplot as plt
#plt.figure()
#plt.plot(mu_sample,sigma_sample,'.')
#plt.savefig('pmcsynik.eps',format='eps', dpi=1000)

## PMC with synlik
# Define the likelihood function
#from abcpy.approx_lhd import PenLogReg
#likfun = PenLogReg(statistics_calculator, [height], n_simulate = 100, n_folds = 10, max_iter = 100000, seed = 1)

#from abcpy.inferences import RejectionABC, PMC
#T, n_sample, n_samples_per_param = 2, 100, 100
#sampler = PMC([height], likfun, backend, seed=1)
#print('PMC Inferring')
#journal = sampler.sample([height_obs], T, n_sample, n_samples_per_param, covFactors=np.array([.1, .1]), iniPoints=None)
#print('PMC done')
#mu_sample = np.array(journal.get_parameters()['mu'])
#sigma_sample = np.array(journal.get_parameters()['sigma'])
#import matplotlib.pyplot as plt
#plt.figure()
#plt.plot(mu_sample,sigma_sample,'.')
#plt.savefig('pmcpenlogred.eps',format='eps', dpi=1000)
