import requests
import argparse
import os
from datetime import timedelta, datetime
import pandas as pd
import json
import http.client


import config

rename_header = { 0  : 'ReportDt', 1  : 'Unit', 2  : 'Power'}

def get_yesterday_date(fetch_date):
    return datetime.strptime(fetch_date, '%m/%d/%Y').date() - timedelta(1)


def import_data():
    url = config.REACTOR_API
    data = requests.get(url).text
    return data
    

def transform_data(data):
    df = pd.DataFrame(pd.read_csv(data,delimiter = "\t"))
    df = df['ReportDt|Unit|Power'].str.split('|',expand=True)
    df = df.rename(columns={0: 'ReportDt', 1: 'Unit',2:'Power'})
    df['ReportDate'] =  df['ReportDt'].str.split(" ",expand=True)[0]
    df['ReportTime'] = df['ReportDt'].str.split(" ",expand=True)[1]
    df['ReportPeriod'] = df['ReportDt'].str.split(" ",expand=True)[2] 
    df = df.drop('ReportDt',axis=1) 
    return df

def get_new_data(df, fetch_date):
    yesterday = get_yesterday_date(fetch_date)
    df = df.sort_values(by=['ReportDt'], ascending=True)
    data_to_append = df[(df['ReportDt'].dt.date == yesterday)]
    return data_to_append

# def save_new_data_to_csv(data_to_append, fetch_date):
#     filename = get_file_path(fetch_date)
#     if not data_to_append.empty:
#         data_to_append(filename, encoding='utf-8', index=False)

def main(fetch_date):
    data = import_data()
    df = transform_data(data)
    data_to_append = get_new_data(df, fetch_date)
    print(data_to_append)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, type=str)
    args = parser.parse_args()
    main(args.date)