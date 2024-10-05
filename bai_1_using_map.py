list_of_strings = ["sinh", "quy", "huy","dung","duc"]
#s nhận từ list -> viet hoa và trả về danh sach ban đầu
capitalized_strings = list(map(lambda s: s.capitalize(), list_of_strings))
print(capitalized_strings)