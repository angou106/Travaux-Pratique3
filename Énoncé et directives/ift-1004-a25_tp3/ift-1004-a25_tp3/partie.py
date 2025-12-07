"""
Module contenant la description de la classe Partie qui permet de jouer une partie du jeu démineur.
Dois être démarré en appelant la méthode jouer(). Cette classe contient les informations sur une
partie et utilise un objet tableau_mines (une instance de la classe Tableau).
"""

from tableau import Tableau


class Partie:
    """
    Contient les informations sur une partie du jeu Démineur, qui se jouera avec
    un tableau de mines. Des méthodes sont disponibles pour faire avancer la partie
    et interagir avec l'utilisateur.

    Attributes:
        tableau_mines (Tableau): Le tableau de cases où les mines sont cachées avec lequel se
                déroule la partie.
        partie_terminee (bool): True lorsque l'utilisateur a terminé de jouer la partie (victoire ou défaite)
    """

    def __init__(self):
        """
        Initialisation de la Partie.

        Note: L'instance de la classe Tableau, qui sera manipulée par les méthodes de la classe,
              sera initialisée lors de l'appel de la méthode Partie.jouer().
        """
        self.tableau_mines = None
        self.partie_terminee = False

    def jouer(self):
        """
        Tant que la partie n'est pas terminée, on joue un tour de la partie.
        Une fois la partie terminée, on affiche le tableau de cases complètement dévoilée
        et on indique un message sur l'issue de la partie (victoire ou défaite).
        Il s'agit d'une victoire si le tableau ne contient plus de cases à dévoiler.
        """

        # TODO: Modifier le code pour demander à l'utilisateur de choisir la taille
        #   du tableau (nombre de lignes et nombres de colonnes, ainsi que le nombre
        #   de mines), passez ensuite ces valeurs en argument au constructeur de Tableau.
        #   Note: il n'est pas demandé de valider les entrées ici

        self.tableau_mines = Tableau()

        compteur_tours = 0
        while not self.partie_terminee:
            compteur_tours += 1
            print(f"\n===> Tour #{compteur_tours} <===")
            self.tableau_mines.afficher_tableau()
            self.tour()

        self.tableau_mines.afficher_solution()

        # TODO: Afficher le message de victoire ou de défaite

    def tour(self):
        """
        Jouer un tour, c'est-à-dire:

        À chaque tour:
            - On demande à l'utilisateur les coordonnées d'une case à dévoiler
            - On effectue le dévoilement en cascade en démarrant à cette case
            - On détecte si une mine a été actionnée,
              auquel cas affecte True à l'attribut self.partie_terminee.
            - On détecte si toutes les cases ont été dévoilées,
              auquel cas affecte True à l'attribut self.partie_terminee.
        """
        # TODO: À compléter
        pass

    def demander_coordonnees_case_a_devoiler(self):
        """
        Méthode qui demande à l'utilisateur d'entrer la coordonnée de la case qu'il veut dévoiler.
        Cette coordonnée comporte un numéro de rangée et un numéro de colonne.
        Tant que les coordonnées ne sont pas valides, on redemande de nouvelles coordonnées.
        Une fois les coordonnées validées, on retourne les deux numéros sous forme d'entiers.

        Returns:
            tuple[int, int]: Un tuple contenant les coordonnées en x et y.
                - int: Numéro de la rangée
                - int: Numéro de la colonne
        """
        # TODO: À compléter
        pass

    def valider_coordonnees(self, rangee_x, colonne_y):
        """
        Méthode qui valide les coordonnées reçues en paramètres.
        Les coordonnées doivent:
            1) être des caractères numériques;
            2) être à l'intérieur des valeurs possibles des rangées et des colonnes
                du tableau; et
            3) correspondre à une case qui n'a pas encore été dévoilée.

        Args:
            rangee_x (str):     Chaîne de caractères contenant la rangée
            colonne_y (str):    Chaîne de caractères contenant  la colonne

        Returns:
            bool : True si les coordonnées sont valides, False autrement.
        """
        # TODO: À compléter
        pass
