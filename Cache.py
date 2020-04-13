from datetime import datetime

class LRUitem(object):
    def __init__(self, key, item) :
        self.key = key
        self.item = item
        self.timestamp = datetime.now()

class LRU(object) :
    def __init__(self, length, delta=None):
        self.length = length
        self.delta = delta
        self.hash = {}
        self.item_list = []

    def put(self, item) :
        # pass
        if item.key in self.hash:
            item_index = self.item_list.index(item)
            self.item_list[:] = self.item_list[:item_index] + self.item_list[item_index + 1:]
            self.item_list.insert(0, item)
        else :
            if len(self.item_list) > self.length:
                self.delete(self.item_list[-1])
            self.hash[item.key] = item
            self.item_list.insert(0, item)


    def delete(self, item):
        # pass
        del self.hash[item.key]
        del self.item_list[self.item_list.index(item)]

    def check(self) :
        # pass
        def old_items():
            recent = datetime.now()
            for item in self.item_list:
                time = recent - item.timestamp
                if time.seconds > self.delta:
                    yield item
        map(lambda x: self.delete(x), old_items())

    def get(self, item) :
        # pass
        if item.key in self.hash:
            item_index = self.item_list.index(item)
            yield self.item_list[item_index]


# def main():
#     LRU

# if __name__ == "__main__":
#     main()