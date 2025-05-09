print("Nguyễn Hồng Pháp")
print("MSSV:235752020710006")
print("#####################")
import numpy as np
dt = np.dtype([('name', 'S20'), ('height', float), ('class', int)])
students = np.array([('Phap', 175.2, 10),
                     ('Nhat', 162.5, 11),
                     ('Luc', 180.0, 10),
                     ('Anh', 168.9, 11)], dtype=dt)
sorted_students = np.sort(students, order='height')
print("Danh sách sinh viên sau khi sắp xếp theo chiều cao:")
for student in sorted_students:
    print("Name:", student['name'].decode('utf-8'), "- Height:", student['height'], "- Class:", student['class'])
