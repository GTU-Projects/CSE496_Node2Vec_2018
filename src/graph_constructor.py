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
        G.add_edge(tweet.date.year,MONTH_NAMES[tweet.date.month])
        G.add_edge(tweet.date.year,YEAR_TAG)
        # connect month edges
        G.add_edge(MONTH_NAMES[tweet.date.month],MONTH_TAG)
        G.add_edge(MONTH_NAMES[tweet.date.month],tweet.date.day)
        # connect day edges
        G.add_edge(tweet.date.day,DAY_TAG)
    return G

def create_time_graph2(tweets):
    G1 = nx.Graph()
    G1.add_node(YEAR_TAG)
    G1.add_node(MONTH_TAG)

    prevYear = None
    prevMonth = None

    prevYear = tweets[0].date.year
    prevMonth = tweets[0].date.month

    for tweet in tweets:
                    
        G1.add_edge(YEAR_TAG,tweet.date.year,weight=tweet.date.year)
        
        if(prevYear < tweet.date.year):
            G1.add_edge(prevYear,tweet.date.year)
            prevYear = tweet.date.year
            prevMonth = tweet.date.month
            
        monthFormat = "{month} {year}".format(month=MONTH_NAMES[tweet.date.month],year=tweet.date.year)
        if(prevMonth < tweet.date.month):
            prevMonthFormat = "{month} {year}".format(month=MONTH_NAMES[prevMonth],year=tweet.date.year)
            G1.add_edge(prevMonthFormat,monthFormat)
            prevMonth = tweet.date.month
        
        G1.add_edge(tweet.date.year,monthFormat)
        G1.add_edge(MONTH_TAG,monthFormat,month=tweet.date.month, year=tweet.date.year)
    return G1

def create_time_graph3(tweets):
    G1 = nx.Graph()
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
        G1.add_edge(YEAR_TAG,tweet.date.year,weight=tweet.date.year)
        
        if(prevYear < tweet.date.year):
            G1.add_edge(prevYear,tweet.date.year)
            prevYear = tweet.date.year
            prevMonth = tweet.date.month
            prevDay = tweet.date.day
            
        monthFormat = "{month}.{year}".format(month=MONTH_NAMES[tweet.date.month],year=tweet.date.year)
        if(prevMonth < tweet.date.month):
            prevMonthFormat = "{month}.{year}".format(month=MONTH_NAMES[prevMonth],year=tweet.date.year)
            G1.add_edge(prevMonthFormat,monthFormat)
            prevMonth = tweet.date.month
            prevDay = tweet.date.day

        G1.add_edge(MONTH_TAG,monthFormat)
        G1.add_edge(tweet.date.year,monthFormat)

        fullDateFormat = "{day}.{month}.{year}".format(day=tweet.date.day,month=tweet.date.month,year=tweet.date.year)
        if prevDay < tweet.date.day:
            prevFullDateFormat = "{day}.{month}.{year}".format(day=tweet.date.day,month=prevMonth,year=tweet.date.year)
            G1.add_edge(prevFullDateFormat,fullDateFormat)
            prevDay = tweet.date.day

        G1.add_edge(monthFormat,fullDateFormat)
        
        G1.add_edge(DAY_TAG,fullDateFormat)
       
    return G1