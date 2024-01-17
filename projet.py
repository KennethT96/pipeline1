def test_params(today):
    if today > 20:
        print("Il ne vous reste plus beaucoup de temps pour faire vos objectifs.")
    else:
        print("Vous avez encore du temps pour atteindre vos objectifs.")

# Importer le module sys pour pouvoir accéder aux arguments de la ligne de commande
if __name__ == "__main__":
import sys
today = int(sys.argv[1])
test_params(today)
