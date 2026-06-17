import asyncio


async def handle_client(reader, writer):
    address = writer.get_extra_info("peername")

    print(f"Client connected: {address}")

    try:
        while True:

            data = await reader.read(1024)

            if not data:
                break

            message = data.decode()

            print(
                f"Received from {address}: "
                f"{message}"
            )

            # Echo
            writer.write(data)

            await writer.drain()

    except ConnectionResetError:
        pass

    print(f"Client disconnected: {address}")

    writer.close()

    await writer.wait_closed()


async def main():

    server = await asyncio.start_server(
        handle_client,
        "127.0.0.1",
        12345
    )

    address = server.sockets[0].getsockname()

    print(f"Server started on {address}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())