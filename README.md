# ServerStart
Discord bot integrated with a Minecraft Server

NOTICE: Only works on Linux Operating Systems at the moment. As of now there are no plans to port over to Windows or Mac

There are plans for the server.py file to eventually be its own library, but at the moment it is to stay with the discord bot.

This is meant to run on PRIVATE discord servers, as everyone in the server has access to all the commands.
In future updates there will be permission requirements, but at the moment there are not.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Directions to running the bot:

1. clone the repository -> git clone ...

2. Make sure to have these additional python libraries installed "discord.py", "mcrcon"

3. Make the 'startbot.sh', 'serverStat.py', and 'killbot.sh' files executable
    - Use the chmod +x {file(s)} command if needed

4. Get a discord bot key and create a file in the same directory called "discord.key"

5. Modify to the 'launchOptions.json' file to point to the correct directories and executables
    - See below for information on each object

6. Execute the startbot.sh script -> ./startbot.sh

~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Directions for the 'launchOptions.json' file:

JAVA_LOCATION: 
The Java Location is the java JVM executable that will be used to launch the minecraft server jar.
 - In the example below I am using Java 8.
 - Also do not add a '/' at the end as the end of the location should be the executable itself

SERVER_DIRECTORY:
The location of the server.jar file, should also have the log files and backups if you have that setup.
 - Make sure there is a '/' at the end as it should point to the folders that are inside

JAR_FILE:
The server.jar executable.
 - What will be run in order to start the server.

MIN_RAM:
The minimum amount of RAM the server will use.
 - Can either be in 'M' as "1024M" or 'G' as "1G"

MAX_RAM:
The maximum amount of RAM the server will use.
 - Can either be in 'M' as "1024M" or 'G' as "1G"

JAVA_PARAMETERS:
Extra parameters that will be added at the server's runtime.

Example: 
{
    
    "MIN_RAM": "1024M",
    "MAX_RAM": "8192M",
    "JAVA_PARAMETERS": "-XX:+UseG1GC -Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+UnlockExperimentalVMOptions -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M -Dfml.readTimeout=180",
    "JAVA_LOCATION": "/usr/lib/jvm/oracle-java8-jre-amd64/bin/java",
    "SERVER_DIRECTORY": "/home/{user}/Documents/Servers/SevTech/",
    "JAR_FILE": "forge-1.12.2-14.23.5.2860.jar"

}