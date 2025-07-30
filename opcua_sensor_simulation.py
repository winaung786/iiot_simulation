from asyncua import ua, Server
import asyncio
import random

async def main():
    """Continuously update OPC UA variables with random temperature and humidity values."""
    server = Server()
    await server.init()
    # Set endpoint for the OPC UA server
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    # Register namespace
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)
    # Add objects and variables to the server
    objects = await server.nodes.objects
    myobj = await objects.add_object(idx, "MyObject")
    temperature = await myobj.add_variable(idx, "Temperature", 0.0)
    humidity = await myobj.add_variable(idx, "Humidity", 0.0)
    # Make variables writable
    await temperature.set_writable()
    await humidity.set_writable()
    # Start server and update values in a loop
    async with server:
        while True:
            temp_value = random.uniform(20.0, 25.0)
            hum_value = random.uniform(30.0, 50.0)
            await temperature.write_value(temp_value)
            await humidity.write_value(hum_value)
            print(f"Temperature: {temp_value}, Humidity: {hum_value}")
            await asyncio.sleep(1)

# Run the asynchronous OPC UA server simulation
asyncio.run(main())
