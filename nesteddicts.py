# dict1  = {}
# 3 levels deep nested dictionary
dicth =    {
    "espresso": 
        {
            "ingredients": 
                {
                    "water": 50,
                    "coffee": 18,
                },
            "cost": 1.5,
        },
    "latte": 
        {
            "ingredients": 
                {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
            "cost": 2.5,
        },
    "cappuccino": 
        {
            "ingredients": 
                {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
            "cost": 3.0,
        }
    }

# print(dicth["espresso"],'\n\n')
# dicth["espresso"].update({'ok':{'w':123}})
# print(dicth["espresso"])
# if dicth.__len__() == 0:
#     print('0')
# else:
#     print((dicth["cappuccino"].keys())  )
x = tuple(dicth["cappuccino"].keys())
print(type(x),x)
