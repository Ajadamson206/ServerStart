import subprocess
import os.path
from mcrcon import MCRcon as mc

class Server():
    def __init__(self, DIRECTORY, LOCATION, LAUNCH_PARAMETERS, MIN_RAM, MAX_RAM, JAR_FILE):
        self.directory = DIRECTORY
        self.javaLocation = LOCATION
        self.status = False
        self.mcronStatus = False
        self.parameters = LAUNCH_PARAMETERS
        self.minRam = MIN_RAM
        self.maxRam = MAX_RAM
        self.jarFile = JAR_FILE
    
    def startServer(self):
        if self.status:
            return
        os.chdir(self.directory)
        launch = f"{self.javaLocation} -server -Xms{self.minRam} -Xmx{self.maxRam} {self.parameters} -jar {self.jarFile} nogui java"
        self.server = subprocess.Popen(launch.rsplit(" "))
        self.PID = self.server.pid

        self.status = True
        with open("serverPID.txt", "w") as file:
            file.write(str(self.server.pid))

    def serverInput(self, command):
        if not self.mcronStatus:
            self.mcr = mc('localhost', 'abc')
            self.mcr.connect()
            self.mcronStatus = True
        resp = self.mcr.command(f"/{command}")
        return resp


    def serverClose(self):
        if not self.mcronStatus:
            self.mcr = mc('localhost', 'abc')
            self.mcr.connect()
            self.mcronStatus = True
        self.mcr.command("/close")
        self.mcr.disconnect()
        self.status = False

    def checkStatus(self):
        if not self.status: # if it is false
            try:
                return os.path.exists(f"/proc/{self.PID}")
            except:
                return False

        if self.status and os.path.exists(f"/proc/{self.PID}"):
            return True
            

