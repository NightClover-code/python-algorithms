tva = 0.2

prixHT = float(input("Entrez le prix HT de l'articles: "))
nb = int(input("Entrez le nombre d'articles: "))

ttc = prixHT + (prixHT * tva)

print("Le prix ttc de l'article est: ", ttc, f"le prix ttc de {nb} articles est: ", ttc * nb)





