let client = new Paho.MQTT.Client("127.0.0.1", Number(9001), "readerjs");

client.onMessageArrived = onMessageArrived;

client.connect({ onSuccess: onConnect });

function onConnect() {
  console.log("Connected OK");
  client.subscribe("demo/svg/height");
}

function onMessageArrived(message) {
    $(document).ready(function() {
        $("img").css("height", message.payloadString);
    });
}
