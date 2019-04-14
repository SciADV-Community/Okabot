from logger import logger
from datetime import datetime
from reply import response_load, comment_reply
import praw,prawcore
import postDB, fixDB
import time

logger.info("Initializing Okabot")

logger.debug("---------------------------------------------")
logger.debug("   ______      _          _ _____     __     ")
logger.debug("  / __/ /____ (_)__  ___ (_) ___/__ _/ /____ ")
logger.debug(" _\ \/ __/ -_) / _ \(_-<_ / (_ / _ `/ __/ -_)")
logger.debug("/___/\__/\__/_/_//_/___( )\___/\_,_/\__/\__/ ")
logger.debug("                       |/                    ")
logger.debug("---------------------------------------------")

response_load()
logger.debug("Responses loaded")

fixDB.verifyDB()
logger.debug("Fix Database loaded")
postDB.verifyDB()
logger.debug("Post Database loaded")

reddit = praw.Reddit("Okabot")
subreddit = reddit.subreddit("okabotplayground")

logger.debug("Connection established")
logger.info("Stream Connected")
logger.info("---------------------------------------------")

cacheTime = 0

while (True):
    try:
        for comment in subreddit.stream.comments():
            if comment.author != "Okabot":
                if postDB.queryDB(comment.submission, comment.id) == False:
                    try:
                        ## Caching to decrease reads on the sqlite database
                        ## Fix database will never be writelocked, so feel free to update while running
                        if time.time() - cacheTime > 3600:
                            fixDict = fixDB.loadCache()

                        # See if the terms in the dict are contained within the message
                        for term in fixDict:
                            if term in comment.body:
                                fixID = fixDict[term]
                                comment_reply(fixID, comment)

                    except praw.exceptions.APIException as e:
                        if "THREAD_LOCKED" in (str(e)):
                            logger.warning("Gah! (Thread Locked)\n")
                        elif "RATELIMIT" in (str(e)):
                            print("But I refuse. (RATELIMIT)\n")
                            logger.error(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
                            pass
                        else: logger.critical(str(e))

                    except praw.exceptions.ClientException as e:
                        print(str(e))
                        print("Woah, I shouldn't waste all day on Reddit. (ClientException)\n")
                        logger.critical(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
                        pass

                    except prawcore.exceptions.Forbidden as e:
                        print(str(e))
                        print("Very well. Time Leap Machine it is. (Forbidden)\n")
                        logger.critical(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
                        pass
                else:
                    logger.debug("That's why we love you! That's why we admire you! (Response Exists: " +
                         str(comment.submission) + " " + comment.id + ")\n")

    except prawcore.exceptions.RequestException as e:
        print("You guys are hopeless. Better do something quick. (Connection failure)\n")
        logger.error(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
        time.sleep(300)
        pass

    except prawcore.exceptions.ResponseException as e:
        print(str(e))
        # Need a meme here
        logger.error(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
        time.sleep(300)
        pass