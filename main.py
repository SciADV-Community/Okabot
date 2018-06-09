from reply import response_load, congroo_reply, kyouma_reply, tutturu_reply, luka_reply, upa_reply, nullpo_reply
from postDB import verifyDB, queryDB
from datetime import datetime
from time import sleep
import praw,prawcore
import re
import logging


print("---------------------------------------------")
print("   ______      _          _ _____     __     ")
print("  / __/ /____ (_)__  ___ (_) ___/__ _/ /____ ")
print(" _\ \/ __/ -_) / _ \(_-<_ / (_ / _ `/ __/ -_)")
print("/___/\__/\__/_/_//_/___( )\___/\_,_/\__/\__/ ")
print("                       |/                    ")
print("---------------------------------------------")
print("「 Future Gadget 38, 4th Edition Ver. 1.62 」 ")
print()


logging.basicConfig(filename="okabot.log")
print("Logging enabled")

response_load()
print("Responses loaded")

verifyDB()
print("Post Database loaded")

reddit = praw.Reddit("Okabot")
subreddit = reddit.subreddit("steinsgate")

print("Connection established")
print("Stream Connected")
print("---------------------------------------------")

while (True):
    try:
        for comment in subreddit.stream.comments():
            if comment.author != "Okabot":
                if queryDB(comment.submission, comment.id) == False:
                    try:
                        if re.search("El[\s\W]+Psy[\s\W]+Cong([a-z]*)", comment.body, re.IGNORECASE):
                            print("Found: " + str(comment.submission) + " " + comment.id + "- ESK")
                            arg = re.search("El[\s\W]+Psy[\s\W]+Cong([a-z]*)", str(comment.body), re.IGNORECASE)
                            correction = "Kong" + arg.group(1)

                            congroo_reply(comment, correction, arg)


                        if (re.search("Ho(u)?oin Kyo(u)?ma", comment.body, re.IGNORECASE) or
                            (re.search("Ho(u)?oin Kyouma", comment.body, re.IGNORECASE)) or
                            (re.search("Hououin Kyoma", comment.body, re.IGNORECASE))):
                            print("Found: " + str(comment.submission) + " " + comment.id + "- KYOUMA")

                            kyouma_reply(comment)


                        if (re.search("T[u,o]{2}[\s,-]?T[u,o]{2}[\s,-]?r[u,o]?[u,o]?", comment.body, re.IGNORECASE) or
                            (re.search("Tuturu", comment.body, re.IGNORECASE))):
                            print("Found: " + str(comment.submission) + " " + comment.id + "- TTR")

                            tutturu_reply(comment)


                        if re.search("ruka[k]?[o]?", comment.body, re.IGNORECASE):
                            print("Found: " + str(comment.submission) + " " + comment.id + "- RUKA")

                            luka_reply(comment)


                        if re.search("\W[o]{1,2}pa\W", comment.body, re.IGNORECASE):
                            print("Found: " + str(comment.submission) + " " + comment.id + "- RUKA")

                            upa_reply(comment)


                        if re.search("nullpo", comment.body, re.IGNORECASE):
                            print("Found: " + str(comment.submission) + " " + comment.id + "- NULL")
                            nullpo_reply(comment)


                    except praw.exceptions.APIException as e:
                        if "THREAD_LOCKED" in (str(e)):
                            print("Gah! (Thread Locked)\n")
                        elif "RATELIMIT" in (str(e)):
                            print("But I refuse. (RATELIMIT)\n")
                            logging.warning(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
                            pass
                        else: print(str(e))

                    except praw.exceptions.ClientException as e:
                        print(str(e))
                        print("Woah, I shouldn't waste all day on Reddit. (ClientException)\n")
                        logging.warning(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
                        pass

                    except prawcore.exceptions.Forbidden as e:
                        print(str(e))
                        print("Very well. Time Leap Machine it is. (Forbidden)\n")
                        logging.warning(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
                        pass
                else:
                    print("That's why we love you! That's why we admire you! (Response Exists: " +
                         str(comment.submission) + " " + comment.id + ")\n")

    except prawcore.exceptions.RequestException as e:
        print("You guys are hopeless. Better do something quick. (Connection failure)\n")
        logging.warning(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
        sleep(300)
        pass

    except prawcore.exceptions.ResponseException as e:
        print(str(e))
        # Need a meme here
        logging.warning(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
        sleep(300)
        pass