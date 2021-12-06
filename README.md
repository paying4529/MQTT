# Setup
## Requirements
- MQTT
- paho-mqtt

## Windows
1. Download mosquitto at https://mosquitto.org/download/

2. "工作管理員" => "服務" => find "mosquitto", right click to START

3. Check mosquitto running

`netstat -an | find "1883"`

4. Open port 1883 on Windows firewall

"防火牆" => "進階設定" => "輸入規則"&"輸出規則" => "新增規則" for TCP port 1883

### To run using CMD
1. Note that the client and broker should be under the same WIFI domain.

2. Add in the end of "mosquitto.conf"


`listener 1883`

=> This line is necessary for other external to connect 

`allow_anonymous true`

=> This line specify no need for pwd. 


3. Change to right directory 

`cd D:\嵌入式\mosquitto`

4. Run

`mosquitto.exe -c mosquitto.conf -v`

## Rpi
Add the open source MQTT broker Mosquitto, along with Mosquitto client software on the Pi

`sudo apt-get install mosquitto mosquitto-clients`

#### Subscribe
`mosquitto_sub -h <IP> -t <TOPIC>`

#### Publish 
`mosquitto_pub -h <IP> -t <TOPIC> -m <MESSAGE>`

## Run on Python
`pip install paho-mqtt`

Refer to publish.py and subscribe.py 
