import asyncio
import websockets

# async def handler(connection):
#     while True:
#         message = await connection.recv()
#         print(message)

async def handler(connection):
    # Server function that listens for clients connecting to this ws server.
    message = await connection.recv()
    print(message)

    # Send message back to all clients connected to
    # the server
    await connection.send(message)

async def main():
    # localhost
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
