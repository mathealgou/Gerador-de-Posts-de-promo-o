from apis import Vtex, Twitter, Instagram
from decouple import config
import json
from terminal import Terminal
from html import Html
from content import Images


def main():
    # Vtex auth info
    APP_KEY = config("APP_KEY")
    APP_TOKEN = config("APP_TOKEN")
    ACCOUNT_NAME = config("ACCOUNT_NAME")
    
    # Instagram auth info

    INSTAGRAM_USERNAME = config("INSTAGRAM_USERNAME")
    INSTAGRAM_PASSWORD = config("INSTAGRAM_PASSWORD")
    
    promos = Vtex.get_promos(ACCOUNT_NAME, APP_KEY, APP_TOKEN)
    
    choosen_promo = Terminal.choose_promo(promos)
    
    promo = Vtex.get_promo(ACCOUNT_NAME, choosen_promo["idCalculatorConfiguration"], APP_KEY, APP_TOKEN)

    html = Html.read().format(
        name=promo["name"],
        price=12
    )
    css = Html.read_css()
    
    Images.generate_images_from_html(html, css)
    
    # Instagram.post(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    
    # Twitter.post_image(bearer_token=TWITTER_BEARER_TOKEN, api_key=TWITTER_API_KEY, api_secret=TWITTER_API_SECRET)
    
if __name__ == "__main__":
    main()