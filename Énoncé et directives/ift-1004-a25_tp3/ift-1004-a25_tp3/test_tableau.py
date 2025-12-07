"""
Module de tests unitaires pour tableau.

Ce module contient les tests unitaires pour valider le bon fonctionnement
des méthodes de la classe Tableau.
"""

from tableau import Tableau


def test_initialisation():
    tableau_test = Tableau()

    assert tableau_test.contient_cases_sans_mines_a_devoiler()
    assert (
        tableau_test.nombre_cases_sans_mine_a_devoiler
        == tableau_test.dimension_colonne * tableau_test.dimension_rangee
        - tableau_test.nombre_mines
    )


def test_valider_coordonnees():
    tableau_test = Tableau()
    dimension_x, dimension_y = (
        tableau_test.dimension_rangee,
        tableau_test.dimension_colonne,
    )

    assert tableau_test.valider_coordonnees(dimension_x, dimension_y)
    assert not tableau_test.valider_coordonnees(dimension_x + 1, dimension_y)
    assert not tableau_test.valider_coordonnees(dimension_x, dimension_y + 1)
    assert not tableau_test.valider_coordonnees(-dimension_x, dimension_y)
    assert not tableau_test.valider_coordonnees(0, 0)


def test_obtenir_case():
    tableau_test = Tableau()
    case1 = tableau_test.obtenir_case(3, 3)
    assert case1 == tableau_test.obtenir_case(3, 3)
    assert case1 != tableau_test.obtenir_case(3, 4)
    assert tableau_test.obtenir_case(10, 10) is None


def test_valider_coordonnees_a_devoiler():
    tableau_test = Tableau()
    assert tableau_test.valider_coordonnees_a_devoiler(3, 3)
    tableau_test.obtenir_case(3, 3).devoiler()
    assert not tableau_test.valider_coordonnees_a_devoiler(3, 3)
    assert not tableau_test.valider_coordonnees_a_devoiler(10, 10)


def test_obtenir_voisins():
    tableau_test = Tableau()
    voisins = tableau_test.obtenir_voisins(3, 3)
    voisins_attendus = [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]
    for i in range(len(voisins_attendus)):
        assert voisins[i] in voisins_attendus
        assert voisins_attendus[i] in voisins
    assert len(tableau_test.obtenir_voisins(3, 3)) == 8
    assert len(tableau_test.obtenir_voisins(1, 1)) == 3
    assert len(tableau_test.obtenir_voisins(5, 5)) == 3


def test_devoiler_case():
    tableau_test_1 = Tableau(5, 5, 0)
    n_mines = tableau_test_1.nombre_cases_sans_mine_a_devoiler
    case = tableau_test_1.obtenir_case(3, 3)
    assert not case.est_devoilee
    tableau_test_1.devoiler_case(case)
    assert case.est_devoilee
    assert tableau_test_1.nombre_cases_sans_mine_a_devoiler == n_mines - 1

    tableau_test_2 = Tableau(5, 5, 25)
    n_mines = tableau_test_2.nombre_cases_sans_mine_a_devoiler
    case = tableau_test_2.obtenir_case(3, 3)
    tableau_test_2.devoiler_case(case)
    assert tableau_test_2.nombre_cases_sans_mine_a_devoiler == n_mines


def test_case_contient_mine():
    tableau_test_1 = Tableau(5, 5, 25)
    assert tableau_test_1.contient_mine(3, 3)
    tableau_test_2 = Tableau(5, 5, 0)
    assert not tableau_test_2.contient_mine(3, 3)


def test_contient_cases_a_devoiler():
    tableau_test = Tableau(5, 5, 25)
    assert not tableau_test.contient_cases_sans_mines_a_devoiler()
    tableau_test = Tableau(5, 5, 24)
    assert tableau_test.contient_cases_sans_mines_a_devoiler()


# Les cinq prochaines lignes de code sont là pour vous aider à tester votre
# première tentative d'implémentation des méthodes initialiser_tableau et afficher_tableau.

tableau_test = Tableau()
print("\nTABLEAU:")
tableau_test.afficher_tableau()
print("\nSOLUTION:")
tableau_test.afficher_solution()

print("Exécution des tests unitaires du module tableau...")
test_initialisation()
test_valider_coordonnees()
test_obtenir_case()
test_valider_coordonnees_a_devoiler()
test_obtenir_voisins()
test_devoiler_case()
test_case_contient_mine()
test_contient_cases_a_devoiler()
print("Tous les tests du module tableau sont réussis!")

# ATTENTION, il n'y a pas de tests pour le dévoilement en cascade
