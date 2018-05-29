from reply import congroo_reply, tutturu_reply, luka_reply, nullpo_reply
from postDB import verifyDB, queryDB, appendDB
from datetime import datetime
import praw,prawcore
import re
import logging


print("---------------------------------------------")
print()
print("  / __/ /____ (_)__  ___ (_) ___/__ _/ /____ ")
print(" _\ \/ __/ -_) / _ \(_-<_ / (_ / _ `/ __/ -_)")
print("/___/\__/\__/_/_//_/___( )\___/\_,_/\__/\__/ ")
print("                       |/                    ")
print("---------------------------------------------")


logging.basicConfig(filename="okabot.log")
print("Logging enabled")

verifyDB()
print("Post Database loaded")

reddit = praw.Reddit("Okabot")
subreddit = reddit.subreddit("steinsgate")
print("Connection established")

print("Stream search activated")
print("---------------------------------\n")

for comment in subreddit.stream.comments():
    if comment.author != "Okabot":
        if queryDB(comment.submission, comment.id) == False:
            try:
                if re.search("El[\s\W]+Psy[\s\W]+Cong([a-z]*)", comment.body, re.IGNORECASE):
                    print("Found: " + str(comment.submission) + " " + comment.id + "- ESK")
                    arg = re.search("El[\s\W]+Psy[\s\W]+Cong([a-z]*)", str(comment.body), re.IGNORECASE)
                    correction = "Kong" + arg.group(1)

                    congroo_reply(comment, correction, arg)

                if (re.search("T[u,o]{2}[\s,-]?T[u,o]{2}[\s,-]?r[u,o]?[u,o]?", comment.body, re.IGNORECASE) or
                    (re.search("Tuturu", comment.body, re.IGNORECASE))):
                    print("Found: " + str(comment.submission) + " " + comment.id + "- TTR")

                    tutturu_reply(comment)

                if re.search("ruka[k]?[o]?", comment.body, re.IGNORECASE):
                    print("Found: " + str(comment.submission) + " " + comment.id + "- RUKA")

                    luka_reply(comment)

                if re.search("nullpo", comment.body, re.IGNORECASE):
                    print("Found: " + str(comment.submission) + " " + comment.id + "- NULL")
                    nullpo_reply(comment)


            except praw.exceptions.APIException as e:
                if "THREAD_LOCKED" in (str(e)):
                    print("Gah! (Thread Locked)\n")
                elif "RATELIMIT" in (str(e)):
                    print("Woah, I shouldn't waste all day on Reddit. (RATELIMIT)\n")
                    logging.warning(datetime.now().strftime("%Y-%m-%d %H:%M") + " - Rate Limit")
                else: print(str(e))

            except praw.exceptions.ClientException as e:
                print(str(e))
                print("You guys are hopeless. Better do something quick. (ClientException)\n")
                logging.warning(datetime.now().strftime("%Y-%m-%d %H:%M") + " - ClientException")

            except prawcore.exceptions.Forbidden as e:
                print(str(e))
                print("Very well. Time Leap Machine it is. (Forbidden)\n")
                logging.warning(datetime.now().strftime("%Y-%m-%d %H:%M") + " - Forbidden")

        else:
            print("That's why we love you! That's why we admire you! (Response Exists: " +
                  str(comment.submission) + " " + comment.id + ")")