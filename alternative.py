from telebot.async_telebot import AsyncTeleBot
import asyncio

token = "5863245528:AAEM8_Qvdz3-YpWH8tWGFDbRJ02tCvyKFMY"
bot = AsyncTeleBot(token)
myuserid=""

with open ("users.txt", "r") as file:
    myuserid=file.read()[:9]

@bot.message_handler(commands=["status", "start"])
async def send_status(message):
    await bot.send_message(message.chat.id, "The bot is alive! Here's the latest video from Aris")
# asyncio.run(bot.polling())

async def sendmessage():
    global myuserid
    task = asyncio.create_task(sendanothermessage())
    task2 = asyncio.create_task(mypolling())
    while True:
        await bot.send_message (myuserid, "hello!")
        await asyncio.sleep(1)

async def sendanothermessage():
    global myuserid
    while True:
        await bot.send_message(myuserid, "goodby")
        await asyncio.sleep(4)

async def mypolling():
    await bot.polling()

asyncio.run(sendmessage())


