import yaml
from discord.ext import commands


config = yaml.safe_load(open('config.yaml'))
bot = commands.Bot(command_prefix=commands.when_mentioned_or(config['prefix']), description='Essential Bot - Type $essential')
bot.remove_command("help")


@bot.event
async def on_ready():
    print('Essential Bot Turning On')
    print('------------')
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('Using prefix:')
    print(config['prefix'])
    print('------------')
    bot.load_extension("code")
    await bot.change_presence(status='Amds Test Bot')

async def test(coro):
    print('yeet')

bot.run(config['token'])
