###### Aidez MacGyver à s'échapper !
------------------------------------
#### Jeux labyrinthe 2D
------------------------

# Installation [Python3]
------------------------
## Téléchargement :

### Télécharger le fichier : 

https://github.com/Lyss74/1.Aidez_MacGyver_a_Sechapper/archive/master.zip

### Ou cloner le repository :

https://github.com/Lyss74/1.Aidez_MacGyver_a_Sechapper.git

# Installez l'environement virtuel:
    pip install virtualenv

# Crèe l'environement virtuel en tapant:
    cd "cheminDuDossierDeReceptionDuProjet" 

# Exécuter le jeu :
-------------------
# Rendez-vous en tapant dans l'invité de commande 
    cd "C:\Users\Admin\Desktop"

# Ensuite taper 
1.Aidez_MacGyver_a_Sechapper\Scripts\activate

# Vous voilà dans l'environnement virtuel

## Exécuter le fichier pygame_start.py pour lancer le jeu :
### Linux / Mac :
    cd "C:\Users\Admin\Desktop\1.Aidez_MacGyver_a_Sechapper"
    python3 pygame_start.py

### Windows :
    cd "C:\Users\Admin\Desktop\1.Aidez_MacGyver_a_Sechapper"
    python pygame_start.py

# Pour désactiver l'environnement virtuel après avoir terminé de jouer avec "Richard Dean Anderson"
# Taper: 
1.Aidez_MacGyver_a_Sechapper\Scripts\deactivate

# Gameplay :
------------
### Seul le héro bouge à l'aide des touches directionnelles.
### Vous devez trouver les 3 objets permettant d'assembler l'objet qui endormiras le gardien (Automatique).


------------------------------------------FONCTIONNALITES----------------------------------------------


# Il n'y a qu'un seul niveau. 


# La structure départ, emplacement des murs, arrivée, devra être enregistrée dans un fichier pour la modifier facilement
   * 'maze_char.txt'
   and
   * Constants file                                                    / line: 4 - 7 / file: constants.py


# MacGyver sera contrôlé par les touches directionnelles du clavier.
# Le seul élément mouvant est MacGyver. Créez les méthodes de classe qui permettent de l'animer et de trouver la sortie. 
   * Class Player > def event_key()                                       / line: 101 - 133 / file: player.py
   and
   * Constants file                                                  / line: 42 - 43 / file: constants.py


# Les objets seront répartis aléatoirement dans le labyrinthe et changeront d’emplacement si l'utilisateur ferme le jeu.
# Ajoutez un compteur qui les listera.
   * Class Item > def random_pos()                                        / line: 24 - 37 / file: the_maze.py
   and
   * Class Player > def animated_blit()                                      / line: 50 - 63  / file: player.py


# La fenêtre du jeu sera un carré pouvant afficher 15 sprites sur la longueur.
   * Constants file                                                  / line: 34 - 39 / file: constants.py


# MacGyver devra donc se déplacer de case en case, avec 15 cases sur la longueur de la fenêtre !
   * Class Player > def moving()                                          / line: 23 - 28 / file: player.py


# Il récupèrera un objet simplement en se déplaçant dessus.
   * Class Player > Pygame                                                       / line: 34 - 40  / file: player.py


# Le programme sera standalone, c'est-à-dire qu'il pourra être exécuté sur n'importe quel ordinateur.
   * Class ConfigFiles > def cross_sprite().
                                                  / line: 16 - 38 / file: config_pictures_sounds.py


# Le programme s'arrête uniquement si MacGyver a bien récupéré tous les objets et trouvé la sortie du labyrinthe. 
# S'il n'a pas tous les objets et qu'il se présente devant le garde, il meurt.
   * Class Player > def victory_game()                                               / line: 94 / 101 / file: player.py


# Vous respecterez les bonnes pratiques de la PEP 8, PEP 20 et développerez dans un environnement virtuel 


# Votre code devra être écrit en anglais : nom des variables, commentaires, fonctions.

