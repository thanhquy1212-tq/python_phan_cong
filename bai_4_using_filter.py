danh_sach = ["kém", "yếu", "trung bình", "khá", "giỏi ", "xuất sắc", "thủ khoa"]
filtered_strings = list(filter(lambda s: len(s) > 5, danh_sach))
print(filtered_strings)