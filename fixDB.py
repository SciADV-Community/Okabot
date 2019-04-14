from logger import logger
import sqlite3, os

dbPath = "./db/"
dbFile = "fix.sqlite"

tableName = "fixes"

p1 = 'term'
p1Type = 'text'
c2 = 'fixID'
c2Type = 'text'


# For checking on startup
def verifyDB():
    if not os.path.exists(dbPath):
        logger.info("Folder does not exist")
        os.mkdir(dbPath)

    if len(os.listdir(dbPath)) != 0:
        if not (os.path.isfile(dbPath + dbFile)):
            connectDB()

    else:
        connectDB()


def loadCache():
    conn, c = connectDB()
    c.execute("SELECT * FROM {}".format(tableName))
    rows = c.fetchall()
    fixDict = {}

    for row in rows:
        fixDict[row[0]] = row[1]

    return fixDict

# Connect or, if non-existent, create db file
def connectDB():
    conn = sqlite3.connect(dbPath + dbFile)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS '{tn}' ({p1} {c2Type}, {c2} {c2Type})".
              format(tn=tableName, p1=p1, p1Type=p1Type, c2=c2, c2Type=c2Type))
    return conn, c
