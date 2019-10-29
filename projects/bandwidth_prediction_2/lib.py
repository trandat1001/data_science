import numpy as np
import pandas as pd
from datetime import datetime

def convert_datetime_to_timestamp(strDate):
    #timestamp = datetime.strptime(strDate, "%Y-%m-%d")
    timestamp = pd.Timestamp(strDate)
    
    return timestamp.timestamp()

def get_date_in_month(strDate):
    #timestamp = datetime.strptime(strDate, "%Y-%m-%d")
    dt = pd.to_datetime(strDate)
    
    return dt.day

def get_date_in_week(strDate):
    #timestamp = datetime.strptime(strDate, "%Y-%m-%d")
    dt = pd.to_datetime(strDate)
    
    return dt.dayofweek

def hour_to_shift(hour):
    return hour // 8