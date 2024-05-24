from itertools import combinations

class SubsetGenerator:
    def get_unique_subsets(self, nums):
        subsets = []
        for r in range(len(nums) + 1):
            subsets.extend(list(combinations(nums, r)))
        return [list(subset) for subset in subsets]

generator = SubsetGenerator()
nums = [4, 5, 6]
print(generator.get_unique_subsets(nums))
