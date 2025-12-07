"""
Module de tests unitaires pour case.

Ce module contient les tests unitaires pour valider le bon fonctionnement
des méthodes de la classe Case.
"""

from case import Case


print("Exécution des tests unitaires du module case...")

une_case = Case()
assert not une_case.est_minee
assert not une_case.est_devoilee
assert une_case.nombre_mines_voisines == 0
assert une_case.obtenir_apparence() == " "

une_case.devoiler()
assert une_case.est_devoilee

une_case.ajouter_mine()
assert une_case.est_minee
assert une_case.obtenir_apparence() == "M"
assert not une_case.est_voisine_d_une_mine()

une_case.est_minee = False
for i in range(1, 5):
    une_case.ajouter_une_mine_voisine()
    assert une_case.nombre_mines_voisines == i
    assert une_case.est_voisine_d_une_mine()
    assert une_case.obtenir_apparence() == str(i)

print("Tous les tests du module case sont réussis!")
