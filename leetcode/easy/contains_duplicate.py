def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for n in nums:
            if n not in my_set:
                my_set.add(n)
            else:
                return True
        return False