import time
import random
from client import Client

def run():
    generator = Client("generator")
    generator.client.loop_start()
    while True:
        i = random.randint(1, 100)
        generator.client.publish("demo/svg/height", str(i))
        print("generator_pub: {}".format(i))
        time.sleep(0.2)

if __name__ == "__main__":
    run()
