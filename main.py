from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message
from config import *





bot = Client('myacc' , api_id=api_id , api_hash=api_hash)


@bot.on_message(filters.private | filters.photo)
async def saveImage(client:Client , message:Message):
    if(message.photo.ttl_seconds):
        await client.send_photo("me" , message.photo.file_id)

@bot.on_message(filters.private | filters.photo)
async def saveVideo(client:Client , message:Message):
    if(message.video.ttl_seconds):
        await client.send_video("me" , message.photo.file_id)
    




bot.run()
