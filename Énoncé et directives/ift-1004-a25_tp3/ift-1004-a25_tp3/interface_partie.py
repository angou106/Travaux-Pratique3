"""
Interface graphique du jeu Démineur

Ce fichier présente une ébauche d'interface. Vous pouvez le modifier à souhait.
"""

from tkinter import Tk, Frame, Button, messagebox, Toplevel, Label, Entry, Canvas, Menu

from case import Case
from tableau import Tableau
from bouton_case import BoutonCase


class InterfacePartie(Tk):
    # Couleurs du démineur classique pour les chiffres
    COULEURS_CHIFFRES = {
        "1": "#0000FF",  # Bleu
        "2": "#008000",  # Vert
        "3": "#FF0000",  # Rouge
        "4": "#000080",  # Bleu foncé
        "5": "#800000",  # Marron
        "6": "#008080",  # Cyan
        "7": "#000000",  # Noir
        "8": "#808080",  # Gris foncé
    }

    # Couleurs de l'interface Windows classique
    COULEUR_FOND = "#C0C0C0"  # Gris clair
    COULEUR_CASE_CACHEE = "#C0C0C0"  # Gris clair
    COULEUR_CASE_DEVOILEE = "#C0C0C0"  # Gris clair
    COULEUR_MINE_EXPLOSEE = "#FF0000"  # Rouge vif
    COULEUR_LED = "#000000"  # Noir
    COULEUR_LED_FOND = "#300000"  # Rouge très sombre / Bordeaux foncé

    # États du smiley
    SMILEY_NORMAL = "🙂"
    SMILEY_GAGNE = "😎"
    SMILEY_PERDU = "😵"

    def __init__(self):
        """
        Constructeur de la classe InterfacePartie.
        Crée tous les boutons existants dans l'interface, dont ceux qui correspondent à des cases.
        """
        super().__init__()

        self.title("Démineur")
        self.resizable(False, False)
        self.configure(bg=self.COULEUR_FOND)

        self.dimension_rangee = 5
        self.dimension_colonne = 5
        self.nombre_mines = 5

        # Créer la barre de menu
        self.creer_menu()

        # Frame principal avec bordure 3D style Windows
        self.main_frame = Frame(self, bg=self.COULEUR_FOND, bd=3, relief="raised")
        self.main_frame.grid(padx=6, pady=6)

        # Panneau supérieur avec les LEDs (nombre de mines et sigle cours) + smiley
        self.creer_panneau_superieur()

        # Cadre du jeu
        self.creer_cadre_jeu()

        self.ouvrir_partie()

    def creer_menu(self):
        """Crée la barre de menu"""
        menubar = Menu(self)
        self.config(menu=menubar)

        # Menu Partie
        menu_partie = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Partie", menu=menu_partie)
        menu_partie.add_command(label="Nouvelle partie", command=self.nouvelle_partie)
        menu_partie.add_separator()
        menu_partie.add_command(
            label="Débutant (5x5, 5 mines)",
            command=lambda: self.configurer_preset(5, 5, 5),
        )
        menu_partie.add_command(
            label="Intermédiaire (9x9, 10 mines)",
            command=lambda: self.configurer_preset(9, 9, 10),
        )
        menu_partie.add_command(
            label="Expert (16x16, 40 mines)",
            command=lambda: self.configurer_preset(16, 16, 40),
        )
        menu_partie.add_separator()
        menu_partie.add_command(label="Personnaliser...", command=self.configurer)
        menu_partie.add_separator()
        menu_partie.add_command(label="Sauvegarder", command=self.sauvegarder)
        menu_partie.add_command(label="Charger", command=self.charger)
        menu_partie.add_separator()
        menu_partie.add_command(label="Quitter", command=self.quitter)

    def creer_panneau_superieur(self):
        """Crée le panneau avec les LEDs et le smiley"""
        # Cadre du panneau supérieur avec bordure enfoncée
        panneau_frame = Frame(
            self.main_frame, bg=self.COULEUR_FOND, bd=3, relief="sunken"
        )
        panneau_frame.grid(row=0, column=0, padx=6, pady=6, sticky="ew")

        # Conteneur interne pour centrer les éléments
        panneau_inner = Frame(panneau_frame, bg=self.COULEUR_FOND)
        panneau_inner.pack(fill="x", padx=4, pady=4)

        # Compteur de mines (gauche) - style LED
        self.compteur_mines = self.creer_affichage_led(panneau_inner, largeur=52)
        self.compteur_mines.pack(side="left")

        # Bouton smiley (centre)
        self.bouton_smiley = Button(
            panneau_inner,
            text=self.SMILEY_NORMAL,
            font=("Segoe UI Emoji", 16),
            width=2,
            height=1,
            bg=self.COULEUR_FOND,
            activebackground="#A0A0A0",
            relief="raised",
            bd=2,
            command=self.nouvelle_partie,
        )
        self.bouton_smiley.pack(side="left", expand=True)

        # Sigle Cours (droite) - style LED
        self.sigle_cours = self.creer_affichage_led(panneau_inner, "IFT-1004", 102)
        self.sigle_cours.pack(side="right")

    def creer_affichage_led(self, parent, texte_initial="000", largeur=52):
        """Crée un affichage style LED"""
        frame = Frame(parent, bg=self.COULEUR_LED, bd=1, relief="sunken")

        canvas = Canvas(
            frame,
            width=largeur,
            height=30,
            bg=self.COULEUR_LED_FOND,
            highlightthickness=0,
        )
        canvas.pack(padx=1, pady=1)

        # Stocker le canvas pour les mises à jour
        frame.canvas = canvas
        frame.largeur = largeur

        self.afficher_led(frame, texte_initial)

        return frame

    def afficher_led(self, frame, valeur):
        """Affiche une valeur sur l'affichage LED"""
        canvas = frame.canvas
        canvas.delete("all")

        if isinstance(valeur, int):
            # Formater sur 3 chiffres
            texte = f"{valeur:03d}"[:3]
        else:
            texte = str(valeur)

        # Afficher en rouge LED
        canvas.create_text(
            frame.largeur // 2,
            15,
            text=texte,
            font=("Consolas", 20, "bold"),
            fill="#FF0000",
            anchor="center",
        )

        frame.valeur = valeur

    def creer_cadre_jeu(self):
        """Crée le cadre contenant la grille de jeu"""
        # Cadre extérieur avec bordure enfoncée
        cadre_exterieur = Frame(
            self.main_frame, bg=self.COULEUR_FOND, bd=3, relief="sunken"
        )
        cadre_exterieur.grid(row=1, column=0, padx=6, pady=(0, 6))

        self.cadre = Frame(cadre_exterieur, bg=self.COULEUR_FOND)
        self.cadre.grid(padx=0, pady=0)

    def ouvrir_partie(self, dictionnaire_cases=None, activer_jeu=True):
        """Démarre une nouvelle partie"""
        # Nettoyer l'ancienne grille
        for bouton in self.cadre.winfo_children():
            bouton.destroy()

        self.dictionnaire_boutons = {}

        # Créer les boutons de case
        for i in range(self.dimension_rangee):
            for j in range(self.dimension_colonne):
                bouton = BoutonCase(self.cadre, i + 1, j + 1)
                bouton.grid(row=i, column=j, padx=0, pady=0)

                # Style Windows classique
                bouton.configure(
                    font=("Arial", 10, "bold"),
                    width=2,
                    height=2,
                    bg=self.COULEUR_CASE_CACHEE,
                    activebackground=self.COULEUR_CASE_CACHEE,
                    relief="raised",
                    bd=2,
                )

                self.dictionnaire_boutons[(i + 1, j + 1)] = bouton

        # Créer le tableau de jeu
        self.tableau_mines = Tableau(
            self.dimension_rangee, self.dimension_colonne, self.nombre_mines
        )

        if dictionnaire_cases is not None:
            self.tableau_mines.dictionnaire_cases = dictionnaire_cases

        if activer_jeu:
            self.activer_jeu()
        else:
            self.desactiver_jeu()

        # Mettre à jour l'affichage
        self.redessiner()
        self.afficher_led(self.compteur_mines, self.nombre_mines)
        self.bouton_smiley.configure(text=self.SMILEY_NORMAL)

    def redessiner(self):
        """Met à jour l'affichage de toutes les cases"""
        for i in range(1, self.tableau_mines.dimension_rangee + 1):
            for j in range(1, self.tableau_mines.dimension_colonne + 1):
                case = self.tableau_mines.obtenir_case(i, j)
                bouton = self.dictionnaire_boutons[(i, j)]
                apparence = case.obtenir_apparence()

                if case.est_devoilee:
                    # Case dévoilée - effet plat
                    bouton.configure(relief="sunken", bd=1)

                    if case.est_minee:
                        # Mine
                        bouton.configure(
                            text="💣",
                            font=("Arial", 12, "bold"),
                            bg=self.COULEUR_MINE_EXPLOSEE
                            if self.tableau_mines.contient_cases_sans_mines_a_devoiler()
                            else self.COULEUR_CASE_DEVOILEE,
                            highlightbackground=self.COULEUR_MINE_EXPLOSEE
                            if self.tableau_mines.contient_cases_sans_mines_a_devoiler()
                            else self.COULEUR_CASE_DEVOILEE,
                            fg="#000000",
                        )
                    elif apparence == "0":
                        # Case vide
                        bouton.configure(text="", bg=self.COULEUR_CASE_DEVOILEE)
                    else:
                        # Chiffre avec couleur
                        bouton.configure(
                            text=apparence,
                            bg=self.COULEUR_CASE_DEVOILEE,
                            fg=self.COULEURS_CHIFFRES.get(apparence, "#000000"),
                        )
                else:
                    # Case non dévoilée
                    bouton.configure(
                        text="", relief="raised", bd=2, bg=self.COULEUR_CASE_CACHEE
                    )

    def activer_jeu(self):
        """Rend tous les boutons de case cliquables"""
        for bouton in self.dictionnaire_boutons.values():
            bouton.activer(self.devoiler_case)

    def desactiver_jeu(self):
        """Rend tous les boutons de case non-cliquables"""
        for bouton in self.dictionnaire_boutons.values():
            bouton.desactiver()

    def devoiler_case(self, event):
        """Gère le clic sur une case.
        Déclenche un dévoilement en cascade à partir de la case cliquée.

        Args:
            event (Tkinter.event): L'événement de clic, qui contient le bouton cliqué
                en attribut.
        """
        bouton = event.widget
        rangee_x, colonne_y = bouton.rangee_x, bouton.colonne_y

        self.tableau_mines.devoilement_en_cascade(rangee_x, colonne_y)
        self.detecter_fin(rangee_x, colonne_y)
        self.redessiner()

    def detecter_fin(self, rangee_x, colonne_y):
        """
        Détecte la fin de la partie.

        Si la partie est terminée, un message indiquant s'il s'agit d'une victoire
        ou d'une défaite est affiché, puis les cases sont toutes révélées, et le jeu est désactivé.

        Note: Vous pouvez vous inspirer de la classe Partie du mode console pour savoir
        comment détecter la fin de la partie.

        Args:
            rangee_x (int): Numéro de la rangée
            colonne_y (int): Numéro de la colonne
        """
        # TODO: À compléter

    def nouvelle_partie(self):
        """Démarre une nouvelle partie"""
        # TODO: À compléter
        # Aide: Ouvre une partie en utilisant la méthode ouvrir_partie avec les arguments par défaut.

    def configurer_preset(self, rangees, colonnes, mines):
        """Configure une partie avec des paramètres prédéfinis"""
        # TODO: À compléter
        # Aide: Assigne les valeurs reçues en arguments aux bons attributs, puis appelle ouvrir_partie().

    def configurer(self):
        """Ouvre la fenêtre de configuration personnalisée"""
        self.fenetre_configuration = Toplevel(self)
        self.fenetre_configuration.title("Partie personnalisée")
        self.fenetre_configuration.configure(bg=self.COULEUR_FOND)
        self.fenetre_configuration.resizable(False, False)
        self.fenetre_configuration.transient(self)
        self.fenetre_configuration.grab_set()

        # Style
        style_label = {"font": ("Arial", 10), "bg": self.COULEUR_FOND}
        style_entry = {"font": ("Arial", 10), "width": 8, "relief": "sunken", "bd": 2}

        # Contenu
        Label(
            self.fenetre_configuration, text="Nombre de rangées:", **style_label
        ).grid(row=0, column=0, padx=10, pady=5, sticky="e")
        Label(
            self.fenetre_configuration, text="Nombre de colonnes:", **style_label
        ).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        Label(self.fenetre_configuration, text="Nombre de mines:", **style_label).grid(
            row=2, column=0, padx=10, pady=5, sticky="e"
        )

        self.entry_rangee = Entry(self.fenetre_configuration, **style_entry)
        self.entry_colonne = Entry(self.fenetre_configuration, **style_entry)
        self.entry_mines = Entry(self.fenetre_configuration, **style_entry)

        self.entry_rangee.insert(0, str(self.dimension_rangee))
        self.entry_colonne.insert(0, str(self.dimension_colonne))
        self.entry_mines.insert(0, str(self.nombre_mines))

        self.entry_rangee.grid(row=0, column=1, padx=10, pady=5)
        self.entry_colonne.grid(row=1, column=1, padx=10, pady=5)
        self.entry_mines.grid(row=2, column=1, padx=10, pady=5)

        # Boutons
        btn_frame = Frame(self.fenetre_configuration, bg=self.COULEUR_FOND)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15)

        Button(
            btn_frame,
            text="OK",
            width=8,
            command=self.lancer_partie_configuree,
            bg=self.COULEUR_FOND,
            relief="raised",
            bd=2,
        ).pack(side="left", padx=5)

        Button(
            btn_frame,
            text="Annuler",
            width=8,
            command=self.fenetre_configuration.destroy,
            bg=self.COULEUR_FOND,
            relief="raised",
            bd=2,
        ).pack(side="left", padx=5)

    def lancer_partie_configuree(self):
        """Lance une partie avec la configuration personnalisée"""
        try:
            self.dimension_rangee = int(self.entry_rangee.get())
            self.dimension_colonne = int(self.entry_colonne.get())
            self.nombre_mines = int(self.entry_mines.get())

            # Validation
            max_mines = (self.dimension_rangee * self.dimension_colonne) - 1
            if self.nombre_mines > max_mines:
                self.nombre_mines = max_mines
            if self.nombre_mines < 0:
                self.nombre_mines = 0

            self.ouvrir_partie()
            self.fenetre_configuration.destroy()
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")

    def sauvegarder(self):
        """
        Sauvegarde la partie en cours dans un fichier texte nommé 'sauvegarde.txt'.
        Se référer à la méthode charger pour connaître le format attendu.
        """
        texte = ""
        for i in range(1, self.tableau_mines.dimension_rangee + 1):
            for j in range(1, self.tableau_mines.dimension_colonne + 1):
                case = self.tableau_mines.obtenir_case(i, j)
                devoilee = "o" if case.est_devoilee else "n"
                valeur = case.obtenir_apparence(True)
                texte += devoilee + valeur + " "
            texte += "\n"

        with open("sauvegarde.txt", "w", encoding="utf-8") as f:
            f.write(texte)

        messagebox.showinfo("Sauvegarde", "Partie sauvegardée!", parent=self)

    def charger(self):
        """
        Charge une partie sauvegardée. Celle-ci doit être stockée dans un fichier nommé
        'sauvegarde.txt' et doit correspondre au format suivant:

        Dans ce fichier, chaque case doit être représentée par deux caractères,
            - un 'o' si la case est dévoilée, un 'n' sinon
            - un 'M' si la case est minée, sinon un entier de 0 à 8
            représentant le nombre de mines voisines

        Les cases d'une même rangée sont séparées par un espace,
        celles sur des rangées différentes par un retour de ligne.

        Exemple (partie 5x5 où l'on a cliqué aux coordonnées 1,3):
        nM o1 o0 o1 n1
        n2 o2 o1 o2 nM
        nM n2 n1 nM n2
        nM n2 n1 n1 n1
        n1 n1 n0 n0 n0
        """
        try:
            with open("sauvegarde.txt", "r", encoding="utf-8") as f:
                x, y_max, n_mines = 0, 1, 0
                dictionnaire_cases = {}
                jeu_en_cours = False

                for ligne in f:
                    x += 1
                    y = 0
                    rangee = ligne.rstrip().split(" ")
                    for str_case in rangee:
                        if not str_case:
                            continue
                        y += 1
                        y_max = max(y, y_max)
                        case = Case()
                        if str_case[0] == "o":
                            case.devoiler()
                        else:
                            jeu_en_cours = True
                        if str_case[1] == "M":
                            case.ajouter_mine()
                            n_mines += 1
                        else:
                            mines_voisines = int(str_case[1])
                            for _ in range(mines_voisines):
                                case.ajouter_une_mine_voisine()
                        dictionnaire_cases[(x, y)] = case

                self.dimension_rangee = x
                self.dimension_colonne = y_max
                self.nombre_mines = n_mines
                self.ouvrir_partie(dictionnaire_cases, jeu_en_cours)
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Aucune sauvegarde trouvée.")

    def quitter(self):
        """
        Affiche un message de confirmation, et dans l'affirmative, quitte le jeu.
        """
        # TODO: À compléter
        # Aide: Vous aurez besoin de messagebox.askyesno et de self.quit.
