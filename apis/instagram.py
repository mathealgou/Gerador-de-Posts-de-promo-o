from instagrapi import Client
import os 
import glob

class Instagram:
    def post(self, username, password, caption):
        client = Client()
        client.login(username, password)
        client.photo_upload("./test.jpg", caption)