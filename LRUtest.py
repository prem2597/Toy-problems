import unittest

class TestMethods(unittest.TestCase) :
    def setUp(self):
        return super().setUp()

    one = LRUitem(1, 'one')
    two = LRUitem(2, 'two')
    three = LRUitem(3, 'three')
    cache = LruCache(length = 3, capacity = 5)

    def cache(self) :
        self.assertEqual(cache.get(one), 'one')


if __name__ == '__main__' :
    unittest.main()