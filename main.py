from youtube_dl import YoutubeDL
from config import token
#from pypresence import Presence
YDL_OPTIONS = {'noplaylist':'False'}#{'format': 'bestaudio', 'noplaylist':'False'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
import discord, asyncio, time, datetime
from discord.ext import commands
from discord.utils import get
Client = discord.Client()
client = commands.Bot(command_prefix = '!')
client.remove_command('help')
'''RPC = Presence("APP_ID")
btns = [
    {
        "label": "VK",
        "url": "https://vk.com/timtaran_yt"
    }
]
RPC.connect()
RPC.update(
    state="Радио бот",
    details="дя",
    start=time.time(),
    buttons=btns,
    large_image="spotify",
    small_image="MC",
    large_text="TSB",
    small_text="TimtaranServerBot"
)'''
class j:
	def __init__(self):
		self.joined = True
J=j()

@client.event
async def on_ready():
	print('Bot Working')
@client.event
async def on_message(ctx, *args):
	print(ctx)
	if ctx.channel.id==832597151698649089:
		channel = client.get_channel(832889985035665438)
		if channel:
			await channel.send(f'{ctx.author.name}#MC>> {ctx.content}')
	elif ctx.channel.id==832797467317370910:
		channel = client.get_channel(832889985035665438)
		if channel:
			await channel.send(f'{ctx.author.name}#{ctx.author.discriminator}>> {ctx.content}')

@client.command(name='info', invoke_without_subcommand=True)
async def info(ctx, *args):
	if ctx.message.channel.id == 832834416903716894:
		embed = discord.Embed(
			title='Обо мне.',
			description='Я радио и майнкрафт бот.',
			colour=discord.Color.green(),
			timestamp=datetime.datetime.now()

		).add_field(
			name='Радио бот',
			value='Воспроизводит музыку со стримов и видео, управляется Timtaran - https://vk.com/timtaran_yt',
			inline=True

		).add_field(
			name='Майнкрафт бот',
			value='Читает сообщения с канала "to-mc" и отправляет их на сервер, а вебхук их присылает сюда.',
			inline=True).set_footer(
        text='Исходный код бота - https://github.com/Timtaran/musicbot',)


		await ctx.send(embed=embed)

@client.command(name='join', invoke_without_subcommand=True)
async def join(ctx):
	destination = ctx.author.voice.channel
	voice_state = await destination.connect()
	await ctx.send(f"Joined {ctx.author.voice.channel} Voice Channel")

@client.command(name='play', invoke_without_subcommand=True)
async def play(ctx, *args):
	'''
	with YoutubeDL(YDL_OPTIONS) as ydl:
		info = ydl.extract_info(open('music_url.txt', 'r').read(), download=False)
	URL = info['formats'][0]['url']
	voice = get(client.voice_clients, guild=ctx.guild)
	voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=URL, **FFMPEG_OPTIONS))
	'''
	if ctx.message.author.id == 440408198168576001:
		if J.joined:
			destination = ctx.author.voice.channel
			voice_state = await destination.connect()
			await ctx.send(f"Joined {ctx.author.voice.channel} Voice Channel")
			J.joined=False
		else:
			voice = get(client.voice_clients, guild=ctx.guild)
			destination = ctx.author.voice.channel
			await voice.disconnect()
			voice = await destination.connect()
		with YoutubeDL(YDL_OPTIONS) as ydl:
			song_info = ydl.extract_info(args[0], download=False)
			voice = get(client.voice_clients, guild=ctx.guild)
			#voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=song_info["formats"][0]["url"]))
			voice.play(
				discord.FFmpegPCMAudio(source=song_info["formats"][0]["url"]))
			#ctx.guild.voice_client.play(discord.FFmpegPCMAudio(song_info["formats"][0]["url"]))
			voice.source = discord.PCMVolumeTransformer(voice.source)
			try:
				voice.source.volume = float(args[1])
			except:
				voice.source.volume = 0.3
			title = song_info['title']
			await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=title))
			await ctx.send(f'Playing {title}')

'''@client.command(name='leave', invoke_without_subcommand=True)
async def leave(ctx):
	print(ctx.message)
	channel=ctx.message.author.voice.channel
	destination = ctx.author.voice.channel
	voice = get(client.voice_clients, guild=ctx.guild)
	if voice and voice.is_connected():
		if ctx.message.guild.name=='life simulator [BetaServer]':
			if ctx.message.author.id == 440408198168576001:
				await voice.disconnect()
				voice = await destination.connect()
		else:
			await voice.disconnect()
		await ctx.send(f"Leaved {ctx.author.voice.channel} Voice Channel")
	else:
		voice = await destination.connect()
		await ctx.send(f"Joined {ctx.author.voice.channel} Voice Channel")'''
@client.command(name='stop', invoke_without_subcommand=True)
async def stop(ctx):
	if ctx.message.author.id == 440408198168576001:
		voice = get(client.voice_clients, guild=ctx.guild)
		destination = ctx.author.voice.channel
		await voice.disconnect()
		voice = await destination.connect()
		J.joined=False

client.run(token)