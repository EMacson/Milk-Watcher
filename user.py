#https://www.youtube.com/watch?v=E6wgokYYrUo

import instaloader
import requests

username = input("Enter username: ")
instagram = instaloader.Instaloader()
profile = instaloader.Profile.from_username(instagram.context, username)
r = requests.get(profile.profile_pic_url)

with open(f"{username}.jpg", 'wb') as photo:
    photo.write(r.content)
    photo.close()

print(f"Followers: {profile.followers}")