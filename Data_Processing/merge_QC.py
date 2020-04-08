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

    nm = "en_climate_daily_QC_701S001_1992_P1D.csv"
    df = read_file(nm)

    for i in range(1993,2020):
        nm = "en_climate_daily_QC_701S001_" + str(i) + "_P1D.csv"
        df4 = read_file(nm)
        df = df.append(df4)
        print(i)

    df.to_csv('QC_1992_2020.csv', index=False)

    nm = "en_climate_daily_QC_7016293_2013_P1D.csv"
    df1 = read_file(nm)

    for i in range(2014,2021):
        nm = "en_climate_daily_QC_7016293_" + str(i) + "_P1D.csv"
        df4 = read_file(nm)
        df1 = df1.append(df4)
        print(i)

    df1.to_csv('QC_2013_2020.csv', index=False)

    nm = "en_climate_daily_QC_7016294_1943_P1D.csv"
    df2 = read_file(nm)

    for i in range(1944,2018):
        nm = "en_climate_daily_QC_7016294_" + str(i) + "_P1D.csv"
        df4 = read_file(nm)
        df2 = df2.append(df4)
        print(i)

    df2.to_csv('QC_1943_2017.csv', index=False)


    df = df.append(df1)
    df = df.append(df2)
    df.to_csv('QC_1943_2020.csv', index=False)

if __name__ == "__main__":
    main()