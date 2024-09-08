nums = [3,1,4,1,5,9,2]
sorted_nums = sorted(nums)
print(sorted_nums)

sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc)

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key = len)
print(sorted_words)