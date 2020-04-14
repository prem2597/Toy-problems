import unittest
from Cache import *
from time import sleep

class TestMethods(unittest.TestCase) :
    def setUp(self):
        return super().setUp()

    def test_func_1(self):
        print ("Initial cache items for test case 1.")
        one = LRU()
        one.put(1,"Hello")
        one.put(2,"How")
        one.put(3,"are")
        one.put(4,"you")
        one.put(5,"Data")
        one.put(6,"King")
        one.put(7,"King")
        print ("#" * 20)
        assert(one.hash.get(1)) == None
        assert(one.hash.get(7)) == "King"

    def test_func_2(self):
        print ("Initial cache items for test case 2.")
        two = LRU()
        two.put(1,"Prem")
        two.put(2,"vathi")
        two.put(3,"re")
        print ("#" * 20)
        assert(two.hash.get(1)) == "Prem"
        assert(two.hash.get(7)) == None
        assert(two.frequency()) == 3

    def test_func_3(self):
        print ("Initial cache items for test case 3.")
        three = LRU()
        three.put(1,"King")
        three.put(2,"Hello")
        three.put(3,"Hi")
        three.put(4,"Queen")
        print ("#" * 20)
        assert(three.hash.get(2))=="Hello"
        assert(three.hash.get(1))=="King"
    
if __name__ == '__main__' :
    unittest.main()