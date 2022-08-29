# install
```sh
#apt update
#apt install -y pip git python3 nano
sudo pip install paho-mqtt  
cd /usr/local/bin  
sudo git clone https://github.com/Denifia/home-assistant-raspberry-pi-mqtt.git  

# edit to suit your environment
sudo nano /usr/local/bin/home-assistant-raspberry-pi-mqtt/mqtt-device.py  

# start up
sudo python /usr/local/bin/home-assistant-raspberry-pi-mqtt/mqtt-device.py  
```

# auto start
```sh
cd /usr/local/bin/home-assistant-raspberry-pi-mqtt  
sudo mv mqtt-device.service /etc/systemd/system/  
sudo systemctl enable mqtt-device.service  
```

# run service
```sh
sudo systemctl start mqtt-device.service
```
