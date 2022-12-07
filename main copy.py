from telebot.async_telebot import AsyncTeleBot 
import pytube
import time
import asyncio

mychat_id=0

# pytube was updated with the following: "https://github.com/pishiko/pytube/tree/fix-channel"
# otherwise the url won't be accepted (and still it does not allow for original youtube urls;
# use the scheme as follows)

# Cheking if there are any new videos on @Avoidingthepuddle channel on youtube
c = pytube.Channel("https://www.youtube.com/user/AvoidingthePuddle")
latest_video_url = c.video_urls[:1][0]
print (latest_video_url)

# check if the current video is the latest video
# add the information about the latest video to the txt file
def new_video_check(link):
    with open("latest_video.txt", "r+") as f:
        if link == f.read():
            print ("There are no new videos")
            return False
        else:
            print ("New video found")
            f.write(link)
            print ("Link updated")
            return True


#let's create how bot will send a message

def send_message (mybot, mymessage):
    @bot.message_handler(commands=["status", "start"])
    async def send_status(message):
        global mychat_id

        with open ("users.txt", "r") as f:
            print (f.read())
            print (str(message.chat.id))
            # if str(message.chat.id) not in str(f.read()):
            #     with open ("users.txt", "a") as file:  
            #         file.write(str(message.chat.id)+", ")
        await mybot.send_message(message.chat.id, "The bot is alive! Here's the latest video from Aris:\n{}".format(mymessage))

    asyncio.run(mybot.polling())





# Let's start working with PyTelegramBotAPI

token = "5863245528:AAEM8_Qvdz3-YpWH8tWGFDbRJ02tCvyKFMY"
bot = AsyncTeleBot(token)

send_message(bot, latest_video_url)


def the_task():
    if new_video_check(latest_video_url):
        with open ("users.txt", "r") as f:
            list_of_users = f.read().split(", ")[:-1]
            print (list_of_users)
        for user_id in list_of_users:
            print ("IS THIS EEVEN WORKIN?")
            bot.send_message(int(user_id), "NEW VIDEO:\n{}".format(latest_video_url))
    asyncio.sleep(3000)

asincio.run(the_task())








asyncio.run(mybot.polling())