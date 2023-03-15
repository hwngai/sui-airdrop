import os
import json

def add_sui_account(wallet_address, recovery_phrase, password, json_file):
    # Kiểm tra xem tệp JSON đã tồn tại hay chưa
    file_exists = os.path.isfile(json_file)

    # Nếu tệp không tồn tại, tạo tệp mới với danh sách rỗng
    if not file_exists:
        with open(json_file, "w") as f:
            json.dump([], f)

    # Đọc dữ liệu từ tệp JSON
    with open(json_file, "r") as f:
        data = f.read()

    # Chuyển đổi chuỗi JSON sang một đối tượng Python
    sui_accounts = json.loads(data)

    # Tạo một đối tượng mới chứa thông tin tài khoản SUI mới
    new_account = {
        "wallet_address": wallet_address,
        "recovery_phrase": recovery_phrase,
        "password": password,
    }

    # Thêm tài khoản SUI mới vào danh sách các tài khoản
    sui_accounts.append(new_account)

    # Ghi danh sách các tài khoản SUI mới vào tệp JSON
    with open(json_file, "w") as f:
        json.dump(sui_accounts, f, indent=4)

    print(f"Đã thêm tài khoản SUI mới vào tệp {json_file}!")



