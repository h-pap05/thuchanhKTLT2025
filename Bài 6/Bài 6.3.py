print("Nguyễn Hồng Pháp")
print("MSSV:235752020710006")
print("#####################")
class Nguoi:
    def getGender(self):
        pass

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
nguoi1 = Nam()
nguoi2 = Nu()

print(nguoi1.getGender())
print(nguoi2.getGender())  

