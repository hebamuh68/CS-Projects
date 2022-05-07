import struct

fat = []


class FAT:
    def __init__(self):

        for i in range(1024):
            if i < 5:
                fat.append(-1)
            else:
                fat.append(0)

    def returnFat(self):
        return fat

    def Write_Fat_Table(self):

        # convert fat array into bytes
        fatbyte = [0] * 4096
        for i in range(len(fat)):
            try:
                fatbyte[i] = fat[i].to_bytes(4, 'big', signed=True)
            except AttributeError:
                fatbyte[i] = str.encode(fat[i])

        # write bytes to virtual disk in 1:4 clusters
        with open("virtualDisk.txt", "rb+") as vf:
            data = vf.read()
            vf.seek(1024)
            for i in fatbyte:
                vf.write(bytes(i))

    def Get_available_CLuster(self):
        for i in range(len(fat)):
            if fat[i] == 0:
                return i
                break
        return None

    def Get_Next(self, index):
        return fat[index]

    def Set_Next(self, data, index):
        fat[index] = data

    def Get_available_CLusters(self):
        available_CLusters = 0
        for i in range(len(fat)):
            if fat[i] == 0:
                available_CLusters += 1

        return available_CLusters

    def Get_free_space(self):
        free_space = FAT.Get_available_CLuster(self) * 1024
        return free_space


"""obj = FAT()
p = obj.returnFat()
print(type(p))
k = obj.Get_available_CLuster()
print(k)"""
