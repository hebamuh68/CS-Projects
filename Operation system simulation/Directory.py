import math

from Virtual_Disk import VirtualDisk
from Directory_Entry import Dir_Entry
from FAT import FAT

all_entries = []
dir_table = []


class Directory(Dir_Entry):

    def __init__(self, f_name, f_attribute, f_cluster, f_size, f_empty):
        Dir_Entry.__init__(self, f_name, f_attribute, f_cluster, f_size, f_empty)
        self.FatTable = None
        self.noOfRequiredBlocks = None
        self.start = None

        self.virtualObj = VirtualDisk()
        self.fat_obj = FAT()

        # adding each list separated from another
        dir_table.append([f_name, f_attribute, f_cluster, f_size, f_empty])

        # joining all entries lists into one list
        all_entries.extend(Dir_Entry.get_dirEntry(self))

    def print_Dir(self):
        return dir_table

    def write_Directory(self, F_cluster=None):
        self.F_cluster = F_cluster

        # to get the first available index of fat file (Start)
        self.start = self.fat_obj.Get_available_CLuster()
        self.noOfRequiredBlocks = math.ceil(len(all_entries) / 1024)
        self.availble_Blocks = self.fat_obj.Get_available_CLusters()

        # check if there's enough available blocks
        if self.noOfRequiredBlocks < self.availble_Blocks:

            # if user give u first cluster and first cluster is empty
            if self.F_cluster != None:
                indx = self.F_cluster
                str_all_entries = [str(i) for i in all_entries]

                # Write in virtual disk file
                self.virtualObj.write_BLock(str_all_entries, indx)

            else:
                indx = self.start
                str_all_entries = [str(i) for i in all_entries]

                # Write in virtual disk file
                self.virtualObj.write_BLock(str_all_entries, indx)

            for i in range(self.start, self.start + self.noOfRequiredBlocks):
                self.fat_obj.Set_Next(-1, i)
        else:
            print("There's no Empty cluster")

    def read_Directory(self, first_cluster):
        for i in range(first_cluster, 1024 + 1):
            if self.fat_obj.Get_Next(i) == -1:
                return self.virtualObj.read_BLock(first_cluster)
            else:
                break

    def search_directory(self, file_name):
        index = -1
        for i in range(len(dir_table)):
            if dir_table[i][0] == file_name:
                index = i
                break

        return index

    def update_content(self, file_name, f_attribute, f_cluster, f_size, f_empty):
        Directory(file_name, f_attribute, f_cluster, f_size, f_empty)

        update_at = Directory.search_directory(self, file_name)
        at = update_at * 32

        if update_at != -1:
            contentToUpdate = all_entries[-32:]
            all_entries[at:at + 32] = contentToUpdate
            del all_entries[-32:]

            dir_table[update_at] = dir_table[-1]
            del dir_table[-1]

            Directory.write_Directory(self, F_cluster=None)

        else:
            print("Entry not found")

    def delete_directory(self, first_cluster):
        for i in range(first_cluster, 1024 + 1):
            if self.fat_obj.Get_Next(i) == -1:  # -1 => busy
                self.fat_obj.Set_Next(0, i)
            else:
                break


dobj = Directory("file1.txt", "0x0", 6, 20, "heba")
dobj = Directory("file2.txt", "0x0", 6, 20, "Hashim")

# dobj = Directory("dir1", "x010", 6, 20, None)
# print(dobj.print_Dir())
