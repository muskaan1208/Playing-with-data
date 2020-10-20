# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:47:30 2020

@author: gupta
"""
import random
import pandas as pd
import random
import csv
import time
import datetime
from datetime import datetime
from datetime import timedelta

'''
def days():
   
    start_date = datetime.date(2020,1,1)
    end_date = datetime.date(2020,12,30)
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date
'''

def random_date():
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    start = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    end = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)



#d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
#d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')

#print(random_date(d1, d2))

def values():
    digits = '0123456789'
    global available_beds 
    contact = random.choice('12')
    for i in range(random.randint(1,2)):
        contact += random.choice(digits)
    return contact


with open('data2.csv','w',newline='') as f:
    w =csv.writer(f)
    w.writerow(['TIMESTMAP','Values2'])
   # start_time = time.time()
    for i in range(100):
        # get_patient_data()
        w.writerow([random_date(),values()])
                   
    print("writen data to file")  