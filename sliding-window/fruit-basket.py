class Solution:
    def fruits_basket(self, fruits):
        max_length = 0
        start_tree = 0
        count = {}
        for end_tree in range(len(fruits)):
            tree_char = fruits[end_tree]
            count[tree_char] = count.get(tree_char, 0) + 1
            while len(count) > 2:
                count[fruits[start_tree]] -= 1
                if count[fruits[start_tree]] == 0:
                    del count[fruits[start_tree]]
                start_tree += 1
            max_length = max(max_length, end_tree - start_tree + 1)
        return max_length