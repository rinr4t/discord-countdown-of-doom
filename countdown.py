import requests
import json
from zoneinfo import ZoneInfo
from datetime import datetime
import time

targetTimezone = ZoneInfo("insert here") #insert your own timezone in iana format here
#you can find your timezone here: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
token = "placeholder" #insert your discord token here
emoji = "❤️" #copy and paste your emoji here

def getStatus():
    currentTime = datetime.now(targetTimezone)
    countdownTimeString = "2023-10-09 08:30:00" #change this to what you are counting down towards
    countdownTime = datetime.strptime(countdownTimeString, "%Y-%m-%d %H:%M:%S").replace(tzinfo=targetTimezone)
    countdown = countdownTime - currentTime

    days = countdown.days
    hours, remainder = divmod(countdown.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    status = f"{days} days, {hours} hours, and {minutes} minutes left of the holidays" #you can change this to fit what you need
    return status

#this part is forked from Oct0-xox's discord-status-changer - thank you for the json stuff <3
def setStatus(token, status):
    data = {
        "custom_status": {
            "text": status,
            "emoji_name": emoji
        }
    }
    headers = {
        "authorization": token,
        "content-type": "application/json"
    }

    response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, data=json.dumps(data))

    if 200 == response.status_code:
        print("Status updated successfully to " + status + "!")
    else:
        print("Failed to update status. Status code:", response.status_code)

if __name__ == "__main__":
    while True:  #infinite loop to continuously update the status
        status = getStatus()  #get the current status
        setStatus(token, status)  #update the status
        time.sleep(60)  #sleep for 60 seconds (1 minute) before updating again
