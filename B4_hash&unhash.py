# giá trị trả về của hàm id là địa chỉ của giá trị (đối tượng) đó trong bộ nhớ.
# x = 10
add = id(1)
print(add) # mỗi lần in sẽ ra 1 kq khác nhau -> lý do là x là 1 biến, sẽ thay 

# nghiên cứu kỹ hơn về list & tupple
# nghiên cứu kỹ hơn về hash object & unhash object
'''
Với hash object, bạn không thể thay đổi nội dung của nó. 
Do đó, Python sẽ xin đủ khoảng trống để lưu trữ dữ liệu của bạn, không nhiều hơn và cũng không ít hơn. Giúp không hoang phí bộ nhớ của bạn. Thế nên, khi bạn cộng thêm một thứ gì đó, Python không biết nhét cái thứ bạn muốn cộng vào chỗ nào. Nên nó đành cuốn gói đi ra chỗ đó, tìm chỗ mới thoáng có đủ khoảng trống.
Còn với unhash object. Là một đối tượng bạn thay đổi được nội dung, vì thế, Python luôn xin dư bộ nhớ để chừa chỗ cho các giá trị tiếp theo bạn có thể thêm vào. Trong bài trước, Kteam đã đề cập đến việc Tuple chiếm ít dung lượng hơn List vì Tuple là hash object.
'''

x = 3//2
print(x)

nums = [1,2,3]
print(float('-inf'))




