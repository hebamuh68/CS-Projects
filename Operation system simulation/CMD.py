import os
import subprocess

from Directory import Directory
from Virtual_Disk import VirtualDisk
from File_Entry import File_Entry
from FAT import FAT


class main:
    def __init__(self):
        self.fat_obj = FAT()
        self.dir_obj = Directory
        self.virtualObj = VirtualDisk()
        self.fileObj = File_Entry()

    def dir(self, dir_table=None):

        if dir_table == None:
            dir_table = self.dir_obj.print_Dir(self)
            self.dir_table = self.dir_obj.print_Dir(self)

        file_count = 0
        file_size = 0
        dir_count = 0
        F_space = self.fat_obj.Get_free_space()

        for i in range(len(dir_table)):
            if self.dir_table[i][1] == "0x0":  # file
                print("           ", self.dir_table[i][3], self.dir_table[i][0])
                file_count += 1
                file_size += self.dir_table[i][3]

            else:
                print("<DIR>        ", self.dir_table[i][0])
                dir_count += 1

        print("             ", file_count, "File(s)      ", file_size, "bytes")
        print("             ", dir_count, "Dir(s)       ", F_space, "bytes free")
        F_space = 0

    def cd(self, dir_name):
        first_cluster = self.dir_obj.search_directory(self, dir_name)
        if first_cluster == -1:
            print("The file doesn't exist")
        else:
            dir_table = self.dir_obj.print_Dir(self)
            cur_dir_table = dir_table[first_cluster]  # ['dir1', 'x0', 0, 0, None]
            cur_dir_table[4] = []  # none
            dir_of_cur_dir = cur_dir_table[4]

            command = input(f"/heba/{dir_name}>> ")
            this_dir_table = dir_of_cur_dir
            if command == "dir":
                main.dir(self, this_dir_table)

    def Import(self, path):

        try:
            file = open(f"{path}")
            splitPath = path.split("/")

            f_name = splitPath[-1]
            f_content = file.read()
            f_size = len(f_content)

            isFileEXist = self.dir_obj.search_directory(self, f_name)
            if isFileEXist == -1:
                f_cluster = 0
                if f_size != 0: f_cluster = self.fat_obj.Get_available_CLuster()
                self.dir_obj(f_name, "0x0", f_cluster, f_size, f_content)
                self.dir_obj.write_Directory(self, f_cluster)
                self.fileObj.write_file(f_content, f_cluster)

            else:
                print("File already exist")
        except:
            print("The file you trying to import doesn't exist in the computer disk")

    def type(self, f_name):
        print(self.fileObj.read_file(f_name))

    def export(self, source, destination):

        content = self.fileObj.read_file(source)
        file_txt = open(f"{destination}"f"/{source}", "w")
        file_txt.write(content)

    def rename(self, old_name, new_name):
        cluster_old_name = self.dir_obj.search_directory(self, old_name)
        cluster_new_name = self.dir_obj.search_directory(self, new_name)
        if cluster_old_name == -1:
            print("The file doesn't exist")
        elif cluster_new_name != -1:
            print("The file doesn't exist")
        else:
            dir_table = self.dir_obj.print_Dir(self)
            dir_table[cluster_old_name][0] = new_name

    def Del(self, f_name):
        first_cluster = self.dir_obj.search_directory(self, f_name)
        if first_cluster != -1:
            dir_table = self.dir_obj.print_Dir(self)
            del dir_table[first_cluster]
        else:
            print("The file doesn't exist")

    def rd(self, dir_name):
        dir_table = self.dir_obj.print_Dir(self)
        main.Del(self, dir_name)

    def copy(self, source, destination):
        des = destination.split("/")
        desname = des[-1]

        f_source = self.dir_obj.search_directory(self, source)
        f_destination = self.dir_obj.search_directory(self, desname)
        dir_table = self.dir_obj.print_Dir(self)

        if f_source == -1:
            print("The file doesn't exist")

        elif f_destination != -1:
            yes = input("This file name already exist, do you want to overwrite? ")
            if yes == "y":
                src = dir_table[f_source]
                desnew = [desname]

                for i in src[1:]:
                    desnew.append(i)
                self.dir_obj.update_content(self, desnew[0], desnew[1], desnew[2], desnew[3], desnew[4])
        else:
            src = dir_table[f_source]
            desnew = [desname]

            for i in src[1:]:
                desnew.append(i)
            dir_table.append(desnew)

    def cls(self):
        clear = "\n" * 100
        print(clear)

    def md(self, dir_name):
        first_cluster = self.dir_obj.search_directory(self, dir_name)
        if first_cluster != -1:
            print("The file already exist")
        else:
            self.dir_obj(dir_name, "x0", 0, 0, None)

    def help(self, arg):
        commands = {"cd": "allows for change of the current working directory of a shell instance.",
                    "cls": "clear the screen or console window of commands and any output generated by them.",
                    "dir": "Displays directory of files and directories stored on disk",
                    "exit": "To close or exit the Windows command line window, also referred to as command or cmd mode or DOS mode",
                    "rd": "remove an empty directory on various operating systems.", "md": "creating a new directory",
                    "rename": "changes the name of the first filename you enter to the second filename you enter.",
                    "type": "displays the contents of a text file",
                    "import": "Inserts data from an external file with a supported file format into a table, hierarchy, view or nickname.",
                    "export": "marks an environment variable to be exported with any newly forked child processes",
                    "copy": "it copies the text or image you have selected and stores is on your virtual clipboard, until it is overwritten by the next cut or copy command.",
                    "del": "Deletes (erases) files from disk. ",
                    }

        if arg == "help":
            print(arg)
            for i in commands:
                print(i, ":", commands[i])

        if arg not in commands.keys():
            print(f"{arg}: Command not found")

        else:
            print(arg, ":", commands[arg])
