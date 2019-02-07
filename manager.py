from sys import argv
import item

script, file_name = argv
class Manager(object):

    def read(self):

        target = open(file_name, 'r')
        print(target.read())
        target.close()

    def add_to_list(self, item):

        target = open(file_name, 'a')

        target.write()

        target.close()

text = Manager()
text.read()
#text.close()
