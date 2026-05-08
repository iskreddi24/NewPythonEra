# name=input('Enter your name:')
# age=input('Enter your Age:')

# def myname(name,age):
#     if not isinstance(name,str):
#         return 'please enter the correct value bro'
#     age=int(age)
#     if not isinstance(age,int) and age<=0:
#         return 'Please enter the correct age bro'
#     return name+str(age)
# result=myname(name,age)
# print(result)
name = input('Enter your name: ')
age = input('Enter your Age: ')

def myname(name, age):

    if not isinstance(name, str):
        return 'Please enter the correct name bro'

            # Convert age into integer
    age = int(age)

    if not isinstance(age, int) or age <= 0:
        return 'Please enter the correct age bro'

    return name + " " + str(age)

result = myname(name, age)

print(result)