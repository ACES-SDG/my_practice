from multiprocessing import Pool
import pandas as pd
import openpyxl

wb = openpyxl.load_workbook('C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore.xlsx')

obj = wb.active

sheetNames  = wb.sheetnames
# print()

def readExcel(n):
    df = pd.read_excel('C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore.xlsx',sheet_name=n)
    print(df,'this is in function with sheetname as ', n)
    

# print('\n')
map(readExcel, sheetNames)
   