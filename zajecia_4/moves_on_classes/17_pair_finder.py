class PairFinder:
    def find_pair_indices(self, numbers, target):
        num_to_index = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

finder = PairFinder()
numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50
print(finder.find_pair_indices(numbers, target))
