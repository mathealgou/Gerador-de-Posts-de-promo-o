class Terminal:
    def choose_promo(promos: list):
        x =[i["name"] for i in promos]
        for i, j in enumerate(x):
            print(i+1, j)
        return promos[int(input("Choose a promo: ")) - 1]