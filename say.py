import disnake
from disnake.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(name='saye', aliases=['echo'])
    async def saye(self, ctx, *, arg=None):
        if arg is None:
            embed = disnake.Embed(title="Ошибка", description="Недостаточно аргументов", color=0x2b2d31) 
            await ctx.reply(embed=embed)
        else:
            embed = disnake.Embed(description=arg, color=0x2b2d31)
            await ctx.send(embed=embed)
            await ctx.message.delete()



    @commands.has_permissions(administrator=True)
    @commands.command(description="Отправить сообщение от имени бота.")
    async def say(self, ctx, *, message):
        if message is None:
            embed = disnake.Embed(title="Ошибка", description="Недостаточно аргументов", color=0x2b2d31) 
            await ctx.send(embed=embed)
        else:
            await ctx.send(message)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(Say(bot))