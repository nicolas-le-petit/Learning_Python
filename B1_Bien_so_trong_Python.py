# Date: 21 Jan 20 (day1)
# Source: HowKteam

# ================BIEN TRONG PYTHON==================
# Các lưu ý:
# bien khong bat dau bang so
# khong co ki tu dac biet
# bien bao gom chu, so, _
# bien khong the trung voi cac tu khoa cua Python
# phan biet chu hoa & chu thuong
# trong Python 3x -> kieu int la vo han
# so thuc trong Python co do chinh xac 15 sau dau "."

# type(<ten_bien>) -> kiem tra kieu cua bien
# các kiểu biến đặt biệt trong Python là: phân số (fraction)/số phức -> để đảm bảo phù hợp với Toán

# để đảm bảo chính xác trong tính toán, ta sử dụng thư viện decimal
# download toàn bộ thư viện decimal/trong Python, * có nghĩa là tất cả
from decimal import*
#lấy tối đa 30 chữ số thập phân
getcontext().prec = 30

print("chia khong co decimal: ",10/3) #kiểu float
print("chia co decimal: ",Decimal(10)/Decimal(3)) #kiểu decimal

# tương tự, muốn sử dụng phân số (fraction), cần import thư viện fractions
from fractions import*
frac = Fraction(8,10)
print ("phân số là: ", frac)
print ("kiểu của frac là: ", type(frac)) 

# sử dụng số ảo không cần add thư viện
# so_ao1.real -> phần thực (kiểu float)
# so_ao1.imag -> phần ảo (kiểu float)
so_ao1 = complex(2,5)
so_ao2 = complex(3,1)
print(so_ao1+so_ao2)
print(type(so_ao2.real))
print(type(so_ao2.imag))

# một số phép toán
# Chia lấy nguyên = X//Y
# Chia lấy dư = X % Y
# X mũ Y = X**Y

# Cú pháp add thư viện:
# import <tên thư viện>
# thư viện math hỗ trợ các phép toán trong Python