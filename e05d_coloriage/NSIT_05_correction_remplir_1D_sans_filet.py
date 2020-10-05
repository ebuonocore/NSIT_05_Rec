def remplir_1D(ma_liste, abscisse):
    if ma_liste[abscisse] == 0: # Si le point est blanc
        ma_liste[abscisse] = 2 # Je change la couleur
        remplir_1D(ma_liste, abscisse - 1) # On poursuit l'exploration par la gauche
        remplir_1D(ma_liste, abscisse + 1) # On poursuit l'exploration par la droite
        
liste_pixels = [1, 0, 0 , 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
remplir_1D(liste_pixels, 9) # On lance le remplissage depuis la graine
liste_pixels