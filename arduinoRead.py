#https://www.youtube.com/watch?v=Kr1RyK6WENQ tutorial from reading from serial

import instaloader
import requests

from serial import Serial

mySerial = Serial(port='COM5', baudrate=9600)

username = "soy_milk_is_the_best_milk"
instagram = instaloader.Instaloader()
profile = instaloader.Profile.from_username(instagram.context, username)
r = requests.get(profile.profile_pic_url)

while True:
    value = mySerial.readline()
    valueInString = str(value, 'UTF-8').strip()
    #print(valueInString)
    if valueInString == "1":
        with open(f"{username}.jpg", 'wb') as photo:
            photo.write(r.content)
            photo.close()
            print(f"Followers: {profile.followers}")