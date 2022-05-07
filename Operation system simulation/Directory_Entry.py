class Dir_Entry:

    def __init__(self, f_name, f_attribute, f_cluster, f_size, f_empty):

        self.ff_name = list(f_name)
        self.ff_attribute = f_attribute
        self.ff_cluster = list(str(f_cluster))
        self.ff_size = list(str(f_size))
        self.ff_empty = list(str(f_empty))

        self.f_name = [0] * 11
        self.f_attribute = [0]
        self.f_empty = [0] * 12
        self.f_cluster = [0] * 4
        self.f_size = [0] * 4

        # assign user value as list items
        for i in range(len(self.ff_name)):
            self.f_name[i] = self.ff_name[i]

        for i in range(len(self.ff_cluster)):
            self.f_cluster[i] = self.ff_cluster[i]

        for i in range(len(self.ff_size)):
            self.f_size[i] = self.ff_size[i]

        for i in range(len(self.ff_empty)):
            self.f_empty[i] = self.ff_empty[i]

    def get_dirEntry(self):

        self.entry = []
        for i in self.f_name:
            self.entry.append(i)

        for i in self.f_attribute:
            self.entry.append(i)

        for i in self.f_cluster:
            self.entry.append(i)

        for i in self.f_size:
            self.entry.append(i)

        for i in self.f_empty:
            self.entry.append(i)

        return self.entry

    def print_dirFile(self):
        with open("t.txt", "w+") as f:
            for i in self.entry:
                f.write(str(i))
