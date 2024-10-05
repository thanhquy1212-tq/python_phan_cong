def find_odd_numbers(*args):
 return [so_le for so_le in args if so_le % 2 != 0]
 #for so_le in args :
    # if so_le % 2 != 0:
      # return so_le
cac_so_le = find_odd_numbers( 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Các số lẻ là: {cac_so_le}")
