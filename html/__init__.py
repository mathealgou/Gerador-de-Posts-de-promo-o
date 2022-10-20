import json
from apis import Vtex
class Html:
    def read(self):
        with open("./html/html.html", 'r') as f:
            return f.read()
    
    def read_css(self):
        with open("./html/css.css", 'r') as f:
            return f.read()
    
    def get_populated_html(self, html, promo, sku):
        price = f"De <s>R$ {sku['original_price']}</s> por { sku['original_price'] - (sku['original_price'] * promo['percentualDiscountValue'] / 100)}"
        
        return html.format(
        name=promo["name"],
        price=price,
        image_url=sku["image_url"],
        product_name=sku["name"]
    )