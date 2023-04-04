import asyncio
import websockets
import json


port = 8123
connected_paths = dict()

paths = ["/", "/test", "/battery"]


def setup_paths():
    for path in paths:
        connected_paths[path] = set()


async def send_to_connections(connections, websocket, message):
    # This is just an example
    a = {
         "eins": 22,
         "zwei": "value"
    }
    a = json.dumps(a)
    # Send a response to all connected clients except sender
    for conn in connections:
           if conn != websocket:
               await conn.send(a)


async def handler(message, websocket, connections):
    await send_to_connections(connections, websocket, message)
    return "parsed msg"


async def message_handler(websocket, path):
    connections = connected_paths[path]
    connections.add(websocket)
    try:
        async for msg in websocket:
            parsed_msg = await handler(msg, websocket, connections)
            print("Received message from client: " + parsed_msg +" path: "+ path)

    except websockets.exceptions.ConnectionClosed as e:
        pass

    finally:
        connections.remove(websocket)


async def ws_handler(websocket, path):
    match path:
        case "/battery":
            await message_handler(websocket, path)
        case _:
            print("This path is not defined")


async def main():
    async with websockets.serve(ws_handler, "localhost", port):
        await asyncio.Future()

if __name__ == "__main__":
    setup_paths()
    asyncio.run(main())