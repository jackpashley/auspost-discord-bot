"""app.py: Runpoint for the application. This is where the bot is started."""

__author__      = "Jack Pashley"

import discord
from parcel_tracker import parcel_check

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(message.content)
        if message.content.startswith("~parcelstatus"):
            parcel_id = message.content.split(" ")[1]
            response = parcel_check(parcel_id)
            await message.channel.send(f"""At {response['localeDateTime']}, your item was registered as being "{response['description'].strip()}"
            """)

intents = discord.Intents.default()
intents.message_content = True

# In discord developer portal, enable Message Content Intent under BOT -> Privileged Gateway Intents
# And in Oauth2, enable Bot/Send Messages, Bot/Read Message History

client = MyClient(intents=intents)
client.run('YOUR_TOKEN_HERE')