from apis import Vtex
from decouple import config
import json
from terminal import Terminal
from html import Html

from html2image import Html2Image

def main():
    hti = Html2Image()
    
    APP_KEY = config("APP_KEY")
    APP_TOKEN = config("APP_TOKEN")
    ACCOUNT_NAME = config("ACCOUNT_NAME")
    
    promos = Vtex.get_promos(ACCOUNT_NAME, APP_KEY, APP_TOKEN)
    
    print(json.dumps(promos, indent=4))
    
    choosen_promo = Terminal.choose_promo(promos)
    
    promo = Vtex.get_promo(ACCOUNT_NAME, choosen_promo["idCalculatorConfiguration"], APP_KEY, APP_TOKEN)

    print(json.dumps(promo, indent=4, sort_keys=True))

    html = Html.read().format(
        name=promo["name"],
    )
    
    hti.screenshot(
    html_str=html, css_str=Html.read_css(),
    save_as='test.png'
    )
    
    print(Html.read().format(test=promo["name"]))
    
if __name__ == "__main__":
    main()