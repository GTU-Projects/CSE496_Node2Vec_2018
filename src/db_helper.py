import MySQLdb
from datetime import datetime

class Tweet():
    def __init__(self,sentName,text,date):
        self.sentName = sentName
        self.text = text
        self.date = date

class DBHelper:

    def __init__(self):
        pass
    

    def connect(self,user,passwd,db,host="localhost"):
        self.db = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset="utf8",init_command="SET NAMES UTF8")
        self.cursor = self.db.cursor()

    def getTweets(self,tableName):
        self.cursor.execute(""" SELECT * FROM {tname} ORDER BY DateCreatedAt ASC;""".format(tname=tableName))
        
        tweets = []
        for x in self.cursor.fetchall():
            # Input1: Wed Aug 10 01:34:24 EEST 2016 -> Wed Aug 10 01:34:24 EEST 2016 OUTPUT->
            formattedTime = x[7].replace("EEST","").replace("EET","")
            formattedTime = datetime.strptime(formattedTime,'%a %b %d %H:%M:%S %Y')
            tweets.append(Tweet(x[0],x[5],formattedTime))
        return tweets

    def getUniqueUserIDs(self, tableName):
        self.cursor.execute(""" SELECT DISTINCT UserID FROM {tname}""".format(tname=tableName))
        userIDs = [user[0] for user in self.cursor.fetchall()]
        return userIDs

    def getUserFriendIDs(self, tableName, userID):
        self.cursor.execute(""" SELECT FriendID FROM {tname} WHERE UserID={userID}""".format(tname=tableName,userID=userID))
        friendIDs = [friend[0] for friend in self.cursor.fetchall()]
        return friendIDs

if __name__=="__main__":
    dbHelper = DBHelper()

    # special config parameters wont work on your environment
    dbHelper.connect(user="root",passwd="Hasan5695*",db="cse496")
    tweets= dbHelper.getTweets(tableName="denemeShort")
    print("TweetSentName:",tweets[0].sentName,"TweetSentText:",tweets[0].text,"TweetSentDate:",tweets[0].date)

    #serIDs = dbHelper.getUniqueUserIDs(tableName="Friends")
    #rint("UserIDs:",userIDs)

    #rint("########################")
    #riendIDs = dbHelper.getUserFriendIDs(tableName="Friends",userID=userIDs[0])
    #rint("User:",userIDs[0]," Friends:",friendIDs)
