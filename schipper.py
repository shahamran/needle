import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import collections
import plotly.plotly as py
COUNTRY_NAMES = ['au','gb','us','ca']
DATETIME = 'datetime'
YEAR = 'year'
COUNTRY = 'country'
DATE_FORMAT = '%m/%d/%Y %H:%M'
FIX_TIME_REGEX = (r'\s24:(\d{2})\s*$', r' 00:\1')

def fix_time(d):
    return re.sub(*FIX_TIME_REGEX, d)

data = pd.read_csv('scrubbed.csv', low_memory=False)
dates = [dt.datetime.strptime(fix_time(d), DATE_FORMAT)
         for d in data[DATETIME]]
data[YEAR] = [d.year for d in dates]
years = np.unique(data[YEAR])
years = [year for year in years if not pd.isnull(year)]



def calcduration(duration):
    s = 0
    disqualified = 0
    for d in duration:
        try:
            #eliminate outliers
            #if a sighting lasts more than two days
            if(float(d)/3600 < 48):
                s = s+(float(d)/60)
            else:
                disqualified = disqualified+1
        except:
            pass
    return s,disqualified

def averageDurationPerYear():
    averageDurationPerYear = {}
    for year in years:
        num_sightings = len(data.loc[data[YEAR] == year, :])
        duration = data.loc[data[YEAR] == year, 'duration (seconds)']
        [sumOfDurations,disqualified] = calcduration(duration)
        averageDurationPerYear[year] = sumOfDurations/(num_sightings-disqualified)

    x = []
    y = []
    averageDurationPerYear = collections._OrderedDictItemsView(averageDurationPerYear)
    for key,val in averageDurationPerYear:
        x.append(key)
        y.append(val)
    plt.xlabel('Year')
    plt.ylabel('average time ogf sighting in minutes ')
    plt.title('average time of sighting each year')
    plt.plot(x, y, color="blue")
    plt.show()

def averageDurationPerCountry():
    averageDurationPerCountry = {}
    for country in COUNTRY_NAMES:
        num_sightings = len(data.loc[data[COUNTRY] == country , :])
        duration = data.loc[data[COUNTRY] == country, 'duration (seconds)']
        [sumOfDurations,disqualified] = calcduration(duration)
        averageDurationPerCountry[country] = sumOfDurations/(num_sightings - disqualified)
    x = []
    y = []

    for key,val in averageDurationPerCountry.items():
        x.append(key)
        y.append(val)
    plt.figure()
    plt.xlabel('country')
    plt.ylabel('average time ogf sighting in minutes ')
    plt.title('average time of sighting per counrty')
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y, align = 'center',alpha = 1.5)
    plt.xticks(y_pos,x)
    plt.show()


averageDurationPerYear()
averageDurationPerCountry()