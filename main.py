# Importing everything
import nextcord, json
from nextcord import SlashOption
from nextcord.abc import GuildChannel
from datetime import datetime as dt

# The botconfig.json file | Usage: data['...']
with open("./botconfig.json") as cf:
    data = json.load(cf)

# Making the "Bot"
bot = nextcord.Client(description=data['description'])

# Creating the slash command:
@bot.slash_command(
    description="Your first slashcommand!"
)
async def yourfirstslashcommand(
    interac : nextcord.Interaction
):
    # Embed for the message:
    embed = nextcord.Embed(title="Your first slash command!", colour=nextcord.Colour.from_rgb(54, 57, 63))
    embed.set_footer(text="Created by Sem#8249")
    # Sending a message | This is different from ctx.send or ctx.reply and it always replies to a message.
    await interac.response.send_message(embed=embed)

# Run the bot
bot.run(data['token'])