print("Nguyễn Hồng Pháp")
print("MSSV:235752020710006")
print("#####################")
class ReverseWords:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        words = self.input_string.split()
        reversed_words = " ".join(reversed(words))   
        return reversed_words
input_string = "Hello, py"
reverse_words = ReverseWords(input_string)
reversed_result = reverse_words.reverse()
print("Chuỗi ban đầu:", input_string)
print("Chuỗi đảo ngược từng từ:", reversed_result)

