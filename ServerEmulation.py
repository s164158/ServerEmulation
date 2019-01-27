import socket
import threading
from random import randint


##TEST ARRAYS ###
modarray = ["{MOD:0}","{MOD:1}","{MOD:2}"]
fpsarray = ["{FPS:10}","{FPS:25}","{FPS         :60}"]
vclarray = ["{VCL:1}","{VCL:25}","{VCL:100}"]
resarray = ["{RES:144}","{RES:480}","{RES:1080}"]
errarray = ["{ERR:10}","{ERR:25}","{ERR:1}"]
berarray = ["{BER:15}","{BER:17}","{BER:99}"]
syncarray = ["{SYN:NO}","{SYN:YES}"]
utilarray = ["{UTI:10}","{UTI:20}","{UTI:55}"]
####
class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60) #remember the client for 60 seconds - if not, forget it.
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:

                data = client.recv(size)
                #print(data)
                randomval = randint(0,2)
                randomval2 = randint(0,1)
                x = "fuckdig}"

                if data:
                    # Set the response to echo back the recieved data
                    response = data
                    #client.send(response)
                    #USE THE COE ABOVE TO ECHO BACK RESPONSE...
                    #print(response)
                    response = response.decode('ascii')
                    response = response.strip()
                    print(response)

                    if response == "{REQ:MOD}":
                        testmsg = modarray[randomval]  # we pick a random value and then send it through the system
                        client.send(testmsg.encode('ascii'))
                    elif response == "{REQ:FPS}":
                        testmsg = fpsarray[randomval]  # same thing
                        client.send(testmsg.encode('ascii'))

                    elif response == "{REQ:VCL}":
                        testmsg = vclarray[randomval]  # same thing
                        client.send(testmsg.encode('ascii'))

                    elif response == "{REQ:RES}":
                        testmsg = resarray[randomval]  # same thing
                        client.send(testmsg.encode('ascii'))

                    elif response == "{REQ:ERR}":
                        testmsg = errarray[randomval]  # same thing
                        client.send(testmsg.encode('ascii'))

                    elif response == "{REQ:BER}":
                        testmsg = berarray[randomval]  # same thing
                        client.send(testmsg.encode('ascii'))

                    elif response == "{REQ:SYN}":
                        testmsg = syncarray[randomval2]  # same thing
                        client.send(testmsg.encode('ascii'))

                    elif response == "{REQ:UTI}":
                        testmsg = utilarray[randomval]  # same thing
                        client.send(testmsg.encode('ascii'))

                    #else:
                     #   print("INVALID INPUT")
                      #  testmsg = "INVALID INPUT"
                       # client.send(testmsg.encode('ascii'))

                else:
                    print("Failed")

            except:
                client.close()
                return False

if __name__ == "__main__":
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()
