# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_index_hash = {}
        sum_index_hash = {}

        for index, text in enumerate(list1):
            list1_index_hash[text] = index
        
        min_index_sum = len(list1) + len(list2)
        for index, text in enumerate(list2):
            if text in list1_index_hash:
                sum_index_hash[text] = list1_index_hash[text] + index
                if sum_index_hash[text] < min_index_sum:
                    min_index_sum = sum_index_hash[text]
        
        min_index_texts = []
        for text, index_sum in sum_index_hash.items():
            if index_sum == min_index_sum:
                min_index_texts.append(text)


        return min_index_texts
