import MySQLdb

class DBHelper:

    def __init__(self):
        pass

    def connect(self,user,passwd,db,host="localhost"):
        self.db = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset="utf8",init_command="SET NAMES UTF8")
        self.cursor = self.db.cursor()

    def getTweets(self,tableName):
        self.cursor.execute(""" SELECT * FROM {tname} """.format(tname=tableName))
        return self.cursor.fetchall()

    def getNextTweet(self,tableName):
        self.cursor.execute(""" SELECT * FROM {tname} """.format(tname=tableName))
        return self.cursor.fetchone()

if __name__=="__main__":
    dbHelper = DBHelper()

    # special config parameters wont work on your environment
    dbHelper.connect(user="root",passwd="Hasan5695*",db="cse496")
    tweet = dbHelper.getNextTweet(tableName="denemeShort")
    print("Tweet",tweet)

