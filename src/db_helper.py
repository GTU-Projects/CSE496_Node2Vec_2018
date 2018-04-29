from datetime import datetime
import json
import copy

class Tweet():
    def __init__(self,username, userID, tweetID, text,date):
        self.username = username
        self.text = text
        self.date = date
        self.userID = userID
        self.tweetID = tweetID

class DBHelper:

    def __init__(self):
        pass

    def connectMysql(self,user,passwd,db,host="localhost"):
        import MySQLdb
        self.db = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset="utf8",init_command="SET NAMES UTF8")
        self.cursor = self.db.cursor()

    def getTweetsFromMysql(self,tableName):
        self.cursor.execute(""" SELECT SentBy, UserID, ID, TextText, DateCreatedAt FROM {tname};""".format(tname=tableName))
        
        tweets = []
        for x in self.cursor.fetchall():
            # Input1: Wed Aug 10 01:34:24 EEST 2016 -> Wed Aug 10 01:34:24 EEST 2016 OUTPUT->
            formattedTime = x[4].replace("EEST","").replace("EET","")
            formattedTime = datetime.strptime(formattedTime,'%a %b %d %H:%M:%S %Y')
            tweets.append(Tweet(username=x[0],text=x[3],userID=x[1],tweetID=x[2],date=formattedTime))
        return tweets
    
    def getUniqueUserIDs(self, tableName):
        self.cursor.execute(""" SELECT DISTINCT UserID FROM {tname}""".format(tname=tableName))
        userIDs = [user[0] for user in self.cursor.fetchall()]
        return userIDs

    def getUserFriendIDs(self, tableName, userID):
        self.cursor.execute(""" SELECT FriendID FROM {tname} WHERE UserID={userID}""".format(tname=tableName,userID=userID))
        friendIDs = [friend[0] for friend in self.cursor.fetchall()]
        return friendIDs

def saveTweetsAsJson(filePath, tweets):
    
    with open(filePath,'w+') as f:
        tempList = []
        for tweet in tweets:
            temp = copy.copy(tweet)
            temp.date = temp.date.strftime("%Y-%m-%d %H:%M:%S")
            tempList.append(temp.__dict__)
        json.dump(fp=f, obj=tempList)
        
def getTweetsFromJson(filePath):
    
    tweetList = []
    with open(filePath,'r') as f:
        jsonObjs = json.load(f)
        
        for obj in jsonObjs:
            tweet = Tweet(**obj)
            tweet.date = datetime.strptime(tweet.date,"%Y-%m-%d %H:%M:%S")
            tweetList.append(tweet)
    return tweetList

if __name__=="__main__":
    dbHelper = DBHelper()

    # special config parameters wont work on your environment
    dbHelper.connect(user="root",passwd="Hasan5695*",db="SocialMediaDB")
    tweets= dbHelper.getTweets(tableName="denemeShort")
    print("TweetSentName:",tweets[0].sentName,"TweetSentText:",tweets[0].text,"TweetSentDate:",tweets[0].date)

    #serIDs = dbHelper.getUniqueUserIDs(tableName="Friends")
    #rint("UserIDs:",userIDs)

    #rint("########################")
    #riendIDs = dbHelper.getUserFriendIDs(tableName="Friends",userID=userIDs[0])
    #rint("User:",userIDs[0]," Friends:",friendIDs)
