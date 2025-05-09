print("Nguyễn Hồng Pháp")
print("MSSV:235752020710006")
print("#####################")
def print_binary_numbers(input_string):
    binary_numbers = input_string.split(',')
    print("Các số nhị phân đã nhập:")
    for binary_number in binary_numbers:
        print(binary_number.strip())
input_string = input("Nhập chuỗi số nhị phân (các số được nối bởi dấu phẩy): ")
print_binary_numbers(input_string)
