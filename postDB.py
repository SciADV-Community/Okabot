import sqlite3, os

dbPath = "./db/"
dbFile = "post.sqlite"

tableName = "comments"

p1 = 'submissionID'
p1Type = 'text'
c2 = 'commentID'
c2Type = 'text'


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
def queryDB(postID, commentID):
    conn, c = connectDB()
    result = c.execute("SELECT * FROM {tn} WHERE {p1}=('{pid}') AND {c2}==('{cid}')".
                       format(tn=tableName, p1=p1, pid=postID, c2=c2, cid=commentID)).fetchall()
    conn.commit()
    conn.close()

    if len(result) == 0:
        return False
    else:
        return True

# Add posts that have been checked
def appendDB(postID, commentID):
    conn, c = connectDB()
    c.execute("INSERT INTO {tn} ({p1},{c2}) VALUES ('{pid}','{cid}')".
        format(tn=tableName, p1=p1, pid=postID, c2=c2, cid=commentID))

    conn.commit()
    conn.close()

# Connect or, if non-existent, create db file
def connectDB():
    conn = sqlite3.connect(dbPath + dbFile)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS '{tn}' ({p1} {c2Type}, {c2} {c2Type})".
              format(tn=tableName, p1=p1, p1Type=p1Type, c2=c2, c2Type=c2Type))
    return conn, c



#verifyDB()
#for x in range(1,100):
#    appendDB(x)
