# API is under constant development for adding/improvising further features and improvements

Current API Version: 1.0.1 [PyPI](https://pypi.org/project/PyVLC/)

Current API functions:

* `connect()`: Starts the connection to VLC on specified host and port 
* `send(command)`: Sends command to VLC
* `disconnect()`: Disconnects from VLC
* `shutdown()`: Ends the connection and shuts down VLC
* `is_alive()`: Returns True if the connection is alive else False
* `list_commands()`: Lists supported commands that can be executed by VLC

# USAGE:

### 1. Either: `pip install PyVLC` or `pip3 install PyVLC`
### Or: Download the latest release zip/tar.gz

### 2. Configure VLC Media Player to use telnet as an additional main interface:

* Open VLC Media Player
* Click Tools on Menu Bar
* Click on Preferences
* On the bottom left of popup window, under 'show settings' click on All
* In the left menu expand 'Interfaces' and click on Main Interfaces
* IMPORTANT: In main interfaces, checkmark on 'Telnet'
* Expand 'Main Interfaces' on the left pane and click on 'Lua'
* On the right pane configure 'Lua Telnet'
    * Lua Interface: `dummy`
    * Host: `localhost` or `127.0.0.1` for same computer or set remote IP
    * Port: `4212` is default, you can leave it as is or configure any other port if required
    * Password: Set your password
* Click on Save

### 3. Run VLC and Import the library in Python

```python3
from PyVLC.PyVLC import PyVLC 
```
The library works asynchronously hence you will need to explicitly import `asyncio` (`import asyncio`) for asynchronous functioning and call the object functions with async/await syntax.

Example:

```Python3
from PyVLC.PyVLC import PyVLC
import asyncio

VLC = PyVLC()
async def runner():
    await VLC.connect()
    while True:
        com = input("VLC> ")
        if com == "quit" or com == "exit":
            await VLC.disconnect()
            break
        await VLC.send(com)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(runner())
```

# LICENSING:

This project is distributed under the MIT License. See [LICENSE](/LICENSE) for details.