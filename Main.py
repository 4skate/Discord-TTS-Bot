import discord
from discord.ext import commands
from discord import app_commands


'''
Documentation:

Different functions for various actions
- on_ready
- on_message(message)
- on_message_edit(before, after)
- on_message_delete(message)
- on_member_join(member)
- on_member_remove(member)
- on_member_update(before, after)
- on_guild_join(guild)
- on_guild_remove(guild)
- on_reaction_add(reaction, user)
- on_reaction_remove(reaction, user)
- on_raw_message_delete(payload)
- on_command_error(ctx,error)
'''
class Client(commands.Bot):
    
    # when the code is ran and the bot is logged on, then this function will run
    async def on_ready(self):
        # in this case, it takes the name of the bot, and reports to the terminal that we are indeed logged on
        print(f'Logged on as {self.user}!')

        try:
            # syncing the server for commands to discord, printing confirmation to the terminal
            #REMINDER
            guild = discord.Object(id=)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f'Error syincing commands: {e}')

    async def on_message(self, message):
        # prevents the bot from responding to itself, if the message is from itself then it returns rather than running the code
        if message.author == self.user:
            return
        # if the message starts with "hello", then the bot will say hello, author name
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')
    
    async def on_reaction_add(self,reaction,user):
        await reaction.message.channel.send('you reacted')

intents = discord.Intents.default()
intents.message_content = True
#Referring to client command and passing through command prefix and intents
client = Client(command_prefix="!", intents=intents)

# setting commands to work specifically for this one server, if not true then the command may take hours to appear globally
#REMINDER
serverId = discord.Object(id=)

#You can set slash command to work in any server or in all servers
#name of command cannot be capital per discord rules
@client.tree.command(name="hello", description="Say hello!", guild=serverId)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")

@client.tree.command(name="printah", description="print whatever u want", guild=serverId)
async def sayHello(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

#REMINDER
client.run('')