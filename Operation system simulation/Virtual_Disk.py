class VirtualDisk:

    def __init__(self):
        # Super_Block initialization
        super_Block = ["0"] * 1024
        with open('virtualDisk.txt', 'w') as f:
            for i in super_Block:
                f.write(str(i))

        # meta_data initialization
        meta_data = ["*"] * 4 * 1024
        with open('virtualDisk.txt', 'a') as f:
            for i in meta_data:
                f.write(str(i))

        # data_file initialization
        data_file = ["#"] * 1019 * 1024
        with open('virtualDisk.txt', 'a') as f:
            for i in data_file:
                f.write(str(i))

    def write_BLock(self, user_data, cluster_number):
        self.user_data = user_data
        with open("virtualDisk.txt", "r+") as file:
            filedata = file.read()
            listdata = list(filedata)
            start = 1024 * cluster_number
            end = start + len(self.user_data)
            listdata[start:end] = self.user_data
            strdata = "".join(listdata)

        with open('virtualDisk.txt', 'w') as file:
            file.write(strdata)
        file.close()

    def read_BLock(self, cluster_number):
        try:
            with open("virtualDisk.txt", "rb") as file:
                filedata = file.read()
                listdata = list(filedata)
                start = 1024 * cluster_number
                end = start + len(self.user_data)
                print(filedata[start:end])
        except:
            with open("virtualDisk.txt", "rb") as file:
                start = cluster_number * 1024
                end = start + 1024
                data = file.read()
                print(data[start:end])


obj = VirtualDisk()
obj.read_BLock(5)
