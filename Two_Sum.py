'''
@brief: give an Int Array (not sorted, have negative), get the Index of 02 Elements which sum equal to a Target with 03 ways
@author: Dung Tran
@date: 09 Feb 2020 
'''
import math

#O(n^2)
def force_code(Array, Target):
	ans = []
	for i in range(len(Array)-1):
		for j in range(i+1, len(Array)):
			if Array[j] == Target-Array[i]:
				ans = [i, j]
				return ans
	return False

#O(n) = nlogn
def binary_search(Array, Target):
	#sort first
	Array.sort()
	for i in range(len(Array)-1):
		low, high = i+1, len(Array)-1
		while low<=high:
			mid = (high+low)//2
			if (Array[mid] == Target - Array[i]):
				ans = [i, mid]
				return ans
			elif (Array[mid] < Target - Array[i]):
				low = mid + 1
			else:
				high = mid - 1
	return False

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


class Test_Case(object):
	"""docstring for Test_Case"""
	def __init__(self, Array, Target):
		self.Array = Array
		self.Target = Target

test_case_1 = Test_Case([-1,2,3,5,0], 3) #return [2,4] or [1,3]
test_case_2 = Test_Case([-1,2,3,5,0], -2) #return False
test_case_3 = Test_Case([-1,-2,0,1,2], -2) #return [1,2]
test_case_4 = Test_Case([1,2,3,4,5,6], 3) #return [0,1]
test_case_5 = Test_Case([1,2,5,6,3,4], 7) #return [1,2] or [4,5] or [0,3]
all_test_case = [test_case_1, test_case_2, test_case_3, test_case_4, test_case_5]


'''
comment: 
if the 03 ways give 01 result --> Same
if the 03 ways give difference result --> Diff
''' 
def auto_test():
	header = '| Test Case |	    Array Test        | Target | Comment | force_code | binary_search | hash_table |'
	cmt_OK = ' Same'
	cmt_KO = ' Diff'
	print(header)
	print((len(header)+2)*'-')
	for i in range(len(all_test_case)):
		
		#print('test_case_', i+1, '\n', all_test_case[i].Array)
		force = force_code(all_test_case[i].Array, all_test_case[i].Target)
		binary = binary_search(all_test_case[i].Array, all_test_case[i].Target)
		hashtable = hash_table(all_test_case[i].Array, all_test_case[i].Target)

		if (force==binary==hashtable):
			# print('OK, force_code = binary_search, the result is:')
			# print(force)
			print('|',str(i+1).center(9),
				'|',str(all_test_case[i].Array).center(23),
				'|',str(all_test_case[i].Target).center(6),
				'|',cmt_OK.ljust(7),
				'|',str(force).center(10),
				'|',str(binary).center(13),
				'|',str(hashtable).center(10),'|')
		else:
			# print('Well, some things wrong!')
			# print('force_code = ',force)
			# print('binary_search = ',binary)
			print('|',str(i+1).center(9),
				'|',str(all_test_case[i].Array).center(23),
				'|',str(all_test_case[i].Target).center(6),
				'|',cmt_KO.ljust(7),
				'|',str(force).center(10),
				'|',str(binary).center(13),
				'|',str(hashtable).center(10),'|')

auto_test()
#hash_table(all_test_case[0].Array, -2)

def check():
	x=1
	while x**2>x*math.log(x,2): #check if n^2>nlogn --> n
		print(x)
		break
