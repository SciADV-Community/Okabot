from reply import congroo_reply, tutturu_reply, luka_reply, nullpo_reply
import praw,prawcore
import re
import random


reddit = praw.Reddit("Okabot")
subreddit = reddit.subreddit("steinsgate")
#subreddit = reddit.subreddit("OkabotPlayground")


print("Stream search activated")
print("---------------------------------\n")

for comment in subreddit.stream.comments():
    #print(str(comment.author) + ": " + str(comment.body))

    if comment.author != "Okabot":
        try:
            if re.search("El[\s\W]+Psy[\s\W]+Cong([a-z]*)", comment.body, re.IGNORECASE):
                print("Found: " + comment.id)
                arg = re.search("El[\s\W]+Psy[\s\W]+Cong([a-z]*)", str(comment.body), re.IGNORECASE)
                correction = "Kong" + arg.group(1)

                congroo_reply(comment, correction, arg)

            if (re.search("T[u,o]{2}[\s,-]?T[u,o]{2}[\s,-]?r[u,o]?[u,o]?", comment.body, re.IGNORECASE) or
                (re.search("Tuturu", comment.body, re.IGNORECASE))):
                print("Found: " + comment.id)

                tutturu_reply(comment)

            if re.search("ruka[k]?[o]?", comment.body, re.IGNORECASE):
                print("Found: " + comment.id)

                luka_reply(comment)

            if re.search("nullpo", comment.body, re.IGNORECASE):
                nullpo_reply(comment)


        except praw.exceptions.APIException as e:
            if "THREAD_LOCKED" in (str(e)):
                print("Gah! (Thread Locked)\n")
            elif "RATELIMIT" in (str(e)):
                print("Woah, I shouldn't waste all day on Reddit. (RATELIMIT)\n")
            else: print(str(e))
        except praw.exceptions.ClientException as e:
            print(str(e))
            print("You guys are hopeless. Better do something quick. (ClientException)\n")
        except prawcore.exceptions.Forbidden as e:
            print(str(e))
            print("Very well. Time Leap Machine it is. (Forbidden)\n")



#    if re.search("El Psy Cong", comment.body, re.IGNORECASE):
#        print("FOUND: " + str(comment.body))
#        print("Author: " + str(comment.author))
#        print("\n")


#for submission in subreddit.new(limit=5):
#    print("Title: ", submission.title)
#    print("ID: ", submission.id)
#    print("---------------------------------\n")