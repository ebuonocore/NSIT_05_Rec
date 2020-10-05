from PIL import Image # Nous allons nous en servir pour accéder aux pixels
import matplotlib.pyplot as plt # Utile ici pour afficher l'image
from urllib.request import urlopen  # Pour ouvrir des images sur Internet

def remplir(img:Image,pos:tuple, couleur:tuple):
    """ Prend une image, une position et une couleur en paramètre
        pos[0] = abscisse
        pos[1] = ordonée
        Parcours récursivement l'image depuis pos pour colorier la zone délimitée par des pixels non-blancs
    """
    largeur, hauteur = img.size
    x,y = pos # On récupère les deux données du tuple pos
    if img.getpixel(pos) == (255,255,255):
        img.putpixel(pos,couleur) # Comme ce pixel est plutôt blanc, on le colorie en rouge
        if x > 0: # S'il reste au moins un pixel à gauche
            remplir(img,(x-1, y),couleur) # On explore le pixel à gauche
        if x < largeur-1: # S'il reste au moins un pixel à droite
            remplir(img,(x+1, y),couleur) # On explore le pixel à droite  
        if y > 0: # S'il reste au moins un pixel en haut
            remplir(img,(x, y-1),couleur) # On explore le pixel en haut
        if y < hauteur-1: # S'il reste au moins un pixel en bas
            remplir(img,(x, y+1),couleur)  # On explore le pixel en bas
        
# Corps du programme
# On récupère d'abord l'adresse d'une image sur Internet
lien_url = "https://github.com/ebuonocore/NSIT_05_Recursivite/blob/main/e05d_coloriage/camion_4.png?raw=true"
# Ouverture de l'image
img = Image.open(urlopen(lien_url)) # Le fichier image est alors 'mémorisé' dans la variable 'img'

ROUGE = (255,0,0)
BLEU = (50, 50, 240)
GRIS = (60, 60, 60)
JAUNE = (240,150,0)
remplir(img,(180,150), ROUGE)
remplir(img,(70,95), ROUGE)
remplir(img,(90,95), ROUGE)
remplir(img,(110,95), ROUGE)
remplir(img,(175,47), JAUNE)
remplir(img,(164,50), JAUNE)
plt.rcParams['figure.figsize']=(10.0, 5.0)
plt.imshow(img) # J'affiche l'image qui correspond à la variable 'img'