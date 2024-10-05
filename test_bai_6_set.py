from itertools import combinations

def get_subsets(input_set, max_len):
    subsets = set()
    for r in range(max_len + 1):
        for subset in combinations(input_set, r):
            subsets.add(frozenset(subset))  # Sử dụng frozenset để lưu vào tập hợp vì set  không thể chứa đối tượng thay đổi
    return subsets

original_set = {1, 2, 3}
max_length = 2
result = get_subsets(original_set, max_length)
print(result)
