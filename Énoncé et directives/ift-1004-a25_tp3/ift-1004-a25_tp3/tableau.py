"""
Module contenant la description de la classe Tableau.
Un tableau est utilisé pour jouer une partie du jeu Démineur.
"""

from case import Case
from random import randint


class Tableau:
    """
    Tableau du jeu de démineur, implémenté avec un dictionnaire de cases.

    Warning:
        Si vous ajoutez des attributs à la classe Tableau, n'oubliez pas de les documenter ici.

    Attributes:
        dimension_rangee (int): Nombre de rangées du tableau
        dimension_colonne (int): Nombre de colonnes du tableau
        nombre_mines (int): Nombre de mines cachées dans le tableau

        nombre_cases_sans_mine_a_devoiler (int) : Nombre de cases sans mine qui n'ont pas encore été dévoilées
            Initialement, ce nombre est égal à dimension_rangee * dimension_colonne - nombre_mines

        dictionnaire_cases (dict): Un dictionnaire de case en suivant le format suivant:
            Les clés sont les positions du tableau sous la forme d'un tuple (x, y),
                x étant le numéro de la rangée, y étant le numéro de la colonne.
            Les éléments sont des objets de la classe Case.
    """

    def __init__(self, dimension_rangee=5, dimension_colonne=5, nombre_mines=5):
        """
        Initialisation d'un objet tableau.

        Attributes:
            dimension_rangee (int): Nombre de rangées du tableau (valeur par défaut: 5)
            dimension_colonne (int): Nombre de colonnes du tableau (valeur par défaut: 5)
            nombre_mines (int): Nombre de mines cachées dans le tableau (valeur par défaut: 5)
        """

        self.dimension_rangee = dimension_rangee
        self.dimension_colonne = dimension_colonne
        self.nombre_mines = nombre_mines

        # Le dictionnaire de case, vide au départ, qui est rempli par la fonction initialiser_tableau().
        self.dictionnaire_cases = {}

        self.initialiser_tableau()

        self.nombre_cases_sans_mine_a_devoiler = (
            self.dimension_rangee * self.dimension_colonne - self.nombre_mines
        )

    def valider_coordonnees(self, rangee_x, colonne_y):
        """
        Valide les coordonnées reçues en argument. Les coordonnées sont considérées valides si elles se trouvent bien
        dans les dimensions du tableau.

        Args:
            rangee_x (int) : Numéro de la rangée de la case dont on veut valider les coordonnées
            colonne_y (int): Numéro de la colonne de la case dont on veut valider les coordonnées

        Returns:
            bool: True si les coordonnées (x, y) sont valides, False autrement
        """
        rangee_valide = 1 <= rangee_x <= self.dimension_rangee
        colonne_valide = 1 <= colonne_y <= self.dimension_colonne
        return rangee_valide and colonne_valide

    def obtenir_case(self, rangee_x, colonne_y):
        """
        Récupère une case à partir de ses numéros de ligne et de colonne

        Args:
            rangee_x (int) : Numéro de la rangée de la cas
            colonne_y (int): Numéro de la colonne de la case
        Returns:
            Case: Une référence vers la case obtenue
            (ou None si les coordonnées ne sont pas valides)
        """
        if not self.valider_coordonnees(rangee_x, colonne_y):
            return None

        coordonnees = (rangee_x, colonne_y)
        return self.dictionnaire_cases[coordonnees]

    def obtenir_voisins(self, rangee_x, colonne_y):
        """
        Retourne une liste de coordonnées correspondant aux cases voisines d'une case. Toutes les coordonnées retournées
        doivent être valides (c'est-à-dire se trouver à l'intérieur des dimensions du tableau).

        Args:
            rangee_x (int) : Numéro de la rangée de la case dont on veut connaître les cases voisines
            colonne_y (int): Numéro de la colonne de la case dont on veut connaître les cases voisines

        Returns:
            list<tuple<int>> : Liste des coordonnées (tuple x, y) valides des cases voisines de la case dont les coordonnées
            sont reçues en argument
        """
        voisinage = (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        )

        liste_coordonnees_cases_voisines = []

        # TODO: Générer la liste des coordonnées valides des cases voisine.
        #  Le tuple voisinage est là pour vous aider.

        return liste_coordonnees_cases_voisines

    def initialiser_tableau(self):
        """
        Initialise le tableau à son contenu initial en suivant les étapes suivantes:
            1) On crée chacune des cases du tableau (cette étape est programmée pour vous).
            2) On y ajoute ensuite les mines dans certaines cases qui sont choisies au hasard
                (attention de ne pas choisir deux fois la même case!).
                - À chaque fois qu'on ajoute une mine dans une case, on obtient la liste de
                  ses voisins (pour se faire, utilisez la méthode obtenir_voisins)
                - Pour chaque voisin, on appelle la méthode ajouter_une_mine_voisine de la case correspondante.
        """
        for rangee_x in range(1, self.dimension_rangee + 1):
            for colonne_y in range(1, self.dimension_colonne + 1):
                coordonnees = (rangee_x, colonne_y)
                self.dictionnaire_cases[coordonnees] = Case()

        # TODO: À compléter (étape 2)
        # Nous vous suggérons d'utiliser dans la fonction randint(a,b) du module random qui
        # retourne un entier aléatoire compris entre a et b inclusivement.

    def valider_coordonnees_a_devoiler(self, rangee_x, colonne_y):
        """
        Valide que les coordonnées reçues en argument sont celles d'une case que l'on peut dévoiler
        (donc que les coordonnées sont valides et que la case correspondante n'a pas encore été dévoilée).

        Args:
            rangee_x (int) : Numéro de la rangée de la case dont on veut valider les coordonnées
            colonne_y (int): Numéro de la colonne de la case dont on veut valider les coordonnées

        Returns
            bool: True si la case à ces coordonnées (x, y) peut être dévoilée, False autrement (donc si la
                  case a déjà été dévoilée ou que les coordonnées ne dont pas valides).
        """
        # TODO: À compléter
        pass

    def afficher_solution(self):
        """
        Méthode qui affiche le tableau de la solution à l'écran. La solution montre les
        mines pour les cases qui en contiennent et la valeur du nombre de mines voisines
        pour les autres cases.
        """
        self.tout_devoiler()
        self.afficher_tableau()

    def tout_devoiler(self):
        """
        Méthode qui dévoile toutes les cases du tableau
        """
        # TODO: À compléter

    def afficher_tableau(self):
        """
        Méthode qui affiche le tableau à l'écran. Le tableau montre le contenu des cases dévoilées
        (mine ou nombre de mines voisines) ou un point pour les cases non dévoilées.

        Vous pouvez vous inspirer de la méthode afficher_solution
        """
        print()  # Retour de ligne

        for rangee_x in range(0, self.dimension_rangee + 1):
            # Affichage d'une ligne, caractère par caractère
            for colonne_y in range(0, self.dimension_colonne + 1):
                if rangee_x == 0 and colonne_y == 0:
                    # Premiers caractères de l'en-tête (coin supérieur gauche)
                    car = "  |"
                elif rangee_x == 0:
                    # En-tête: numéro de la colonne
                    # (si y > 10, on affiche seulement l'unité pour éviter les décalages)
                    car = f"{colonne_y % 10}"
                elif colonne_y == 0:
                    # Début de ligne: numéro de la ligne sur deux caractères,
                    # suivi d'une ligne verticale.
                    car = f"{rangee_x:<2}|"
                else:
                    # Contenu d'une case
                    case_xy = self.obtenir_case(rangee_x, colonne_y)
                    car = case_xy.obtenir_apparence()

                # Afficher le caractère suivit d'un espace (sans retour de ligne)
                print(car, end=" ")

            # À la fin de chaque ligne
            print()  # Retour de ligne
            if rangee_x == 0:  # Ligne horizontale de l'en-tête
                print("--+-" + "--" * self.dimension_colonne)

    def contient_cases_sans_mines_a_devoiler(self):
        """
        Méthode qui indique si le tableau contient des cases sans mines à dévoiler.

        Returns:
            bool: True s'il reste des cases à dévoiler, False autrement.
        """
        # TODO: À compléter
        pass

    def devoilement_en_cascade(self, rangee_x, colonne_y):
        """
        Méthode qui dévoile la case aux coordonnées en argument (utilisez  la méthode
        devoiler_case du tableau), et qui, si elle est vide, appelle le dévoilement
        en cascade pour chacun de ses voisins, lorsque ceux-ci ne soient pas déjà dévoilés

        Args:
            rangee_x (int) : Numéro de la rangée de la case à dévoiler
            colonne_y (int): Numéro de la colonne de la case à dévoiler
        """
        # PARTIE 1, on obtient et dévoile la case
        case = self.obtenir_case(rangee_x, colonne_y)
        self.devoiler_case(case)

        # PARTIE 2, on dévoile les voisins
        # TODO: À compléter

    def devoiler_case(self, case):
        """
        Méthode qui dévoile le contenu de la case reçue en argument.
        Si la case ne contient pas de mine, on décrémente l'attribut qui représente le nombre de
        cases sans mine à dévoiler.

        Args:
            case (Case) : La case à dévoiler
        """
        # TODO: À compléter
        pass

    def contient_mine(self, rangee_x, colonne_y):
        """
        Méthode qui vérifie si la case dont les coordonnées sont reçues en argument contient une mine.

        Args:
            rangee_x (int) : Numéro de la rangée de la case dont on veut vérifier si elle contient une mine
            colonne_y (int): Numéro de la colonne de la case dont on veut vérifier si elle contient une mine

        Returns:
            bool: True si la case à ces coordonnées (x, y) contient une mine, False autrement.
        """
        # TODO: À compléter
        pass
