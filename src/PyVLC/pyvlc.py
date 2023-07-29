import telnetlib3
import asyncio
from getpass import getpass

class pyvlc:
    def __init__(self, host="localhost", port=4212):
        self.host = host
        self.port = port
        self.buffer = ""

    async def connect(self):
        try:
            self.reader, self.writer = await telnetlib3.open_connection(self.host, self.port)
        except ConnectionRefusedError as CRE:
            print("Failed to connect. Most likely VLC is not running. If VLC is running then verify the host and port. Also check the telnet interface is enabled as a main interface in VLC.")
            return CRE
        print(await self.reader.readuntil(b"Password:"))
        self.writer.write(getpass("Password: ") + "\n")
        await self.reader.readuntil(b">")
    
    async def send(self, command: str):
        if self.writer:
            self.writer.write(command + "\n")
            try:
                self.buffer = await self.reader.readuntil(b">")
            except asyncio.IncompleteReadError as IRE:
                self.buffer = IRE.partial
            self.buffer = str(self.buffer.decode("utf-8"))
        else:
            print("No writer object available. Run connect() method then try again.")
    
    async def disconnect(self):
        if self.writer:
            self.writer.write("quit\n")
            print(await (self.reader.readuntil()))
            self.writer.close()
            print("Disconnected from VLC")
    
    async def shutdown(self):
        if self.writer:
            self.writer.write("shutdown\n")
            try:
                print(await (self.reader.readuntil(b"Shutting down.")))
            except asyncio.IncompleteReadError as IRE:
                print(IRE.partial)
            finally:
                self.writer.close()
        else:
            print("No writer attached")
    
    async def is_alive(self):
        if self.writer.is_closing():
            return False
        else:
            return True
    
    async def list_commands(self):
        if self.writer:
            self.writer.write("help\n")
            try:
                self.buffer = await self.reader.readuntil(b">")
            except asyncio.IncompleteReadError as IRE:
                self.buffer = IRE.partial
            finally:
                self.buffer = str(self.buffer.decode("utf-8"))
                print(self.buffer)
    
