import asyncio
import websockets
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import configloader.config as cnf


connected_paths = dict()
paths = list()

def setup_paths():
    for path in paths:
        connected_paths[path] = set()
    
def convert_topic_to_ws_path(topics):
    for topic in topics:
        paths.append(f"/{topic}")

async def send_to_connections(connections, websocket, message):
    # Send a response to all connected clients except sender
    for conn in connections:
           if conn != websocket:
               await conn.send(message)


async def message_handler(websocket, path):
    connections = connected_paths[path]
    connections.add(websocket)
    try:
        async for msg in websocket:
            await send_to_connections(connections, websocket, msg)

    except websockets.exceptions.ConnectionClosed as e:
        pass

    finally:
        connections.remove(websocket)


async def ws_handler(websocket, path):
    if path in paths:
        await message_handler(websocket, path)
    else:
        print(f"The path: {path} is not defined")
        


async def main(port):
    async with websockets.serve(ws_handler, "localhost", port):
        await asyncio.Future()

def start_ws():
    port = 8123
    topics = cnf.getWsConfig()
    convert_topic_to_ws_path(topics)
    setup_paths()
    asyncio.run(main(port))


# if __name__ == "__main__":
#     port = 8123
#     topics = cnf.getWsConfig()
#     convert_topic_to_ws_path(topics)
#     setup_paths()
#     asyncio.run(main(port))