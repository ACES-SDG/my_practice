from tkinter import *

root = Tk()    

users = ['Anne', 'Bea', 'Chris']

variables=[]

for x in users:


    var_ejecutar=f"global {x}"
    exec(var_ejecutar)

    var_ejecutar=f"{x}=DoubleVar()"
    exec(var_ejecutar)

    variables.append(f"{users[x]}")

    var_ejecutar=f"""l = Checkbutton(root, text=\"{str(users[x])}\", 
        variable={users[x]},onvalue = 1,offvalue = 0)"""
    exec(var_ejecutar)
    
    var_ejecutar="l.pack(anchor = 'w')"
    exec(var_ejecutar)


def get_val():

    for i in variables:

        var_ejecutar=f"print('baigan',{i}.get())"
        exec(var_ejecutar)
        # print(i.get())
    print(variables)
btn= Button(root, text="ACTUALIZAR", state=NORMAL, command=get_val,bg="#C2CDD1") #crear boton
btn.pack(anchor = 'w')

root.mainloop()
