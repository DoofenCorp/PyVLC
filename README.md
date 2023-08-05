# API is under constant development for adding/improvising further features and improvements

Current API Version: 1.0.1 [PyPI](https://pypi.org/project/PyVLC/)

Current API functions:

* `connect()`: Starts the connection to VLC on specified host and port 
* `send(command)`: Sends command to VLC
* `disconnect()`: Disconnects from VLC
* `shutdown()`: Ends the connection and shuts down VLC
* `is_alive()`: Returns True if the connection is alive else False

# USAGE:

## Either: `pip install PyVLC` or `pip3 install PyVLC`
## Or: Download the latest release zip/tar.gz

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