# FarmersWorld Automation Script

## Why this one
In order to mine automatically, you can find several tools online using differents technologies.  

One of them is [https://farmerscript.online/](https://farmerscript.online/) which lets you manage your FarmersWorld's account and mine every hour for you.  

But to use it, you should have a browser opened 24h/24.   
Using a very cheap VPS (1Go RAM, 2vCPU) or a RPI is cool to do this but the previous site crashes the browser overnight (memory leak ? Idk..)

So this project uses Selenium w/ python to :
* Start the browser
* Get https://farmerscript.online/
* Log in
* Let the script do its business (claim your stuff, auto-repair tools, auto-refill energy, transfert tokens from wallet, ..)
* Close the browser after X minutes

Doing this frequently solved my problem. It is definitly not optimized (to restart the countdown just after it finished..) but at least works.

## Prerequisites
### 1/ Python 3.x & Pip3
Install `python3` and `pip3`... 
```bash 
sudo apt install -y python3 python3-pip
```
### 2/ msmtp
The tool sends email using msmtp. Be sure you have msmtp up & running to send email using this command line : `echo "TEST" | msmtp my-email-address@nsa.com`

### 3/ App requirements
Install project dependencies... 
```bash
pip3 install -r requirements.txt
```

### 4/ Manually validates pop-ups
At start, you should start the browser manually, log in and make actions on site (like claiming, ..) to trigger authorization pop-ups. 
When you have logged in (with OTP sent over email) and validated actions, everything is saved in the default browser profile.  
This tool with reuse this profile in order to not be blocked anymore.

Read this to find you default profile location : [https://www.howtogeek.com/255587/how-to-find-your-firefox-profile-folder-on-windows-mac-and-linux/](https://www.howtogeek.com/255587/how-to-find-your-firefox-profile-folder-on-windows-mac-and-linux/)

## How to use
### 1/ Add crontab
Add this line in you crontab jobs :   
`*/15 * * * * python3 ~/FarmersWorld/fw-autorun.py >> ~/FarmersWorld/fw.log 2>&1`
```bash
crontab -e
```
This will run the script every `15 minutes`.

### 2/ Config
Create & Edit your config file

```bash
cp config-sample.py config.py
```

### 3/ Firefox
This tool uses Firefox but feel free to switch to Chrome or other browsers.  
Add the `geckodriver` binary in you `PATH` ([Download it from here](https://github.com/mozilla/geckodriver/releases))
