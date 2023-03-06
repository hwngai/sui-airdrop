
import random
import string

def generate_password(length):
    # Chọn tất cả các ký tự chữ cái và số để tạo mật khẩu
    characters = string.ascii_letters + string.digits

    # Thêm các ký tự đặc biệt vào danh sách ký tự
    special_characters = "$#@"
    characters += special_characters

    # Tạo mật khẩu ngẫu nhiên bằng cách chọn ngẫu nhiên các ký tự từ danh sách ký tự
    password = ''.join(random.choice(characters) for i in range(length))

    # Đảm bảo mật khẩu đủ phức tạp bằng cách kiểm tra các điều kiện sau:
    # - Mật khẩu chứa ít nhất một chữ cái viết hoa
    # - Mật khẩu chứa ít nhất một chữ cái viết thường
    # - Mật khẩu chứa ít nhất một số
    # - Mật khẩu chứa ít nhất một ký tự đặc biệt
    while not (any(char.isupper() for char in password) and
               any(char.islower() for char in password) and
               any(char.isdigit() for char in password) and
               any(char in special_characters for char in password)):
        password = ''.join(random.choice(characters) for i in range(length))

    return password