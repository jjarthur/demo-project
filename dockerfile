FROM eclipse-mosquitto:2.0.6

COPY mosquitto.conf /mosquitto/config/mosquitto.conf

EXPOSE 1885
EXPOSE 9001
