from abc import ABCMeta, abstractmethod

class Backend(metaclass = ABCMeta):
    """
    This is the base class for every parallelization backend. It essentially
    resembles the map/reduce API from Spark.

    An idea for the future is to implement a MPI version of the backend with the
    hope to be more complient with standard HPC infrastructure and a potential
    speed-up.

    """

    @abstractmethod
    def parallelize(self, list):
        """
        This method distributes the list on the available workers and returns a
        reference object.

        The list should be split into number of workers many parts. Each
        part should then be sent to a separate worker node.

        Parameters
        ----------
        list: Python list
            the list that should get distributed on the worker nodes
        Returns
        -------
        PDS class (parallel data set)
            A reference object that represents the parallelized list
        """
        
        raise NotImplementedError


    @abstractmethod
    def broadcast(self, object):
        """
        Send object to all worker nodes without splitting it up.

        Parameters
        ----------
        object: Python object
            An abitrary object that should be available on all workers

        Returns
        -------
        BDS class (broadcast data set)
            A reference to the broadcasted object
        """
        
        raise NotImplementedError


    @abstractmethod
    def map(self, func, pds):
        """
        A distributed implementation of map that works on parallel data sets (PDS).

        On every element of pds the function func is called.

        Parameters
        ----------
        func: Python func
            A function that can be applied to every element of the pds
        pds: PDS class
            A parallel data set to which func should be applied
        
        Returns
        -------
        PDS class
            a new parallel data set that contains the result of the map
        """
        
        raise NotImplementedError

    @abstractmethod
    def flatMap(self, func, pds):
        """
        Same as map, but flatMap can return for every input element zero, one, or mulitple output elements.

        Since flatMap can return multiple output elements, the passed function should return a list.

        Parameters
        ----------
        func: Python func
            A function that can be applied to every element of the pds, the result has to be of type list.
        pds: PDS class
            A parallel data set to which func should be applied
        
        Returns
        -------
        PDS class
            a new parallel data set that contains the result of the flatMap
        """

        raise NotImplementedError

    @abstractmethod
    def groupByKey(self, pds):
        """
        Groups a PDS of key/value pairs according to its key.

        The resulting PDS contains the key/list of value pairs from the source PDS.

        Parameters
        ----------
        pds: PDS class
            A parallel data set of type [(k,v),..]

        Returns
        -------
        PDS class
            A new parallel data set that contains the result of groupByKey in the form [(k,[v,..],..)]
        """
    
        raise NotImplementedError

    @abstractmethod
    def collect(self, pds):
        """
        Gather the pds from all the workers, send it to the master and return it as a standard Python list.

        Parameters
        ----------
        pds: PDS class
            a parallel data set
            
        Returns
        -------
        Python list
            all elements of pds as a list
        """
        
        raise NotImplementedError

    
class PDS:
    """
    The reference class for parallel data sets (PDS).
    """

    @abstractmethod
    def __init__(self):
        raise NotImplementedError


class BDS:
    """
    The reference class for broadcast data set (BDS).
    """
    
    @abstractmethod
    def __init__(self):
        raise NotImplementedError


    @abstractmethod
    def value(self):
        """
        This method should return the actual object that the broadcast data set represents. 
        """
        raise NotImplementedError



