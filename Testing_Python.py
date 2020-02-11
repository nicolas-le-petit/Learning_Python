# import unittest


# class TestSum(unittest.TestCase):

#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

# if __name__ == '__main__':
#     unittest.main()


# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# del dict['Name'] # remove entry with key 'Name'
# print(dict)
# dict.clear()    # remove all entries in dict
# print(dict)
# del dict       # delete entire dictionary
# print(dict)

def hash_table(Array, Target):
	#make a hashtable
	my_dict = {}
	for x in range(len(Array)):
		my_dict[x] = Array[x]

	for i in range(len(Array)):
		val = Target - Array[i]
		for key, value in my_dict.items():
			if val == value and key!= i:
				ans = [i, key]
				return ans
	
	return False
hash_table([-1,2,3,5,0], -2)