# -*- coding: utf-8 -*-

import datetime
import calendar
import sys

def main(this_year, interval):
    
    # Search range: [this_year - interval, interval)

    # Same January
    print("January is same as: ")
    for y in range(this_year - interval, this_year):
        if datetime.date(y, 1, 1).isoweekday() == \
           datetime.date(this_year, 1, 1).isoweekday():
               print(y)

    # Same February
    print("February is same as: ")
    for y in range(this_year - interval, this_year):
        if calendar.monthrange(this_year, 2) == calendar.monthrange(y, 2):
            print(y)

    # Other Months
    print("Other months are same as: ")
    for y in range(this_year - interval, this_year):
        if datetime.date(y, 3, 1).isoweekday() == \
           datetime.date(this_year, 3, 1).isoweekday():
               print(y)

if __name__ == "__main__":
    
    year = int(sys.argv[1])
    interval = int(sys.argv[2])
    
    main(year, interval)
