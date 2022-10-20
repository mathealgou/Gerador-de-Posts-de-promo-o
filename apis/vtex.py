import requests
import json
from datetime import datetime

class Vtex:
    def get_promos(self, account_name: str,appKey: str, appToken: str):
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
        
    def get_promo(self, account_name: str, id: str, appKey: str, appToken: str):
        PROMOTION_API_URL = "api/rnb/pvt/calculatorconfiguration"
        response = requests.get(f"https://{account_name}.vtexcommercestable.com.br/{PROMOTION_API_URL}/{id}", headers={"X-VTEX-API-AppKey": appKey, "X-VTEX-API-AppToken": appToken})
        
        data = response.json()
        return data
    
    def get_sku_price(self, account_name: str, sku_id: str, appKey: str, appToken: str):
        response = requests.get(f"https://api.vtex.com/{account_name}/pricing/prices/{sku_id}", headers={"X-VTEX-API-AppKey": appKey, "X-VTEX-API-AppToken": appToken})
        data = response.json()
        return data
    
    def get_sku(self, account_name: str, sku_id, appKey: str, appToken: str):
        response = requests.get(f"https://{account_name}.vtexcommercestable.com.br/api/catalog_system/pvt/sku/stockkeepingunitbyid/{sku_id}", headers={"X-VTEX-API-AppKey": appKey, "X-VTEX-API-AppToken": appToken})
        data = response.json()
        
        price = self.get_sku_price(account_name, sku_id, appKey, appToken)

        sku = {
            "id": data["Id"],
            "name": data["NameComplete"],
            "image_url": data["ImageUrl"],
            "brand": data["BrandName"],
            "original_price": price["basePrice"],
        }
        
        return sku