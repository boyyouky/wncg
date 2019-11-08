class Directory(object):
    def __init__(self,name,password):
        self.directory = {}
        self.name = name
        self.password = password
    def add_person(self,name,number):
        self.directory.update({name:number})
    def delete_person(self,name):
        self.directory.pop(name)
    def show_directory(self):
        name = list(self.directory.keys())
        number = list(self.directory.values())
        for i in range(len(self.directory.keys())):
            print(name[i], number[i])

    def clear_directory(self):
        self.directory.clear()
print('添加三人后显示：')
directory =Directory('chen wei',123)
directory.add_person('zhang',13320922972)
directory.add_person('li',19983439335)
directory.add_person('chen',154222345542)
directory.show_directory()
print("删除一人后显示：")
directory.delete_person('chen')
directory.show_directory()
