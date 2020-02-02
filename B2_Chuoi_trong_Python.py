# Date: 22 Jan 20 (day2)
# Source: HowKteam

# dấu nháy đơn '' và dấu nháy kép " " cùng thể hiện string
# nếu trong chuối có dấu nháy "" thì sử dụng ''
# nếu trong chuỗi có dấu nháy '' thì sử dụng "
# 

'''
dấu 3 nháy đơn thể hiện chuỗi có nhiều dòng
tương tự """""" cũng có chức năng giống như vậy
nó có chức năng tạo cmt nhiều dòng
'''
user_str = '''Line1
Line2
Line3'''
print(user_str)

#Escape sequence
# \a -> alert -> kêu 1 tiếng beep
# \t -> tương ứng với nhấn Tab
# \b -> backspace -> lui về khoảng trắng gần nhất
# \' -> print dấu nháy đơn '
# \" -> print dấu nháy kép "
# \\ -> print dấu \

print('\\')

# chuỗi trần -> "bỏ qua" các escape sequence
# thêm r vào trước chuỗi
print(r"abc\n cde")

# Python hỗ trợ toán tử nhân chuỗi
# str = str*n -> lặp lại n lần chuỗi str
user_str2 = 'abc'
user_str2 = user_str2*3
print(user_str2)

# kiểm tra strB có tồn tại trong strA hay không
strA = 'Dung Tran'
strB = 'Dung Tran Tan'
check = strA in strB
print(check)

# cắt chuỗi -> strB = strA[start:end:step]
# start: vị trí bắt đầu cắt, end: vị trí cuối -1, step: bước
strB = strA[1:5]
print(strB)

# ép kiểu -> giống C
# %s,%d -> giống C -> chức năng là để lấy thành phần tương ứng trong class (vd class có 2 tp _str_ & _repr_, %)
# cú pháp
		
a = 'trong đây có 2 biến truyền vào %s %d' %('string',2)
print(a)

# f-string -> đại diện cho biến str truyền vào
# cú pháp f'{<biến đại diện>}'
x = 'Tan Dung'
y = f'{x} Tran'
print(y)

# print theo format
# cú pháp: str = 'abc {x1} xyz {x2}'.format(x1=<giá trị x1>, x2=<giá trị x2>)
# hoặc: str = 'abc {} xyz {}'.format(<giá trị 1>,<giá trị 2>) -> lưu ý phải tương ứng
f = 'Đây là chuỗi được định dạng\n1: {one},2: {two}'.format(one=1,two=2)
print(f)

# căn lề trái:
left = 'Đây là {:>50} bên trái'.format('khúc giữa')
print(left)
# căn lề giữa
center = 'Đây là {:*>50} bên trái'.format('khúc giữa')
print(center)