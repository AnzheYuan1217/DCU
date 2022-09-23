class Student():

    def set_attributes(self, sid, name, modlist):
        self.sid = sid
        self.name = name
        self.modlist = modlist
        return


    def print_attributes(self):
        print('ID: {}'.format(self.sid))
        print('Name: {}'.format(self.name))
        print('Modules: {}')
        return

    def add_module(self, mod):
        self.modlist.append(mod)
        return

    def del_module(self, mod):
        self.modlist.remove(mod)
        return
