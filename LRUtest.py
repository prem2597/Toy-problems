import unittest
from Cache import *
from time import sleep

class TestMethods(unittest.TestCase) :
    # def setUp(self):
    #     return super().setUp()
    # 
    
    def print_cache(cache) :
        # pass
        for i, item in enumerate(cache.item_list) :
            print (f"index: {i} " + f"key: {item.key} " + f"item: {item.item} " + f"time: {item.timestamp} ")

    print ("Initial cache items.")
    one = LRUitem(1, 'one')
    two = LRUitem(2, 'two')
    three = LRUitem(3, 'three')
    cache = LRU(length = 3, delta = 5)
    cache.put(one)
    cache.put(two)
    cache.put(three)
    print_cache(cache)
    print ("#" * 20)

    # print ("Insert a existing item: {0}.".format(one.key))
    # cache.put(one)
    # print_cache(cache)
    # print ("#" * 20)

    # print ("Insert another existing item: {0}.".format(two.key))
    # cache.put(two)
    # print_cache(cache)
    # print ("#" * 20)

    # print ("Validate items after a period of time")
    # sleep(6)
    # cache.check()
    # print_cache(cache)
    # print ("#" * 20)

    # def cache(self) :
    #     self.assertEqual(cache.get(one), 'one')


if __name__ == '__main__' :
    unittest.main()