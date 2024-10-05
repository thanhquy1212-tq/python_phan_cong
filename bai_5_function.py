# 2 tham số truyền vào
def calculate_discounted_price(gia_goc, phan_tram_chiet_khau):
# tiền chiêt khấu
 tien_chiet_khau = (phan_tram_chiet_khau /100) * gia_goc
# giá sau khi trừ tiền chiết khấu
 discounted_price = gia_goc - tien_chiet_khau
# trả về giá sau khi chiết khấu
 return discounted_price

gia_goc = int(input("Nhập giá gốc: "))
phan_tram_chiet_khau =int(input("Nhập phần trăm chiết khấu: "))

discounted_price = calculate_discounted_price(gia_goc, phan_tram_chiet_khau)

print(f"Giá đã chiết khấu là: {discounted_price}")