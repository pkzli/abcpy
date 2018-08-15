from abcpy.backends.base import *

def BackendDummy(*args,**kwargs):
    from abcpy.backends.dummy import BackendDummy
    return BackendDummy(*args,**kwargs)

def BackendMPI(*args,**kwargs):
    from abcpy.backends.mpi import BackendMPI
    return BackendMPI(*args,**kwargs)

def BackendMPITestHelper(*args,**kwargs):
    from abcpy.backends.mpi import BackendMPITestHelper 
    return BackendMPITestHelper(*args,**kwargs)

def BackendSpark(*args,**kwargs):
    from  abcpy.backends.spark import BackendSpark
    return BackendSpark(*args,**kwargs)
