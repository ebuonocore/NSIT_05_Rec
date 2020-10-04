from PIL import Image # Nous allons nous en servir pour accéder aux pixels
import matplotlib.pyplot as plt # Utile ici pour afficher l'image
from urllib.request import urlopen  # Pour ouvrir des images sur Internet

def pixel_blanc(pos:tuple)->bool:
    """ Renvoie True si la moyenne des 3 couleurs du point dépasse 240
    """
    r,v,b = img.getpixel(pos)
    if r+v+b > 720:
        return True
    else:
        return False

def rempli(img:Image,pos:tuple, couleur:tuple):
    """ Prend une image, une position et une couleur en paramètre
        pos[0] = abscisse
        pos[1] = ordonée
        Parcours récursivement l'image depuis pos pour colorier la zone délimitée par des pixels non-blancs
    """
    largeur, hauteur = img.size
    x,y = pos # On récupère les deux données du tuple pos
    if pixel_blanc(pos):
        img.putpixel(pos,couleur) # Comme ce pixel est plutôt blanc, on le colorie en rouge
        if x > 0: # S'il reste au moins un pixel à gauche
            rempli(img,(x-1, y),couleur) # On explore le pixel à gauche
        if x < largeur-1: # S'il reste au moins un pixel à droite
            rempli(img,(x+1, y),couleur) # On explore le pixel à droite  
        if y > 0: # S'il reste au moins un pixel en haut
            rempli(img,(x, y-1),couleur) # On explore le pixel en haut
        if y < hauteur-1: # S'il reste au moins un pixel en bas
            rempli(img,(x, y+1),couleur)  # On explore le pixel en bas
        
# Corps du programme
# On récupère d'abord l'adresse d'une image sur Internet
lien_url = "https://github.com/ebuonocore/NSIT_05_Recursivite/blob/main/e05d_coloriage/camion_2.png?raw=true"
# Ouverture de l'image
img = Image.open(urlopen(lien_url)) # Le fichier image est alors 'mémorisé' dans la variable 'img'

ROUGE = (255,0,0)
BLEU = (50, 50, 240)
GRIS = (60, 60, 60)
rempli(img,(90,80), ROUGE)
rempli(img,(25,80), ROUGE)
rempli(img,(65,50), ROUGE)
rempli(img,(53,50), ROUGE)
rempli(img,(43,50), ROUGE)
rempli(img,(34,50), ROUGE)
rempli(img,(5,5), BLEU)
rempli(img,(5,125), GRIS)
rempli(img,(125,125), GRIS)
plt.imshow(img) # J'affiche l'image qui correspond à la variable 'img'