import asyncio
import websockets
import sys
import pyperclip
DEFAULT_PORT = 8881

def run_server(port):
    async def handle_message(websocket):
        async for message in websocket:
            # Replace the null character from vim yank with newline
            message = message.strip().replace("\x00", "\n")
            length = len(message)
            print(f"Received message {length=}")
            pyperclip.copy(message)
    start_server = websockets.serve(handle_message, "0.0.0.0", port)
    asyncio.get_event_loop().run_until_complete(start_server)
    print(f"Server started on port {port}")
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("Server stopped.")

if __name__ == "__main__":
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    run_server(port)
