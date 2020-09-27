#!/usr/bin/python3.6
''' pubg report bot'''

import discord, logging
from bot.main import client as client
logging.basicConfig(level=logging.DEBUG)

# Create an API key here: https://discordapp.com/developers/applications/
# Create a webhook in the channel settings of your discord server
bot_token = 'Njg1MTY4MDYyMjQ0NDU0NDA3.XmEuew.0a0c_FHIJrdFWkGk69q8Q9rAnD4' # Bot token (discordapi)
webhook_uri = 'https://discordapp.com/api/webhooks/701388849749819473/UXjLy30FXS0hsWYF3tSuZu_i3mCRs1ZYrLQFMOUHttqnichCpPYjKRnEZaErvAwBfP0_' #Webhook URL (discord client)

check_rate = 15  # How often the bot will check for updates, in minutes (no less than five minutes or you'll be banned from pubg.report)
if __name__ == "__main__":
    client.run(bot_token)
