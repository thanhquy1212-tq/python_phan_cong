import itertools


def get_subsets(input_set, max_size):
    # Khởi tạo một tập hợp rỗng để chứa các tập hợp con
    result_set = set()

    # Tạo ra tất cả các tổ hợp con có độ dài từ 0 đến max_size
    for r in range(0, max_size + 1):
        for subset in itertools.combinations(input_set, r):
            result_set.add(frozenset(subset))  # Sử dụng frozenset để có thể thêm vào tập hợp

    return result_set

input_set = {1, 2, 3}
max_size = 2

subsets = get_subsets(input_set, max_size)
for subset in subsets:
    print(subset)
