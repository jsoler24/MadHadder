import discord
import random
import time
from discord.ext.commands import Bot

BOT_PREFIX = ("-","?","!")
token = 'NTU3Mzk0MDgwMzM4ODA0NzU2.D3HrsA.b9330LT-ET1L5fZCc38M4B3-qwg'
client = Bot(command_prefix=BOT_PREFIX)

@client.command(name = 'change_places',
                aliases = ['changeplaces','Changeplaces', 'CHANGEPLACES'],
                description = "Changes all of the users places in the channel")
async def change_places():

    # set the intial variables
    members_in_channels, channels_list = getMembersAndChannels()
    
    # make random number to choose a member
    randMembersIndex = random.randrange(0,len(members_in_channels))

    #set target member and print to the console
    target_member = members_in_channels[randMembersIndex]
    print("The target:")
    print(target_member)
    
    # while loop to send target to different channels
    i = 0
    while i < 13:
        
        # get random index based on how many channels
        randChannelIndex = random.randrange(0,len(channels_list))
        
        # get the target channel based on the random number
        target_channel = channels_list[randChannelIndex]

        # Debuggin
        print(randChannelIndex)
        print(target_channel)

        await client.move_member(target_member, target_channel)

        print("Counter: " + str(i))
        print(str(target_member) + " moved to channel " + str(target_channel)+ " with index " + str(randChannelIndex))

        time.sleep(1)
        i += 1
       
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


def getMembersAndChannels():
    # get all of the members and channels on the server
    channels = client.get_all_channels()
    members = client.get_all_members()
    #initailze empty lists to append too
    channels_list = []
    members_list = []
    current_members_in_channel = []
   
    for member in members:
        members_list.append(member)
    
    for channel in channels:
        #ignore chat with the channel names of certain channels
        if str(channel) == 'booth' or str(channel) == 'AFK' or str(channel) == 'nerds': 
            continue
        else:
            channels_list.append(channel)

    for member in members_list:
            # Filter out members that are offline - part of 'None' channels
            if member.voice_channel != None:
                # Append a member to the list if the are part of a channel
                current_members_in_channel.append(member)


    return current_members_in_channel, channels_list

client.run(token)
