def split_string_to_words(input_string):
    #  split() để chia chuỗi thành danh sách các từ
    ds = input_string.split()
    return ds

# Ví dụ sử dụng
input_string = "sinh quy huy dung duc"
ds = split_string_to_words(input_string)
print(ds)
