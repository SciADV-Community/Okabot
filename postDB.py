import sqlite3, os, re

dbPath = "./db/"
dbFile = "post.sqlite"

tableName = ""

p1 = 'postID'
p1Type = 'text'


# For checking on startup
def verifyDB():
    if not os.path.exists(dbPath):
        print("Folder does not exist")
        os.mkdir(dbPath)

    if len(os.listdir(dbPath)) != 0:
        if not (os.path.isfile(dbPath + dbFile)):
            connectDB()
    else:
        connectDB()

# Check if post has been checked
def queryDB(postID):
    print()

# Add posts that have been checked
def appendDB(postID):
    print()

# Connect or, if non-existent, create db file
def connectDB():
    conn = sqlite3.connect(dbPath + dbFile)
    c = conn.cursor()
