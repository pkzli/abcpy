from itertools import groupby
from abcpy.backends import Backend, PDS, BDS

class BackendDummy(Backend):
    """
    This is a dummy parallelization backend, meaning it doesn't parallelize
    anything. It is mainly implemented for testing purpose.

    """
    
    def __init__(self):
        pass

    
    def parallelize(self, python_list):
        """
        This actually does nothing: it just wraps the Python list into dummy pds (PDSDummy).

        Parameters
        ----------
        python_list: Python list
        Returns
        -------        
        PDSDummy (parallel data set)
        """
        
        return PDSDummy(python_list)

    
    def broadcast(self, object):
        """
        This actually does nothing: it just wraps the object into BDSDummy.

        Parameters
        ----------
        object: Python object
        
        Returns
        -------        
        BDSDummy class
        """
        
        return BDSDummy(object)

    
    def map(self, func, pds):
        """
        This is a wrapper for the Python internal map function.

        Parameters
        ----------
        func: Python func
            A function that can be applied to every element of the pds
        pds: PDSDummy class
            A pseudo-parallel data set to which func should be applied
        
        Returns
        -------
        PDSDummy class
            a new pseudo-parallel data set that contains the result of the map
        """
        
        result_map = map(func, pds.python_list)
        result_pds = PDSDummy(list(result_map))
        return result_pds


    def flatMap(self, func, pds):
        """
        Implement exactly the functionality of its base class.
        """
        raise NotImplementedError


    def groupByKey(self, pds):
        """
        Implement exactly the functionality of its base class.
        """

        grouped_list = groupby(pds.python_list, key=lambda x: x[0])
        result = []
        for key, val in grouped_list:
            value_list = [x[1] for x in val]
            result.append( (key, value_list))
        result_pds = PDSDummy(list(result))
        return result_pds

    
    def collect(self, pds):
        """
        Returns the Python list stored in PDSDummy

        Parameters
        ----------
        pds: PDSDummy class
            a pseudo-parallel data set
        Returns
        -------
        Python list
            all elements of pds as a list
        """
        
        return pds.python_list


    

class PDSDummy(PDS):
    """
    This is a wrapper for a Python list to fake parallelization.
    """
    
    def __init__(self, python_list):
        self.python_list = python_list

        

class BDSDummy(BDS):
    """
    This is a wrapper for a Python object to fake parallelization.
    """
    
    def __init__(self, object):
        self.object = object

        
    def value(self):
        return self.object
