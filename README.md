# VIOT
smart voting using iot with facial and finger recognition
this uses api to find out the correct face matched or not 
it uses the R305 module fingerprint Sensor and a Raspberry pi USB TTL converter to work with the fingerprint.
The library for finger print can be downloaded 

1)sudo bash

Now we add the necessary package sources 

2)wget -O - http://apt.pm-codeworks.de/pm-codeworks.de.gpg | apt-key add -

3)wget http://apt.pm-codeworks.de/pm-codeworks.list -P /etc/apt/sources.list.d/

We then update the available packages and install the Python library:

4)apt-get update

5)apt-get install python-fingerprint --yes

If an error has occurred (in particular, that not all dependent packages have been installed), then execute the following:
apt-get -f install

the necessary code can be found in the particular folder path of raspberry pi

/usr/share/doc/python_fingerprint

