# Home Assistant Raspberry Pi MQTT

Allow Home Assistant to auto discover your Raspberry Pi (or other linux devices) and expose a Shutdown and Restart button over MQTT.

Heavily inspired by [olkal's RPI-MQTT-shutdown](https://github.com/olkal/RPI-MQTT-shutdown) repo.

## Setup
```sh
# you may need to install a few packages first but
# on a raspberry pi they're probably already installed
#apt update
#apt install -y pip git python3 nano

sudo pip install paho-mqtt
cd /usr/local/bin
sudo git clone https://github.com/Denifia/home-assistant-raspberry-pi-mqtt.git

# edit to suit your environment
sudo nano /usr/local/bin/home-assistant-raspberry-pi-mqtt/mqtt-device.py

# test that it starts up
sudo python /usr/local/bin/home-assistant-raspberry-pi-mqtt/mqtt-device.py

# your raspberry pi and it's two buttons should now be in home assistant!
```

# Run as service
```sh
cd /usr/local/bin/home-assistant-raspberry-pi-mqtt
sudo mv mqtt-device.service /etc/systemd/system/
sudo systemctl enable mqtt-device.service

# start the service now instead of waiting for a reboot
sudo systemctl start mqtt-device.service
```
