from logger import logger
from reply import response_load, congroo_reply, kyouma_reply, tutturu_reply, luka_reply, upa_reply, stein_reply, nullpo_reply
from postDB import verifyDB, queryDB
from datetime import datetime
from time import sleep
import praw,prawcore
import re



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

verifyDB()
logger.debug("Post Database loaded")

reddit = praw.Reddit("Okabot")
subreddit = reddit.subreddit("okabotplayground")

logger.debug("Connection established")
logger.info("Stream Connected")
logger.info("---------------------------------------------")

while (True):
    try:
        for comment in subreddit.stream.comments():
            if comment.author != "Okabot":
                if queryDB(comment.submission, comment.id) == False:
                    try:
                        if (re.search("El[\s\W]+Psy[\s\W]+Cong([a-z]*)", comment.body, re.IGNORECASE) and \
                            not re.search("El Psy Kongroo", comment.body, re.IGNORECASE)):
                            logger.debug("Found: " + str(comment.submission) + " " + comment.id + "- ESK")
                            arg = re.search("El[\s\W]+Psy[\s\W]+Cong([a-z]*)", str(comment.body), re.IGNORECASE)
                            correction = "Kong" + arg.group(1)

                            congroo_reply(comment, correction, arg.group(1))


                        if ((re.search("Ho(u)?oin Kyo(u)?ma", comment.body, re.IGNORECASE) or
                            (re.search("Ho(u)?oin Kyouma", comment.body, re.IGNORECASE)) or
                            (re.search("Hououin Kyoma", comment.body, re.IGNORECASE))) and
                            not re.search("Hououin Kyouma", comment.body, re.IGNORECASE)):
                            logger.debug("Found: " + str(comment.submission) + " " + comment.id + "- KYOUMA")

                            kyouma_reply(comment)


                        if ((re.search("T[u,o]{2}[\s,-]?T[u,o]{2}[\s,-]?r[u,o]?[u,o]?", comment.body, re.IGNORECASE) or
                            (re.search("Tuturu", comment.body, re.IGNORECASE))) and
                            not re.search("Tutturu", comment.body, re.IGNORECASE)):
                            logger.debug("Found: " + str(comment.submission) + " " + comment.id + "- TTR")

                            tutturu_reply(comment)


                        if (re.search("(\A|\W)ruka[k]?[o]?", comment.body, re.IGNORECASE) and
                            not re.search("(\A|\W)luka", comment.body, re.IGNORECASE)):
                            logger.debug("Found: " + str(comment.submission) + " " + comment.id + "- RUKA")

                            luka_reply(comment)


                        if (re.search("\W[o]{1,2}pa\W", comment.body, re.IGNORECASE) and
                            not re.search("(\A|\W)luka", comment.body, re.IGNORECASE)):
                            logger.debug("Found: " + str(comment.submission) + " " + comment.id + "- OPA")

                            upa_reply(comment)

                        if (re.search("stein\'s gate", comment.body, re.IGNORECASE) and
                            not re.search("steins(\;|\s)gate", comment.body, re.IGNORECASE)):
                            logger.debug("Found: " + str(comment.submission) + " " + comment.id + "- SG")

                            stein_reply(comment)

                        if re.search("nullpo", comment.body, re.IGNORECASE):
                            logger.debug("Found: " + str(comment.submission) + " " + comment.id + "- NULL")
                            nullpo_reply(comment)


                    except praw.exceptions.APIException as e:
                        if "THREAD_LOCKED" in (str(e)):
                            logging.warning("Gah! (Thread Locked)\n")
                        elif "RATELIMIT" in (str(e)):
                            print("But I refuse. (RATELIMIT)\n")
                            logging.error(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
                            pass
                        else: logging.critical(str(e))

                    except praw.exceptions.ClientException as e:
                        print(str(e))
                        print("Woah, I shouldn't waste all day on Reddit. (ClientException)\n")
                        logging.critical(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
                        pass

                    except prawcore.exceptions.Forbidden as e:
                        print(str(e))
                        print("Very well. Time Leap Machine it is. (Forbidden)\n")
                        logging.critical(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
                        pass
                else:
                    logger.debug("That's why we love you! That's why we admire you! (Response Exists: " +
                         str(comment.submission) + " " + comment.id + ")\n")

    except prawcore.exceptions.RequestException as e:
        print("You guys are hopeless. Better do something quick. (Connection failure)\n")
        logging.error(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
        sleep(300)
        pass

    except prawcore.exceptions.ResponseException as e:
        print(str(e))
        # Need a meme here
        logging.error(datetime.now().strftime("%Y-%m-%d %H:%M") + " - " + str(e))
        sleep(300)
        pass
