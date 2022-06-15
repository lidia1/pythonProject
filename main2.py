# # import random
# #
# # POSSIBLE_MOVES = ("Guri", 'Letra', 'Gershera')
# #
# # computer_choice_idx = random.randint(0,2)
# # computer_choice = POSSIBLE_MOVES[computer_choice_idx]
# #
# # user_choice_idx =int(input("Please, enter: 1 for Guri, 2 for Letra, 3 for Gershera: "))
# # user_choice = POSSIBLE_MOVES[user_choice_idx -1]
# #
# # if computer_choice == "Guri":
# #     if user_choice == "Guri":
# #         print("Barazim")
# #     elif user_choice == "Letra":
# #         print("User win")
# #     else:
# #         print("Computer wins")
# #
# # elif computer_choice == "Letra":
# #     if user_choice == "Guri":
# #         print("Computer wins")
# #     elif user_choice == "Letra":
# #         print("Computer wins")
# #     else:
# #         print("User wins")
# #
# # else:
# #     if user_choice == "Guri":
# #         print("User win")
# #     elif user_choice == "Letra":
# #         print("Computer win")
# #     else:
# #         print("Barazim")
# #
#
# # def greet_by_name(name):
# #     print("Hello,", name)
# #
# # greet_by_name("Lidia")
#
# # def sqrt(x, y, z=3):
# #     s = (x+y+z) ** 0.5
# #     return s
# #
# # res= sqrt(1,3,10)
# # print(res)
# # def add_list(l):
# #     return sum(l)
# #
# # def add(*args):
# #     result = 0
# #     for arg in args:
# #         result += arg
# #         return result
# #
# # print(add_list([1,2,10]))
# # print(add())
#
# # def print_name_and_something(**kwargs):
# #     print(f"Dict: {kwargs}")
# #     for key,value
#
# # def print_somehting3(*args,**kwargs):
# #     print(args)
# #     print(kwargs)
# #
# #
# # print_somehting3(1,2,3,5,6, False, [], age=25, boy=True)
#
# def add(*args):
#     result = 0
#     for arg in args:
#         result += args
#     return result
#
# def sub(*args):
#     result=0
#     for args in sub:
#         result -= args
#     return result
#
# def add_list(l):
#     return sum(l)
#
# def sub_list(l):
#     return sub(l)
#
# d={'add':add, 'sub':sub}
# # print(d{'add'}(1,2,3,4))
#
# inp=input("Enter numbers seperated by ' ': ")
# print(inp)
# lst = inp.split(" ")
# lst = [int(el) for el in lst]
#
# operation =input("Add or sub? ")
# print(d[operation](lst))

# with open("file.txt", "a+") as f:
#     # while True:
#     #     line = f.readline()
#     #     print(line, end='')
#     #     if not line:
#     #         break
#     lines = f.readline()
# #    print(lines, type(lines))
#     lines = [line[:-1] for line in lines]
#     print(lines)
#     f.write("Rreshti i ri ne python\n")

# with open('csv_file.csv') as f:
#      lines = f.readline()
#      lines = [line[:-1].split(", ").split(" ") for line in lines]
#      print(lines)
#      # lines = [line.split(",") for line in lines]
#      # print(lines)
#
# make_lower= lambda x: x.lower()
# print(make_lower("HAHAHAHAH"))
##################################3

class Person:
    total_nr_persons=0

    def __init__(self,n, s, a, m=False):
        self.name = n
        self.surname= s
        self.age = a
        self.married = m
        Person.total_nr_persons +=1
        self.id = Person.total_nr_persons

    def get_married(self):
        self.married = True

    def change_name(self, new_name):
        self.name = new_name


p1 = Person("Lidia", "Makishti", 25)
p2= Person("Foti", "Miho", 20)
print(p1.id, p1.total_nr_persons, p2.id, p2.total_nr_persons)


