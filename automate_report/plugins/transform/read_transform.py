import pandas as pd
import glob
import os

def apend_all_files(filename):
    data =pd.read_csv(filename, sep=',' , encoding='ascii') 

    print(data)
    return data

if __name__ == '__main__':
    apend_all_files('C:\\Users\\kevnov\\Documents\\Digital Skola\\automate_report\\sales_product_data\\Sales_December_2019.csv')

