import tweepy
class Twitter:
    def post_image(api_key, api_secret, bearer_token ):
        auth = tweepy.OAuthHandler("apiKey",
                                "apiKey")

        auth.set_access_token("apiKey",
                            "apiKey")
        api.verify_credentials()

        api = tweepy.API(auth)

        media = api.media_upload(filename="./test.png")

        tweet = api.update_status(status="Image upload", media_ids= 
        [media.media_id_string])