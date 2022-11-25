import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# app = tk.Tk()

# lable = tk.Label(app, text='is it ok',font=30,height=5).pack(side='top',fill='x')
# app.geometry('1100x700')

df = pd.read_excel("C:/Users/Mazhar/OneDrive/Desktop/LIve_Working/Ocean Pro V_3.0.0/Excel_files/sales.xlsx")

fig , ax = plt.subplots(1,2)

# dfd = df.groupby(['Category','Region']).aggregate({'Sales':sum}).unstack(-2)

# fig= dfd.plot( kind='bar' ,subplots=True)


plt.subplot(2,1,1)
plt.bar(df['Category'],df['Sales'])
plt.xticks(rotation=90)
plt.rcParams["figure.autolayout"] = True


plt.subplot(2,1,2)
plt.bar(df['Category'],df['Quantity'])
plt.xticks(rotation=90)
plt.rcParams["figure.autolayout"] = True

# fig.add_subplot()



plt.show()
# app.mainloop()