class Terminal:
    def choose_promo(promos: list):
        x =[i["name"] for i in promos][:5]
        for i, j in enumerate(x):
            print(f"\u001b[32m{i+1}  -", "\u001b[37m",j)
        return promos[int(input("Choose a promo: ")) - 1]