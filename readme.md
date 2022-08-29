# install
apt update
apt install -y pip git python3 nano

sudo pip install paho-mqtt
cd /usr/local/bin
sudo git clone https://github.com/Denifia/home-assistant-raspberry-pi-mqtt.git
sudo nano /usr/local/bin/home-assistant-raspberry-pi-mqtt/mqtt-device.py
sudo python3 /usr/local/bin/home-assistant-raspberry-pi-mqttn/mqtt-device.py

# auto start
cd /usr/local/bin/home-assistant-raspberry-pi-mqtt
sudo mv mqtt-device.service /etc/systemd/system/
sudo systemctl enable mqtt-device.service

# run service
sudo systemctl start mqtt-device.service
