class Captions:
    def get_instagram_caption(self, promo, sku):
        return f"š {promo['name']} | {sku['name']} š\n\nš„ De R$ {sku['original_price']} por R$ {sku['original_price'] - (sku['original_price'] * promo['percentualDiscountValue'] / 100)} š„\n\nš https://avantivtexio.myvtex.com/{sku['id']}"