class Captions:
    def get_instagram_caption(self, promo, sku):
        return f"🚀 {promo['name']} | {sku['name']} 🚀\n\n🔥 De R$ {sku['original_price']} por R$ {sku['original_price'] - (sku['original_price'] * promo['percentualDiscountValue'] / 100)} 🔥\n\n🔗 https://avantivtexio.myvtex.com/{sku['id']}"