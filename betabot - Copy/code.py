import asyncio
import discord
from discord.ext import commands
from discord.utils import get

# For Reddit downloader
import os
import re
import requests
import praw
import configparser
import concurrent.futures
import argparse

import random
intab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

outab = u'🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿'

class essentialbot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def prune2(self, ctx, arg1='1', arg2='1'):

        amount = 20
        person = None

        if arg2 != '1':
            amount = int(arg2)

        if arg1 != '1':
            person = arg1
            person = person.replace('<', '')
            person = person.replace('>', '')
            person = person.replace('@', '')
            person = person.replace('!', '')
            person = int(person)

            person = get(ctx.guild.members, id=person)
            if person is None:
                amount = int(arg1)




        async for unit in ctx.channel.history(limit=5000):
            if amount > 0:
                if person is None:
                    await unit.delete()
                    amount = amount - 1

                else:
                    if person.id == unit.author.id:
                        await unit.delete()
                        amount = amount - 1

    @commands.command()
    async def text(self, ctx, arg='1'):
        if arg != '1':

            async for each in ctx.channel.history(limit=1, before=ctx.message):
                message = each


            await ctx.message.delete()

            letters = []

            thirdString = ''

            # Original String
            # string = fontlogicnew



            for elem in arg:
                print(str(elem))
                if str(elem) != ' ' and str(elem) not in str(letters):
                    letters.append(elem)
                    letter = elem
                    translation = letter.maketrans(intab, outab, thirdString)
                    letter = letter.translate(translation)
                    await message.add_reaction(letter)


    @commands.command()
    async def reddit(self, ctx, arg='1', arg2='none'):
        if arg != '1':
            await ctx.message.delete()
            message = await ctx.channel.send('Loading...')
            # do the stuff
            random.seed = ctx.message.id
            # await ctx.message.delete()

            options = ['top', 'hot']
            order = random.choice(options)

            if arg2 == 'none':
                limit = random.randint(1, 100)
            else:
                limit = int(arg2)
            sub = arg

            config = configparser.ConfigParser()
            config.read('conf.ini')
            reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],
                                      client_secret=config['REDDIT']['client_secret'],
                                      user_agent='Multithreaded Reddit Image Downloader v2.0 (by u/impshum)')


            # r = requests.get(image['url'])


            name = "name of" + arg
            image = 'None'
            text = ''
            try:
                go = 0
                if order == 'hot':
                    submissions = reddit.subreddit(sub).hot(limit=None)
                elif order == 'top':
                    submissions = reddit.subreddit(sub).top(limit=None)
                # elif self.order == 'new':
                #     submissions = self.reddit.subreddit(self.sub).new(limit=None)

                for submission in submissions:
                    # print(str(submission.title))
                    # print(str(submission.url))
                    # print(str(submission.score))
                    # if not submission.stickied and submission.url.endswith(('jpg', 'jpeg', 'png')):
                    go += 1
                    if go >= limit:
                        if submission.url is not None:
                            image = submission.url

                        if submission.selftext is not None:
                            text = submission.selftext

                        title = submission.title
                        break



            except:
                fug = 1



            if name != 'None' and image != 'None':
                # if text is None or text == '':
                textmax = 1500
                titlemax = 256


                if len(text) >= textmax:
                    textcut = len(text) - textmax
                    text = text[:-textcut]

                if len(title) >= titlemax:
                    titlecut = len(title) - titlemax
                    title = title[:-titlecut]

                embed = discord.Embed(title='', description=text, color=ctx.author.color)

                #  print()
                print('title to set: '+ title)
                print('url is' + submission.permalink)
                embed.set_author(name=title, url='http://reddit.com' + submission.permalink)

                comment = submission.comments[0]
                commenttext = comment.body
                commentauthor = comment.author
                commentscore = comment.score
                commentscore = str(commentscore)


                embed.set_footer(text="/r/" + arg.lower() + ' Score: ' + str(submission.score) + " Comments: " + str(submission.num_comments) + " No." + str(limit) + " Sort:" + order + "\n" + commentscore + ": " + str(commentauthor) + ": " + commenttext, icon_url='https://i.imgur.com/ICgMeIS.png')

                if 'png' in submission.url or 'jpg' in submission.url or 'jpeg' in submission.url:
                    embed.set_image(url=image)

                # if text is not None and text != '':
                #     embed =
                #     embed.add_field(name=".f11", value="", inline=True)



                await message.delete()
                message = await ctx.message.channel.send(embed = embed)
                await message.add_reaction('🗨')
                await message.add_reaction('🔼')
                await message.add_reaction('🔽')



            else:
                await ctx.channel.send("This doesn't appear to be a valid subreddit try $reddit cute")
        else:
            await ctx.channel.send("You must supply a subreddit - Please run the command like $reddit cute")

            @commands.command()
            async def corn(self, ctx, arg=''):
                if arg != '1':
                    await ctx.message.delete()
                    message = await ctx.channel.send('http://experiencecornelius.com/')

def setup(bot):
    bot.add_cog(essentialbot(bot))