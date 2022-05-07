from Virtual_Disk import VirtualDisk
from Directory import Directory


class File_Entry:
    def __init__(self):
        self.dir_obj = Directory
        self.virtualObj = VirtualDisk()

    def write_file(self, user_data, cluster_number):
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

    def read_file(self, file_name):
        isFileEXist = self.dir_obj.search_directory(self, file_name)  # return first_cluster

        if isFileEXist != -1:
            f_cluster = isFileEXist
            dir_table = self.dir_obj.print_Dir(self)
            content = dir_table[f_cluster][4]
            return str(content)

        else:
            return "The file doesn't exist"
