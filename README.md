# Plex-Mqtt-Connector

This connector allows to combine MQTT with the webhooks of the Plex Media Server.

**Please don't forget to set the ip address of your MQTT-Server!!!**

## Example

For example you can connect OpenHAB to Plex with this script. Plex will send it's webhooks to your local machine on port 5000. The script will receive this webhooks and publish a part of the content into a topic on your MQTT-Server. Items in your OpenHAB instance are able to show the latest message (player state, title and type of the media).

If you use rules you are able to dim your lights everytime a movie or episode of your favorite series begins. Also you can turn on your lights after the player stopped.

## Requirements

You can use this script on your local machine. But this machine has to be turned on everytime you wanna use this function. Otherwise you could use a Raspberry Pi.

Don't forget to install the Python packages and Python itself.

Also you have to install a MQTT-Server on any machine. E. g. OpenHAB is able to work as MQTT-Server.

## FAQ

### Which is the topic for my clients?

Every client has an unique id. You can find this unique id in your Plex Server or the XML of the devices. You can also use an MQTT-Explorer and search for the id after a message was published into a topic.

Every topic starts with plex/ and contains the id of your client. Foreach information (title and and type) a subtopic is used.

The state of your player will be published into the main topic (plex/[playerid]).
The topic for your title is called plex/[playerid]/title
The topic for your type is called plex/[playerid]/type

### Where to configure my webhooks?

You need a Plex Pass to configure webhooks on your server.

Every webhook should be send to: http://[IP-ADDRESS]:5000/webhook

### More information

You will find more information about this project and scenarios here: https://hobbyblogging.de/heimkino-im-smart-home (German only)

---

Clone or fork this repo to add functions.

And don't forget to take a look at [Hobbyblogging](https://hobbyblogging.de). Thank you!