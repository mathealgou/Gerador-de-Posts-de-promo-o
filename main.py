from apis import Vtex
from decouple import config
import json
from terminal import Terminal

def main():
    
    APP_KEY = config("APP_KEY")
    APP_TOKEN = config("APP_TOKEN")
    ACCOUNT_NAME = config("ACCOUNT_NAME")
    
    promos = Vtex.get_promos(ACCOUNT_NAME, APP_KEY, APP_TOKEN)
    
    choosen_promo = Terminal.choose_promo(promos)
    
    promo = Vtex.get_promo(ACCOUNT_NAME, choosen_promo["idCalculatorConfiguration"], APP_KEY, APP_TOKEN)

    print(json.dumps(promo, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()