import unittest
from abcpy.backends import BackendDummy
from tests.backend_tests import BackendTests

class DummyBackendTests(BackendTests, unittest.TestCase):
    backends = [BackendDummy()]
