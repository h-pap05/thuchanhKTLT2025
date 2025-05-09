print("Nguyễn Hồng Pháp")
print("MSSV:235752020710006")
print("#####################")
def file_read(fname):
 from itertools import islice
 with open(fname, "w") as myfile:
  myfile.write("Python Exercises\n")
  myfile.write("Java Exercises")
 txt = open(fname)
 print(txt.read())
file_read('D:/a.txt')

