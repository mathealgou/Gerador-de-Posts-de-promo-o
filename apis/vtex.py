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
        
        data.reverse()
        
        return data
        
    def get_promo(account_name: str, id: str,appKey: str, appToken: str):
        PROMOTION_API_URL = "api/rnb/pvt/calculatorconfiguration"
        print(f"https://{account_name}.vtexcommercestable.com.br/{PROMOTION_API_URL}/{id}")
        response = requests.get(f"https://{account_name}.vtexcommercestable.com.br/{PROMOTION_API_URL}/{id}", headers={"X-VTEX-API-AppKey": appKey, "X-VTEX-API-AppToken": appToken})
        
        data = response.json()
        return data