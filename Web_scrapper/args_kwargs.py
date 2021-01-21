# def my_data(request,*args,**kwargs):
#     print(request)
#     print(args,kwargs)
    

# my_data("kyaw","soe",1,3,4,name="Krishna")


# def get_data(**kwargs):
    
#     chance = 5
#     count= 1
#     while count <= chance:
        
#         name = input("Enter name: ")
#         if name == kwargs.get("name"):
#             print("Ur name is correct")
#             break
#         else:
#             print("U guess wrong, Chance Remaining: ==> ", chance - count)
#             count += 1
            
# name = input("Enter Quiz name: ")            
# get_data(name=name)

def args_kwargs_test(d,*name_list,):
    pass
    # print(name_list,d)

args_kwargs_test("shamu","ramu","lol")

# def unpacking_string(string):
#     string = input("Enter any string :")
#     string = [*string]
#     print(string)


# unpacking_string("RealPython")  

# *a, = "Hello"
# print(a)

def unpacking_dictionary():
    context = {}
    name = input("Enter name: ")
    age = int(input("Enter Age: "))
    if age >=100:
        context.update({"error":"Name should not greater than 100"})
    else:
        context.update({"name":name,"age":age})
        context = {**context}
    print(context)
    # print(context.popitem())
    # print(context)
    # x = ("data")
    # print(context.fromkeys(x,"location"))

unpacking_dictionary()


    











