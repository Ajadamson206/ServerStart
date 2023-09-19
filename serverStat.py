import discord
import os.path
import server


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        print('------------')

    async def on_message(self, message):
        if message.author == self.user:
            return

        userCommand = message.content.split(" ")

        async def logs():
            # Number of lines read from the bottom ()
            try:
                N = int((message.content.strip())[5:])
            except:
                await message.channel.send("Unable to determine number of lines; command - !logs [# of lines]\nExample: !logs 5")
                return

            # Prevent the character limit
            if (N >= 50 | N < 0):
                await message.channel.send("Range error: Please select a smaller range")
                return
            
            logMessage = "Current Logs: \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

            # Read from the log file
            with open(server.directory + "logs/latest.log", "r") as logFile:
                for line in (logFile.readlines() [-N:]):
                    logMessage += line
            await message.channel.send(logMessage)


        async def serverStart():
            if server.serverStatus():
                await message.channel.send("Server is already running")
                return
            server.startServer()
            
        async def input():
            server.serverInput(message.content)
            


        async def status():
            await message.channel.send(f"Server Running - {server.serverStatus()}")


        async def help():
        # Send a mesage with a list of the commands
            await message.channel.send("""
List of commands....

- !help
Displays this list of commands

- !status
Shows the current status of the Minecraft Server

- !serverStart
Start up the Minecraft Server

- !logs [# of lines from 0 to 50]
Read the most recent logs of the minecraft server
""")

        commands = {
            "!logs": logs,
            "!serverStart": serverStart,
            "!input": input,
            "!status": status,
            "!help": help
        }

        if userCommand[0] in commands: await commands[userCommand[0]]()
        



intents = discord.Intents.default()
intents.message_content = True

# Open file where the client key is stored
with open("discord.key", "r") as keyFile:
    key = keyFile.read()

client = MyClient(intents=intents)
client.run(key)
