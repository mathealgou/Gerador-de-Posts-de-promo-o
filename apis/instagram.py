from instagrapi import Client
import os 
import glob

class Instagram:
    def post(username, password):
        print(username, password)
        client = Client()
        client.login(username, password)
        client.photo_upload("./test.jpg", "test")