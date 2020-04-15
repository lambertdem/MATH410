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

    nm = "en_climate_daily_QC_7025250_1941_P1D.csv"
    df = read_file(nm)
    for i in range(1942,2014):
        nm = "en_climate_daily_QC_7025250_" + str(i) + "_P1D.csv"
        df1 = read_file(nm)
        df = df.append(df1)
        print(i)

    df.to_csv('MTL_1941_2013.csv', index=False)

    nm = "en_climate_daily_QC_7025251_2013_P1D.csv"
    df1 = read_file(nm)
    for i in range(2014,2021):
        nm = "en_climate_daily_QC_7025251_" + str(i) + "_P1D.csv"
        df2 = read_file(nm)
        df1 = df1.append(df2)
        print(i)
    df.to_csv('MTL_2013_2020.csv', index=False)

    df = df.append(df1)
    df.to_csv('MTL_1941_2020.csv', index=False)

if __name__ == "__main__":
    main()