class HashTable:
    def __init__(self, length=1024):
        self.length = length
        self.hash_table = [None]*self.length
        self.idx = 0


    def add(self, key, value=None):
        hsh = self.hash(key)

        if not self.hash_table[hsh]:
            self.hash_table[hsh] = []

        self.hash_table[hsh].append([key, value])

    def get(self, key):
        """ returns value from table at the hashed-key-index"""
        hashed_key = self.hash(key)
        key_index = self.hash_table[hashed_key]

        if key_index:
            for i in range(len(key_index)):
                if key == key_index[i][0]:
                    return key_index[i][1]
        return None

    def contains(self, key):
        """Returns boolean if key is already in HashTable"""
        hashed_key = self.hash(key)
        key_index = self.hash_table[hashed_key]
        
        if key_index:
            if key == key_index[0][0]:
                return True
        return False
            
    def hash(self, key):
        """
        Returns hash-index
        """
        sum_chars = 0
        key = str(key)
        for char in key: 
            sum_chars += ord(str(char))
        square_sum = sum_chars**2
        divide_square = square_sum // ord(key[0])
        return (divide_square % self.length)

    def get_length(self):
        return self.length

    ### we need these to make the iterable process #####
    def __iter__(self): 
            return self
  
    def __next__(self):  
        if self.idx > self.length-1:
            # self.idx = 0
            raise StopIteration 
        else: 
            self.idx += 1
            return self.hash_table[self.idx-1]
























