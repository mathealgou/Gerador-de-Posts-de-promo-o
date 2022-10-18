import tweepy
class Twitter:
    def post_image(api_key, api_secret, bearer_token ):
        auth = tweepy.OAuth1UserHandler(
            "n9GLII6KyWKQF4MWtMex33bDh",
            "Q7MStirDSacokS7QLYsrYsUhv47pltF1JdbbB4BRzGRhB1GDkt",
            "AAAAAAAAAAAAAAAAAAAAAGMuiQEAAAAAlVImBZWgIiB0D8TJUZN%2FxM%2B2knE%3DD2VQBH4wEpvuCJW3L8jtybC85Yv7ZRu6aL4h5bnEQHGZEU1vYM",
            "SyNLKn2hywscVOVvwtLgs0zW0yaSFOW3_sXj-dqItqkxj20d3i"
        )

        api = tweepy.API(auth)

        media = api.media_upload(filename="./test.png")
        print("MEDIA: ", media)

        tweet = api.update_status(status="Image upload", media_ids= 
        [media.media_id_string])