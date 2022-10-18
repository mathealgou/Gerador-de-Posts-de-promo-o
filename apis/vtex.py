import requests
import json
from datetime import datetime

class Vtex:
    def get_promos(account_name: str,appKey: str, appToken: str):
        PROMOTION_API_URL = "api/rnb/pvt/benefits/calculatorconfiguration"
        response = requests.get(f"https://{account_name}.vtexcommercestable.com.br/{PROMOTION_API_URL}", headers={"X-VTEX-API-AppKey": appKey, "X-VTEX-API-AppToken": appToken})
        
        data = response.json()["items"]
        # sort by date in formart '2021-04-05T03:00:00Z'
        
        data.sort(key=lambda x: datetime.strptime(x["beginDate"], '%Y-%m-%dT%H:%M:%SZ'))
        
        # filter for only active promos
        data = filter(lambda x: x["status"] == "active", data)
        
        # filter for only promos with at least one SKU  
        data = filter(lambda x: x["scope"]["skus"] > 0, data)

        data = list(data)
        
        return data
        
    def get_promo(account_name: str, id: str,appKey: str, appToken: str):
        PROMOTION_API_URL = "api/rnb/pvt/calculatorconfiguration"
        print(f"https://{account_name}.vtexcommercestable.com.br/{PROMOTION_API_URL}/{id}")
        response = requests.get(f"https://{account_name}.vtexcommercestable.com.br/{PROMOTION_API_URL}/{id}", headers={"X-VTEX-API-AppKey": appKey, "X-VTEX-API-AppToken": appToken})
        print(response)
        
        data = response.json()
        return data
    
    def parse_promo(promo):
        # TODO: Create a better schema for the promo
        pass