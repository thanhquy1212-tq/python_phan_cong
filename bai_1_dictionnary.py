def add_key_value_to_dict(my_dict, key, value):
    # Thêm cặp khóa-giá trị vào từ điển
    my_dict[key] = value
    return my_dict


my_dict = {'tên': 'Quý', 'tuổi': 25}
key = 'tỉnh'
value = 'Quảng Nam'

updated_dict = add_key_value_to_dict(my_dict, key, value)
print(updated_dict)
