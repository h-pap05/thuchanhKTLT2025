print("Nguyễn Hồng Pháp")
print("MSSV:235752020710006")
print("#####################")
def file_read_from_head(fname, nlines):
 from itertools import islice
 with open(fname) as f:
  for line in islice(f, nlines):
   print(line)
file_read_from_head('D:/a.txt',2)

