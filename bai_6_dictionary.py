def merge_dicts(dict1, dict2):
    # Hợp nhất hai từ điển bằng phương thức update()
    dict1.update(dict2)
    return dict1

dict1 = {'tên': 'quý', 'tuổi': 22}
dict2 = {'tinh': 'quảng nam', 'nghề nghiệp': 'sinh viên'}

merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)
