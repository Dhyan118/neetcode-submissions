class RandomizedSet:

    def __init__(self):
        self.h = {} #{1:0, 2:1}
        self.nums = [] #[1,2]

    def insert(self, val: int) -> bool:
        if val in self.h:
            return False 
        self.h[val] = len(self.nums)   # to store val = to store index check len of nums
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.h:
            return False

        remove_idx = self.h[val] # Check which one is last val in hashmap
        last_val = self.nums[-1] # Check which one is last val in List
        self.nums[remove_idx] = last_val # Then change index of element which wannt to del to last
        self.h[last_val] = remove_idx # Then change index of element which wannt to del to last
        self.nums.pop() 
        del self.h[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()