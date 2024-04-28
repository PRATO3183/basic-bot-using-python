import discord
import random
import requests

intents =  discord.Intents.all()
client = discord.Client(intents=intents)

# Dictionary of country flags and their corresponding country names
FLAGS = {
    "https://flagcdn.com/w640/gb.png": "United Kingdom",
    "https://flagcdn.com/w640/us.png": "United States",
    "https://flagcdn.com/w640/ca.png": "Canada",
    "https://flagcdn.com/w640/au.png": "Australia",
    "https://flagcdn.com/w640/de.png": "Germany",
    "https://flagcdn.com/w640/fr.png": "France",
    "https://flagcdn.com/w640/jp.png": "Japan",
    "https://flagcdn.com/w640/cn.png": "China",
    "https://flagcdn.com/w640/br.png": "Brazil",
    "https://flagcdn.com/w640/in.png": "India"
}

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print("new message",message.content)
    
    if "image" in message.content: 
        response = requests.get('https://source.unsplash.com/random')
        image_url = response.url
        await message.channel.send(image_url)
    
    elif "hi" in message.content:
        await message.channel.send("Hello User")
    
    elif "bye" in message.content:
        await message.channel.send("Bye User")
    
    elif "rick" in message.content:
        response=requests.get("https://media.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif")
        image_url = response.url
        await message.channel.send(image_url)
    elif "nigga" in message.content:
        response=requests.get("https://cdn.discordapp.com/avatars/566312646362529803/5a17b233e6c06d4f5470adebd2be456f.png?size=4096")
        image_url=response.url
        await message.channel.send(image_url)
    elif "flag" in message.content:
        # Choose a random flag URL from the dictionary
        flag_url = random.choice(list(FLAGS.keys()))
        # Send the flag image to the channel
        await message.channel.send(flag_url)
        # Wait for a message from the user
        response = await client.wait_for('message', check=lambda m: m.author == message.author)
        # Check if the user's response matches the country name
        if response.content.lower() == FLAGS[flag_url].lower():
            await message.channel.send("Good!")
        else:
            await message.channel.send("Sorry, the correct answer was {}.".format(FLAGS[flag_url]))
    
    elif "song" in message.content:
        song_name = message.content[5:]  # Extract the song name from the message
        query = "https://open.spotify.com/search/{}".format(song_name)
        await message.channel.send(query)
    
    else:
        await message.channel.send(message.content)

client.run('MTA4ODUzNDIxMjk0MTk4Mzg0NA.GEWwE6.-G_Kkbi2onSHu7kiGlteeL86-HRuaGtwvlouu8')
