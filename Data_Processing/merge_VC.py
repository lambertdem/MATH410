import numpy as np
import pandas as pd
import math
import os
import sys

def read_file(csv_name):
    #Read a comma separated value file with header where csv_name is of the form *.csv
    df = pd.read_csv(csv_name, sep=',')
    return df

def main():

    nm = "en_climate_daily_BC_1108395_2013_P1D.csv"
    df = read_file(nm)

    for i in range(2014,2021):
        nm = "en_climate_daily_BC_1108395_" + str(i) + "_P1D.csv"
        df4 = read_file(nm)
        df = df.append(df4)
        print(i)
    df.to_csv('VC_2013_2020.csv', index=False)

    nm = "en_climate_daily_NT_2204100_1937_P1D.csv"
    df1 = read_file(nm)
    for i in range(1938,2014):
        nm = "en_climate_daily_NT_2204100_" + str(i) + "_P1D.csv"
        df4 = read_file(nm)
        df1 = df1.append(df4)
        print(i)
    df1.to_csv('VC_1937_2013.csv', index=False)
    

    df = df.append(df1)
    df.to_csv('VC_1937_2020.csv', index=False)

if __name__ == "__main__":
    main()