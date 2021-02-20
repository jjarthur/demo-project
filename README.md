# mqtt-example-project

## Installing python packages
```pip install -r requirements.txt```

## Running the broker
* Run the broker locally: `mosquitto -c mosquitto.conf -v`
* ...or with Docker:
    1. `docker build -t eclipse-mosquitto .`
    2. `docker run --rm -it eclipse-mosquitto` (or `docker run --rm -p 1885:1885 -p 9001:9001 -it eclipse-mosquitto` on Windows)

## Running the application
1. Run the generator: `python src/mqtt/generator.py`
2. Run the reader: `python src/mqtt/reader.py`
3. Open `src/app/index.html` in web browser
