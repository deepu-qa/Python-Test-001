import pandas as pd
from datetime import datetime
from pytz import timezone
import pytz

def get_time_in_pst(timeInMilli):
    date_format='%Y-%m-%d %H:%M:%S'

    date_time = datetime.fromtimestamp(timeInMilli/1000).strftime(date_format)

    # # Create datetime object in local timezone
    dt_utc = datetime.strptime(date_time, date_format)
    dt_utc = dt_utc.replace(tzinfo=pytz.UTC)
    date = dt_utc.astimezone(timezone('US/Pacific'))
    
    return date.strftime(date_format)

def read_jmeter_csv(input_file_name):
    col_list = ["timeStamp", "label", "responseCode", "responseMessage", "failureMessage"]
    df = pd.read_csv(input_file_name, usecols=col_list)
    # selecting rows where response code is not 200
    rslt_df = df[df['responseCode'] != 200] 

    for index, row in rslt_df.iterrows():
        pst_time = get_time_in_pst(row[0])
        print(f"Time={pst_time}")
        print(f"label={row[1]}")
        print(f"responseCode={row[2]}")
        print(f"responseMessage={row[3]}")
        print(f"failureMessage={row[4]}")
        print("===============")

if __name__ == "__main__":
    read_jmeter_csv("Inputs/Jmeter_log1.jtl")