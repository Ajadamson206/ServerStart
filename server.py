import subprocess

#directory = "/home/albert/Documents/Servers/SevTech/"
# For debug testing purposes only
directory = "/home/albert/Documents/Coding/serverStart/"

# Returns True if the process is running (Unix Only)
def serverStatus():
   # with open(directory + "serverpid.txt", "r") as serverPIDfile:
   #     PID = (serverPIDfile.read()).strip()
   # return (os.path.exists(f"/proc/{PID}"))
   return False

def startServer():
    # subprocess.run(directory + "ServerStart.sh")
    global server
    # server = subprocess.Popen([f"{directory}ServerStart.sh", ""], stdin=subprocess.PIPE)
    server = subprocess.Popen(["java", "-server", "-Xms1024M", "Xmx4096", "-jar", f"{directory}server.jar", "nogui"], stdin=subprocess.PIPE)



def serverInput(command):
    server.stdin.write(command.encode())


def serverClose():
    server.stdin.write("close".encode())