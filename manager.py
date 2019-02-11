# from sys import argv
import item

# script, file_name = argv

class Manager(object):

    print("Welcome to your to-do manager!")

    def read(self):
        target = open('todos.txt', 'r')
        print(target.read())
        target.close()

    def add_to_list(self):

        target = open('todos.txt', 'a')
        add_item = target.write(input('What do you want do add? '))
#        print(target.write(item))
        target.close()

    def exit(self):

        input = ("> ")

        if input == 'quit':
            exit(0)

        else:
            print("I don't know what you want to do")



    #def complete_items():

add_item = Manager()
add_item.read()
add_item.add_to_list()
#target.close()
#text = Manager()
#text.read()
#text.close()
