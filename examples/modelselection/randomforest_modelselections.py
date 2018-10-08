from abcpy.modelselections import RandomForest

def infer_model():
    # define observation for true parameters mean=170, std=15
    y_obs = [175.01 ,164.10]
    #359,144.05538,156.6335,176.88495,174.02085,177.62864,200.94146,170.58087,180.62691,174.00281,163.37984,166.23795,183.9539,153.22641]

    ## Create a array of models
    from abcpy.continuousmodels import Uniform, Normal, StudentT
    model_array = [None]*2

    #Model 1: Gaussian
    mu1 = Uniform([[150], [200]], name='mu1')
    sigma1 = Uniform([[5.0], [25.0]], name='sigma1')
    model_array[0] = Normal([mu1, sigma1])
    
    #Model 2: Student t
    mu2 = Uniform([[150], [200]], name='mu2')
    sigma2 = Uniform([[1], [30.0]], name='sigma2')
    model_array[1] = StudentT([mu2, sigma2])

    # define statistics
    from abcpy.statistics import Identity
    statistics_calculator = Identity(degree = 2, cross = False)

    # define backend
    from abcpy.backends import BackendDummy as Backend
    backend = Backend()

    # Initiate the Model selection scheme
    modelselection = RandomForest(model_array, statistics_calculator, backend, seed = 1)

    # Choose the correct model
    model = modelselection.select_model(y_obs, n_samples = 100, n_samples_per_param = 2)

    # Compute the posterior probability of each of the models
    model_prob = modelselection.posterior_probability(y_obs)



if __name__ == "__main__":
    infer_model()
