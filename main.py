from apis import Vtex, Twitter, Instagram
from decouple import config
import json
from terminal import Terminal
from html import Html
from content import Images, Captions
import time


def main():
    # Vtex auth info
    APP_KEY = config("APP_KEY")
    APP_TOKEN = config("APP_TOKEN")
    ACCOUNT_NAME = config("ACCOUNT_NAME")
    
    # Instagram auth info
    INSTAGRAM_USERNAME = config("INSTAGRAM_USERNAME")
    INSTAGRAM_PASSWORD = config("INSTAGRAM_PASSWORD")
    
    
    vtex = Vtex()
    html = Html()
    terminal = Terminal()
    images = Images()
    instagram = Instagram()
    captions = Captions()
    
    terminal.greet()
    
    # terminal.fake_loading("Connecting to VTEX API...")
    
    promos = vtex.get_promos(ACCOUNT_NAME, APP_KEY, APP_TOKEN)
    
    choosen_promo = terminal.choose_promo(promos)
    
    # terminal.fake_loading("Getting promo info...", sleep=1)
    
    promo = vtex.get_promo(ACCOUNT_NAME, choosen_promo["idCalculatorConfiguration"], APP_KEY, APP_TOKEN)

    sku = vtex.get_sku(ACCOUNT_NAME, promo["skus"][0]["id"], APP_KEY, APP_TOKEN)
    
    terminal.info("Information retrieved successfully!")
    
    raw_html = html.read()
    
    populated_html = html.get_populated_html(raw_html, promo, sku)
    
    css = html.read_css()
    
    # terminal.fake_loading("Generating images...")
    
    images.generate_images_from_html(populated_html, css)
    
    terminal.info("Posting image...")
    
    instagram_caption = captions.get_instagram_caption(promo, sku)
    
    instagram.post(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, instagram_caption)
    
if __name__ == "__main__":
    main()