from postDB import queryDB, appendDB
from logger import logger
import urllib.request, urllib.error
import random
import os


# El Psy Kongroo, Hououin Kyouma, Tutturu, Luka
path = "./db/"
respfile = ["EPK.txt", "KYO.txt", "TTR.txt", "LKO.txt", "UPA.txt", "SG.txt"]
respdata = []
baseurl = "https://raw.githubusercontent.com/Zorpos/Okabot/master/db/"

footer = ("\n\n***\n\n"
          "^[Why?](https://github.com/Zorpos/Okabot/blob/master/README.md) ^| [^More ^Info](https://github.com/Zorpos/Okabot) ^|"
          " ^[Creator](http://futuregadget-lab.us/) ^|"
          " ^[Contact](https://np.reddit.com/message/compose/?to=zaros104&subject=Okabot%20Feedback)"
)

def response_load():
    # Verify files exist
    for i in respfile:
        if not (os.path.isfile(path + i)):
            try:
                logger.warning("Missing file " + i + " , Downloading from repo.")
                urllib.request.urlretrieve(baseurl + i, path + i)
            except urllib.error.HTTPError as e:
                logger.critical("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                logger.critical(e)
                logger.critical(baseurl + i)
                logger.critical("Resolve networking or create file. ")
                logger.critical("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                quit(1)

    # Load files to memory
    index = 0
    for i in respfile:

        resparray = []
        for line in open(path + respfile[index]):
            # Quick and dirty fix for having newlines in quote files
            line = line.strip('\n')
            line = line.replace('\\n','\n')
            resparray.append(line)

        respdata.append(resparray)
        index += 1


def congroo_reply(comment, correction, arg):
    if not (("cong" in str(comment).lower()) and("kong" in str(comment).lower())):
        # 0 & -1 because Python can't index
        respnum = random.randint(0, len(respdata[0]) - 1)

        response = respdata[0][respnum]

        try:
            if "%correction%" in response:
                response = response.replace("%correction%", correction)
            if "%arg1%" in response:
                response = response.replace("%arg1%", arg)
        except TypeError as e:
            logger.error(response)
            logger.error("Correction: " + correction + " | " + "Arg: " + arg)
            logger.error("---------------------------------------------")
            logger.error(str(e))
            logger.error("---------------------------------------------")


        #print(response + footer)
        comment.reply(response + footer)
        appendDB(comment.submission, comment.id)
        logger.info("Replied to:" + comment.id + "\n")


def kyouma_reply(comment):
    respnum = random.randint(0, len(respdata[1]) - 1)
    response = respdata[1][respnum]

    #print(response + footer)
    comment.reply(response + footer)
    appendDB(comment.submission, comment.id)
    logger.info("Replied to:" + comment.id + "\n")


def tutturu_reply(comment):
    respnum = random.randint(0, len(respdata[2]) - 1)
    response = respdata[2][respnum]

    #print(response + footer)
    comment.reply(response + footer)
    appendDB(comment.submission, comment.id)
    logger.info("Replied to:" + comment.id + "\n")


def luka_reply(comment):
    respnum = random.randint(0, len(respdata[3]) - 1)
    response = respdata[3][respnum]

    #print(response + footer)
    comment.reply(str(response) + footer)
    appendDB(comment.submission, comment.id)
    logger.info("Replied to:" + comment.id + "\n")


def upa_reply(comment):
    respnum = random.randint(0, len(respdata[4]) - 1)
    response = respdata[4][respnum]

    #print(response + footer)
    comment.reply(response + footer)
    appendDB(comment.submission, comment.id)
    logger.info("Replied to:" + comment.id + "\n")


def stein_reply(comment):
    respnum = random.randint(0, len(respdata[4]) - 1)
    response = respdata[5][respnum]

    #print(response + footer)
    comment.reply(response + footer)
    appendDB(comment.submission, comment.id)
    logger.info("Replied to:" + comment.id + "\n")


def nullpo_reply(comment):
    comment.reply("[Gah!](https://i.imgur.com/3jJWARm.png)" + footer)
    appendDB(comment.submission, comment.id)
    logger.info("Replied to:" + comment.id + "\n")
