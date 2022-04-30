import os


class CMD:

    def shell_commands(self):

        commands = ["cd", "clear", "dir", "exit", "cp", "rm", "info", "mkdir", "rm", "rename", "cat", "import",
                    "export"]

        run = True
        while run == True:

            userCmd = list(map(str, input(">>> ").split()))
            if userCmd[0] == "exit":
                run = False
                break

            # print user command if consist of one word
            elif len(userCmd) == 1:
                if userCmd[0] == "cd":
                    print(os.getcwd())
                elif userCmd[0] in commands:
                    os.system(userCmd[0])
                else:
                    print(userCmd[0], ": ", "Command doesn't exist!")

            else:
                # print cd commands
                if userCmd[0] == "cd":
                    os.chdir(userCmd[1])

                # print help and help_cmd commands
                elif userCmd[0] == "help" and userCmd[1] not in commands:
                    print(userCmd[1], ": ", "Command doesn't exist!")

                # print other commands
                else:
                    os.system(' '.join(userCmd))


# ------------------------------------------------------------------------------------------
run = CMD()
run.shell_commands()
