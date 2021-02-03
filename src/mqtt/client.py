import paho.mqtt.client as mqtt

class Client:
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected OK")
        else:
            print("Bad connection, rc={}".format(rc))

    def on_message(self, client, userdata, msg):
        print("{}_msg: {} {}".format(self.client_id, msg.topic, str(msg.payload)))

    def on_disconnect(self, client, userdata, flags, rc=0):
        print("Disconnected: {}".format(rc))

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def __init__(self, client_id):
        self.client_id = client_id
        self.client = mqtt.Client(self.client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

        self.client.connect("127.0.0.1", 1885, 60)
