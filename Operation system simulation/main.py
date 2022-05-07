from CMD import main
import subprocess
import os

obj = main()

run = True
while run == True:
    command = list(map(str, input("> ").split()))

    if command[0] == "dir":
        obj.dir()

    elif command[0] == "import":
        obj.Import(command[1])

    elif command[0] == "type":
        obj.type(command[1])

    elif command[0] == "export":
        source = command[1]
        destination = command[2]
        obj.export(source, destination)

    elif command[0] == "rename":
        old_name = command[1]
        new_name = command[2]
        obj.rename(old_name, new_name)

    elif command[0] == "del":
        obj.Del(command[1])

    elif command[0] == "copy":
        obj.copy(command[1], command[2])

    elif command[0] == "cls":
        obj.cls()

    elif command[0] == "md":
        obj.md(command[1])

    elif command[0] == "rd":
        obj.rd(command[1])

    elif command[0] == "cd":
        obj.cd(command[1])

    elif command[0] == "help":
        obj.help(command[1], command)


    elif command[0] == "exit":
        run = False
        break
