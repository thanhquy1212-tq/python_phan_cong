def tim_so_lon_nhat():
    so_lon_nhat = None
    while True:
            number = float(input("Nhập một số (nhập 0 để dừng): "))
            if number == 0:
                break
            if so_lon_nhat is None or number > so_lon_nhat:
                so_lon_nhat = number
    if so_lon_nhat is not None:
        print(f"Số lớn nhất trong dãy là: {so_lon_nhat}")
    else:
        print("Không có số nào được nhập.")
tim_so_lon_nhat()