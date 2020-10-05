def couleur_aleatoire():
    """ Renvoie une couleur aleatoire au format (r,v,b)
    """
    import random as rd
    alea = rd.randint(1,255)
    return (alea,alea,alea)

# Corps du programme
# On récupère d'abord l'adresse d'une image sur Internet
lien_url = "https://github.com/ebuonocore/NSIT_05_Recursivite/blob/main/e05d_coloriage/wolf_3.png?raw=true"
# Ouverture de l'image
img = Image.open(urlopen(lien_url)) # Le fichier image est alors 'mémorisé' dans la variable 'img'
largeur, hauteur = img.size # On récupère les dimensions de l'image

for y in range(hauteur):
    for x in range(largeur):
        col = img.getpixel((x,y))
        r, v, b = col[0], col[1], col[2]
        if (r,v,b) == (255,255,255): # Est-ce que ce pixel est blanc?
            col = couleur_aleatoire()
            remplir(img, (x,y), col)

plt.rcParams['figure.figsize']=(8.0, 8.0)
plt.imshow(img) # J'affiche l'image qui correspond à la variable 'img'