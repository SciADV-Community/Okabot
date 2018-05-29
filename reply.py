from postDB import queryDB, appendDB
import random


footer = ("\n\n***\n\n"
          "^[Why?](https://github.com/Zorpos/Okabot/blob/master/README.md) ^| [^More ^Info](https://github.com/Zorpos/Okabot) ^|"
          " ^[Creator](http://futuregadget-lab.us/) ^|"
          " ^[Contact](https://np.reddit.com/message/compose/?to=zaros104&subject=Okabot%20Feedback)"
)

def congroo_reply(comment, correction, arg):
    if not (("cong" in str(comment).lower()) and("kong" in str(comment).lower())):
        response = random.randint(1, 3)

        if (arg.group(1) == 'roo' or response == 1):
            comment.reply("*It's " + correction + "*." + footer)
        elif response == 2:
            comment.reply("It's *" + correction + "*! Don't forget it." + footer)
        elif response == 3:
            comment.reply("No! Not *Cong" + arg.group(1) + "*! *" + correction + "*!" + footer)

        appendDB(comment.submission, comment.id)
        print("Replied to:" + comment.id + "\n")


def tutturu_reply(comment):
    response = random.randint(1, 3)

    if response == 1:
        comment.reply("It maybe this worldline, but that doesn't sound totally right... \n\n"
                                    "I believe the utterance is *\"Tutturu\"*, is it not?" + footer)
    elif response == 2:
        comment.reply("While I'm not sure where it came from or what it means, *\"tutturu\"* "
                                    "is definitely her catchphrase." + footer)
    elif response == 3:
        comment.reply("*Tutturu* to you too." + footer)

    appendDB(comment.submission, comment.id)
    print("Replied to:" + comment.id + "\n")


def luka_reply(comment):
    response = random.randint(1, 3)

    if response == 1:
        comment.reply("I do believe you're referring to lab mem 006, Urushibara Luka.\n\n"
                                    "Still a dude... I think." + footer)
    elif response == 2:
        comment.reply("*Luka* is the epitome of 'Someone this cute can't be a girl'." + footer)
    elif response == 3:
        comment.reply("*Urushibara Luka.* \n\n "
                                    "A stunning example of feminine charm and grace. \n\n"
                                    "Lips delicate like cherry blossoms in bloom.\n\n"
                                    "The essence of Japanese beauty.\n\n"
                                    "The chief priest's son.\n\n That's right, \"son\"." + footer)

    appendDB(comment.submission, comment.id)
    print("Replied to:" + comment.id + "\n")


def nullpo_reply(comment):
    comment.reply("[Gah!](https://i.imgur.com/3jJWARm.png)" + footer)
    appendDB(comment.submission, comment.id)
    print("Replied to:" + comment.id + "\n")