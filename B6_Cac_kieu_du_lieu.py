# List trong Python là một dạng dữ liệu cho phép lưu trữ nhiều kiểu dữ liệu khác nhau trong nó
# Để khai báo một list trong Python thì chúng ta sử dụng cặp dấu [] và bên trong là các giá trị của list.
# Các phần tử trong một list được đánh dấu bắt đầu từ 0 theo chiều từ trái sang phải và từ -1 theo chiều từ phải qua trái.
# '''
# list = [a,b,c,d]
# index = 0,1,2,3
# reverse index = -4,-3,-2,-1
# '''
list1 = [1,2,"Dung"]
print(list1)

# xóa 1 ptử trong List
del list1[1]
print(list1)

# có thể lồng n List vào nhau => List cũng có thể chứa kiểu dữ liệu list
list2 = ['Teo','Ti','Chuot']
print(list2[0:2])
list3 = [list1,list2]
print(list3)
# có thể truy cập vào từng list trong list tổng hợp hoặc thậm chí đến từng phần tử của list con
print(list3[0])
print(list3[1][1])


#=====================TUPPLE=========================#
# Tuple trong Python là một kiểu dữ liệu dùng để lưu trữ các đối tượng không thay đổi về sau (giống như hằng số).
days = ('sun','mon','tue','wed','thu','fri','sat') #khai báo
#hoặc
days_1 = 'sun','mon','tue','wed','thu','fri','sat' #không cần dấu ()
# khai báo tupple trống
empty = ()
# Còn nếu như tuple của bạn chỉ chứa duy nhất một giá trị thì bắt buộc bạn phải thêm một dấu , nữa đằng sau giá trị đó.
only = ('Best',)

# Để truy cập đến các phần tử trong Tuple thì các bạn thực hiện tương tự như đối với chuỗi và list.
print(days[0:4]) #truy xuâts từ start -> end (lưu ý ptử thứ end sẽ không xuất hiện)

# tupple không cho phép thay đổi/thêm các phần tử trong tupple đã được define
# chúng ta chỉ có thể nối 2 tupple lại với nhau để "thêm" tupple