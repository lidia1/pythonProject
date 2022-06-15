# # # This is a sample Python script.
# #
# # # Press Shift+F10 to execute it or replace it with your code.
# # # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# #
# #
# # #def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
# #    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# #
# #
# # # Press the green button in the gutter to run the script.
# # #if __name__ == '__main__':
# #     #print_hi('PyCharm')
# #
# # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# #
# # a = "String"
# # b = 3.14
# #
# # c = True
# #
# # d = 10
# #
# # #########
# # s= b +d
# # d = -10000
# # f = "fjale"
# # s1= f + str(d)
# # #print(s1,type(s1))
# #
# # e =2.15
# # pow = 2**5
# # #print(pow)
# # f=str(20/7)
# # m= 'm'
# # print(f + m)
# # #print(20 /7, 20 % 7, 20 // 7, round(20/7))
# #
# # p= False
# # n= True
# # #print( p or n)
# #
# # ##############################
# #
# # lst=[1,2,3,123,"pop", False, True]
# # print(lst)
# # lst.append("Hello")
# # lst2=[123, -43 , "Help"]
# # lst.extend(lst2)
# # print(lst)
# # lst.remove("Help")
# # print(lst)
# # #####
# #
# # s = set(lst)
# # print(s)
# # s.add(4)
# # print(s)
# # ###
# # d = dict()
# # d= {"Mon":1, "Tue":2, "Wed":3,"Thur":14, "Fri":[]}
# # print(d['Mon'])
# # d["Sat"]= {1,2,3}
# # print(d)
# # d["Sat"]= -198
# # print(d)
# #
# # ########
# #
# # t = (1,2,3,51.6, "Hello", "True") #tuple
# #
# #
# # lst5=["Hello", 1, 2 ,3 , 4 ,5 , 69.4, "What", True, False]
# # #print(lst5[0])
# # #print(lst5[1])
# # #print(lst5[-2])
# # s1={10, 20, 304, "Help"}
# # t1=( 10, 20, 304, "Help")
# # print(1 in t1) #Kontroll nese e ke
# # print(-11115 in lst5, "pppp" in lst5)
# # #print(lst5[1:-1])
# # #print(lst5[-3:])
# # #print(lst5[-4:-1])
# #
# # #Metoda strip heq hapsira anash
# # #Metoda split heq hapsira ne mes
# # a= 'bcd f'
# # b= 'ecc'
# # a_pa_space=a.strip()
# # print(a.strip(),len(a.strip()))
# # print(a.split("f"))
# #
# # name_surname= "lidia Makishti "
# # lst= name_surname.split(" ")
# # name=lst[0]
# # surname=lst[1]
# # print(name)
# # print(surname)
# # #####
# #
# # #Interval numrash
# # lst=[1,2,4,6,7,8,9]
# # print("Sum of elements in the list is:",sum(lst))
# # print("Average of elements in the list:",round(sum(lst)/len(lst)))
# #
# # a=list(range(0,101,5))
# # print(a, len(a))
#
# lst = [39, 32, 0, 9, 1, 2, 5, 7, -1, -19]
# print(lst)
# lst.sort(reverse=True)  # Rregullon list qe eshte
# print(lst)
# print(sorted(lst))  # kthen list te re
#
# # a = int(input("Enter nr 1:"))
# # b = int(input("Enter nr 2:"))
# # print("Sum is: ", a + b)
#
# ##############  if statment
# # guess= int(input("Enter 1,2 or 3:"))
# #
# # if guess ==1:
# #     print("correct")
# # elif guess ==2:
# #     print("Not correct")
# # elif guess==3:
# #     print("choose 1 or 2")
# # else:
# #     print("Other than 1 ,2 or 3")
#
# pi = 2.24
# # if pi > 3:
# #     if pi < 3.2:
# #         print("pi is between 3 and 3.2")
# #     else:
# #         print("pi is greater than 3.2")
#
# # if(pi >3) and (pi < 3.2):
# #     print("pi is between 3 and 3.2")
# #     pi= pi *3
# # elif pi > 3:
# #     print("pi is greater than 3.2")
# # else:
# #     print("pi is  < 3")
# #     print("if statment finished")
# # print(pi)
#
# # condition = 3 < 2
# # print(condition, type(condition))
# # if condition == True:
# #     print("condition is true")
# # else:
# #     print("condition false")
#
# ############################
# ########## CIKLET
#
#lst = [1, 2, 3, 4, -1, -2, -3, -3, -3]
# idx = 0
# nr_of_elements_greaterthan0=0
# sum_positive_number = 0
# while idx < len(lst):
#      print(idx, len(lst), lst[idx])
#      if lst[idx] >=0:
#          sum_positive_number
#          nr_of_elements_greaterthan0 += 1
#      idx = idx + 1
# print(nr_of_elements_greaterthan0, sum_positive_number)
# print(lst)
# nr_of_elements_greaterthan0=0
# sum_positive_number = 0
# for element in range(1,len(lst),2):
# #for element in lst:
#     if lst[element] >=0:
#         nr_of_elements_greaterthan0 += 1
#         sum_positive_number += lst[element]
#     print(element, lst[element])

# lst = list(range(1,101))
# s = 0
# for idx in range(len(lst)):
#     current_element = lst[idx]
#     if (current_element % 2) == 0:
#         s += current_element

# d={1:10, 2:20, 3:30, "Mon":40}
# s = 0
# for key, val in d.items():
#     print(key,val)
#     s += val
# print(s)

# for key in d:
#     val=d[key]
#     s+= val
# print(s)

lst = [1, 2, 3, 4, -1, -2, -3, -3, -3]
# condition=[]
# for el in lst:
#     if el < 0:
#         condition.append(True)
#     else:
#         condition.append(False)
# print(lst)
# print(condition)
lst = [1, 2, 3, 4, -1, -2, -3, -3, -3] #####JANE VEPRIME NJESOJ
# for idx in range(len(lst)):
#     el = lst[idx]
#     print(idx,el)

#for idx, el in enumerate(lst):
    #print(idx, el)

# condition=[el for el in lst if el <0]
# print(sum(condition))
#

####MATRIX
mat=[[1, 2], [10, 3]]
# print(mat[0], type(mat[0]))
# print(mat[0][1], type(mat[0][1]))
# print([el[2] for el in mat]) ## E printon si liste te re
s=[]
for el in mat:
    s += el
print(s)


a= [1, 2, 3, 4, 5, 6 ,8]
b= [2, 3, 5, 6, 7, 8 ,9]
a_plus_b=[]
# for idx in range(len(a)):
#     a_plus_b.append(a(idx)+ b(idx))
#

for pair in zip(a,b):
    a_plus_b.append((sum(pair)))
print(a_plus_b)



# print(list(zip(a,b)))
# for el_a, el_b in zip(a,b):
    a_plus_b.append(el_a + el_b)
print(a_plus_b)

################# FUNKSIONI

def f(x, y):
    s = x + y
    return s
res= f(1, 10)
print(res, type(res))

def list_sum(lst):
    s=0
    for el in lst:
        s += el
    return s

result= list_sum([1, 2, 3, 4])
print(result)
