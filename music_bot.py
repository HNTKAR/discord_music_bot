import discord

client = discord.Client()

players = {}

@client.event
async def on_ready():
    print(client.user.name)

@client.event
async def on_message(message):

    if message.content.startswith('.play'):
        try:
            channel = message.auhor.voice.voice_channel
            voice = await client.join_voice_channel(channel)
            player = voice.create_ffmpeg_player('Sounds\h.mp3')
            player.start()
        except Exception as exc:
            await client.send_message(message.channel, "Es ist ein Fehler aufgetreten. ```{ttt}```".format(ttt=exc))
        voice_client = client.voice_client_in(message.server)
        await voice_client.disconnect()

client.run('xxx')