import networkx as nx
import numpy as np

MONTH_TAG="month"
YEAR_TAG="year"
DAY_TAG="day"

MONTH_NAMES = {1:"JAN",2:"FEB",3:"MAR",4:"APR",
          5:"MAY",6:"JUN",7:"JUL",8:"AUG",
         9:"SEP",10:"OCT",11:"NOV",12:"DEC"}


def create_time_graph1(tweets):
    G = nx.Graph()
    G.add_node(YEAR_TAG)
    G.add_node(MONTH_TAG)
    G.add_node(DAY_TAG)

        # Draw Graph According to Page3

    #for i in range(0,10000):
    #    tweet = tweets[i]
    for tweet in tweets:
        # connect Year edges
        G.add_edge(tweet.date.year,MONTH_NAMES[tweet.date.month],weight=1.0)
        G.add_edge(tweet.date.year,YEAR_TAG,weight=1.0)
        # connect month edges
        G.add_edge(MONTH_NAMES[tweet.date.month],MONTH_TAG,weight=1.0)
        G.add_edge(MONTH_NAMES[tweet.date.month],tweet.date.day,weight=1.0)
        # connect day edges
        G.add_edge(tweet.date.day,DAY_TAG,weight=1.0)
    return G

def create_time_graph2(tweets):
    G1 = nx.DiGraph()
    G1.add_node(YEAR_TAG)
    G1.add_node(MONTH_TAG)

    prevYear = None
    prevMonth = None

    prevYear = tweets[0].date.year
    prevMonth = tweets[0].date.month

    for tweet in tweets:
                    
        G1.add_edge(YEAR_TAG,str(tweet.date.year),weight=15.0)
        
        if(prevYear < tweet.date.year):
            G1.add_edge(str(prevYear),str(tweet.date.year),weight=12.0)
            prevYear = tweet.date.year
            prevMonth = tweet.date.month
            
        monthFormat = "{month} {year}".format(month=MONTH_NAMES[tweet.date.month],year=tweet.date.year)
        if(prevMonth < tweet.date.month):
            prevMonthFormat = "{month} {year}".format(month=MONTH_NAMES[prevMonth],year=tweet.date.year)
            G1.add_edge(prevMonthFormat,monthFormat,weight=4.0)
            prevMonth = tweet.date.month
        
        G1.add_edge(str(tweet.date.year),monthFormat,weight=4.0)
        #G1.add_edge(MONTH_TAG,monthFormat,weight=8.0)
    return G1

def create_time_graph3(tweets):
    G1 = nx.DiGraph()
    G1.add_node(YEAR_TAG)
    G1.add_node(MONTH_TAG)
    G1.add_node(DAY_TAG)

    prevYear = None
    prevMonth = None
    prevDay = None

    prevYear = tweets[0].date.year
    prevMonth = tweets[0].date.month
    prevDay = tweets[0].date.day

    for tweet in tweets:
        G1.add_edge(YEAR_TAG,str(tweet.date.year),weight=30.0)
        
        if(prevYear < tweet.date.year):
            G1.add_edge(str(prevYear),str(tweet.date.year),weight=40.0)
            prevYear = tweet.date.year
            prevMonth = tweet.date.month
            prevDay = tweet.date.day
          
        monthFormat = "{month}.{year}".format(month=MONTH_NAMES[tweet.date.month],year=tweet.date.year)
        G1.add_edge(str(tweet.date.year),monthFormat,weight=10.0)
        
        if(prevMonth < tweet.date.month):
            prevMonthFormat = "{month}.{year}".format(month=MONTH_NAMES[prevMonth],year=tweet.date.year)
            G1.add_edge(prevMonthFormat,monthFormat,weight=15.0)
            prevMonth = tweet.date.month
            prevDay = tweet.date.day
        
        #G1.add_edge(MONTH_TAG,monthFormat,weight=1.0)
        fullDateFormat = "{day}.{month}.{year}".format(day=tweet.date.day,month=tweet.date.month,year=tweet.date.year)
        if prevDay < tweet.date.day:
            prevFullDateFormat = "{day}.{month}.{year}".format(day=prevDay,month=tweet.date.month,year=tweet.date.year)
            G1.add_edge(prevFullDateFormat,fullDateFormat,weight=1.0)
            prevDay = tweet.date.day

        G1.add_edge(monthFormat,fullDateFormat,weight=3.0)
        
        #G1.add_edge(DAY_TAG,fullDateFormat,weight=1.0)
       
    return G1

def create_time_graph3_no_weight(tweets):
    G1 = nx.DiGraph()
    G1.add_node(YEAR_TAG)
    G1.add_node(MONTH_TAG)
    G1.add_node(DAY_TAG)

    prevYear = None
    prevMonth = None
    prevDay = None

    prevYear = tweets[0].date.year
    prevMonth = tweets[0].date.month
    prevDay = tweets[0].date.day

    for tweet in tweets:
        G1.add_edge(YEAR_TAG,str(tweet.date.year),weight=1.0)
        
        if(prevYear < tweet.date.year):
            G1.add_edge(str(prevYear),str(tweet.date.year),weight=1.0)
            prevYear = tweet.date.year
            prevMonth = tweet.date.month
            prevDay = tweet.date.day
          
        monthFormat = "{month}.{year}".format(month=MONTH_NAMES[tweet.date.month],year=tweet.date.year)
        G1.add_edge(str(tweet.date.year),monthFormat,weight=1.0)
        
        if(prevMonth < tweet.date.month):
            prevMonthFormat = "{month}.{year}".format(month=MONTH_NAMES[prevMonth],year=tweet.date.year)
            G1.add_edge(prevMonthFormat,monthFormat,weight=1.0)
            prevMonth = tweet.date.month
            prevDay = tweet.date.day
        
        #G1.add_edge(MONTH_TAG,monthFormat,weight=1.0)
        fullDateFormat = "{day}.{month}.{year}".format(day=tweet.date.day,month=tweet.date.month,year=tweet.date.year)
        if prevDay < tweet.date.day:
            prevFullDateFormat = "{day}.{month}.{year}".format(day=prevDay,month=tweet.date.month,year=tweet.date.year)
            G1.add_edge(prevFullDateFormat,fullDateFormat,weight=1.0)
            prevDay = tweet.date.day

        G1.add_edge(monthFormat,fullDateFormat,weight=1.0)
        
        #G1.add_edge(DAY_TAG,fullDateFormat,weight=1.0)
       
    return G1