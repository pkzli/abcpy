import unittest

class BackendTests():
    def test_map(self):
        for backend in self.backends:
            data = [1,2,3,4,5]
            pds = backend.parallelize(data)
            pds_map = backend.map(lambda x: x**2, pds)
            res = backend.collect(pds_map)
            self.assertListEqual(res, [1,4,9,16,25], 'Map not producing correct results for backend {}.'.format(type(backend)))
            self.assertEqual(len(res), len(data), 'Resulting map pds has wrong length for backend {}.'.format(type(backend)))

    def test_broadcast(self):
        for backend in self.backends:
            data = [1,2,3,4,5]
            pds = backend.parallelize(data)
            bds = backend.broadcast(100)
            pds_m = backend.map(lambda x: x+bds.value(), pds)
            res = backend.collect(pds_m)
            self.assertListEqual(res, [101,102,103,104,105], 'Broadcast not correctly working in combination with map for backend {}.'.format(type(backend)))

    # def test_reduceByKey_summation():
        # for backend in self.backends:
            # data = [(1,10), (1,11), (2, 20), (2, 21)]
            # data_pds = backend.parallelize(data)
            # result_pds = backend.reduceByKey(lambda val1, val2: val1 + val2, data_pds)
            # result = backend.collect(result_pds)
            # result_expected = [(1, 21), (2, 41)]
            # self.assertEqual(result, result_expected, 'ReduceByKey got wrong results for backend {}'.format(type(backend)))
            
    def test_flatMap_expand(self):
        for backend in self.backends:
            data = [(), (1), (2,3)]
            data_pds = backend.parallelize(data)
            result_pds = backend.flatMap(lambda x: [i for i in x], data_pds)
            result = backend.collect(result_pds)
            result_expected = [1, 2, 3]
            self.assertCountEqual(result, result_expected, 'Error in backend {}'.format(type(backend)))

    def test_flatMap_ungroup(self):
        for backend in self.backends:
            data = [(1, [10, 11]), (2, [20, 21])]
            data_pds = backend.parallelize(data)
            result_pds = backend.flatMap(lambda key, val: [(key, i) for i in val], data_pds)
            result = backend.collect(result_pds)
            result_expected = [(1,10), (1,11), (2, 20), (2, 21)]
            self.assertCountEqual(result, result_expected, 'Error in backend {}'.format(type(backend)))

    def test_groupByKey_simple(self):
        for backend in self.backends:
            data = [(1,10), (1,11), (2, 20), (2, 21)]
            data_pds = backend.parallelize(data)
            result_pds = backend.groupByKey(data_pds)
            result = backend.collect(result_pds)
            result_expected = [(1, [10, 11]), (2, [20, 21])]
            self.assertCountEqual(result, result_expected, 'Error in backend {}'.format(type(backend)))

    def test_groupByKey_oneelement(self):
        for backend in self.backends:
            data = [(1,10), (2, 20)]
            data_pds = backend.parallelize(data)
            result_pds = backend.groupByKey(data_pds)
            result = backend.collect(result_pds)
            result_expected = [(1, [10]), (2, [20])]
            self.assertCountEqual(result, result_expected, 'Error in backend {}'.format(type(backend)))
