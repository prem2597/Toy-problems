from datetime import datetime

class LRU(object) :
    def __init__(self):
        super().__init__()
        self.timestamp = datetime.now()
        self.size = 5
        self.hash = {}
        self.item_list = []

    def put(self, key, value) :
        # pass
        if key in self.hash :
            print("Yes")
            item_index = self.item_list.index(key)
            print(item_index)
            self.item_list[:] = self.item_list[:item_index] + self.item_list[item_index + 1:]
            print(self.item_list)
            self.item_list.insert(0, key)
            print(self.item_list)
        else :
            if len(self.item_list) > self.size :
                print("True")
                self.delete(self.item_list[-1])
            self.hash[key] = value
            self.item_list.insert(0, key)

    def delete(self, key) :
        # self.hash.pop(key, None)
        del self.hash[key]
        del self.item_list[self.item_list.index(key)]

    def get(self, key) :
        if key in self.hash:
            yield self.hash[key]

    def frequency(self)-> int :
        return len(self.hash)

    def get_cache(self) :
        for key, item in self.hash.items() :
            if None:
                pass
            else :
                print (f"index: {key} " + f"key: {item} ")

