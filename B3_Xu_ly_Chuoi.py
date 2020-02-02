# viết hoa chữ cái đầu chuỗi
user_str = 'trần tấn Dũng' 
cap = user_str.capitalize() # chỉ có chữ Tran viết hoa, các chữ cái còn lại không viết hoa
print('cap: ',cap)

# viết hoa tất cả các chữ
up = user_str.upper()
print('upper: ', up)

# viết thường tất cả chuỗi
low = user_str.lower()
print('lower: ', low)

# hoán đổi chữ viết hoa thành chữ thường, chữ thường thành chữ viết hoa
swap = user_str.swapcase()
print('swapcase: ', swap)

# chuẩn hóa chuỗi, viết hoa các chữ cái đầu tiên
tit = user_str.title()
print('title: ', tit)

# căn giữa, trái, phải
cen = user_str.center(50,'-')
print(cen)
left = user_str.ljust(50,'*')
print(left)

# encode -> mã hóa
encode = user_str.encode()
print(encode)

# thay thế chuỗi
rep = user_str.replace('n','ng')
print(rep)

# loại bỏ ký tự đầu/cuối ~ trim
strip = user_str.strip()
