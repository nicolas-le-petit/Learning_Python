# interable aobject là 1 kiểu đối tượng chứa các phần tử mà các phần tử có liên kết với nhau, vd List, Array...
# có thể tham chiếu bằng index
# interation object là kiểu đối tượng chứa các phần tử mà không thể truy cập trực tiếp bằng index mà phải truy cập lần lượt -> giống linked list
# define tupple
# tup = [x for x in range(4)]
# print(tup)
# # difine interator
# intor = (x for x in range(4))
# print(next(intor))


def findPeakElement(nums):
    l,r = 0,len(nums)
        
    if len(nums)==1:
 		print("The list has just 01 element!",mid)
        return 0
        
    while l<r:
        mid = (l+r)//2
        print('mid=',mid)

        if mid>=(len(nums)-1) or mid<0:
            if nums[len(nums)-1] > nums[0]:
            	print('nums[len(nums)-1] > nums[0]')
                return len(nums)-1
            else:
            	print('nums[len(nums)-1] < nums[0]')
                return 0
            
        if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
        	print('find the target!')
            return mid
        elif nums[mid]>nums[mid-1]:
        	print('move to right')
            l=mid+1
        else:
        	print('move to left')
            r=mid

    if (l!=len(nums) and nums[l]>nums[l-1] and nums[l]>nums[l+1]):
    	print('post-process left')
        return l
    return -1

print(findPeakElement([1,2,3]))
print(findPeakElement([2,1,2]))