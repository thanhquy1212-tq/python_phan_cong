# Hàm lấy ký tự tại chỉ mục nhất định
def get_char_at_index(string, index):
    return string[index]

# Nhập chuỗi và chỉ mục từ người dùng
input_string = input("Nhập chuỗi: ")
index = int(input("Nhập chỉ mục: "))

# Gọi hàm và hiển thị kết quả
result = get_char_at_index(input_string, index)
print(f"Ký tự tại chỉ mục {index} là: {result}")
