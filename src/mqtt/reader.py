from client import Client

def run():
    reader = Client("reader")
    reader.subscribe("demo/svg/height")
    reader.client.loop_forever()

if __name__ == "__main__":
    run()
