def remplir_1D_mieux(ma_liste:list, abscisse:int):
    if ma_liste[abscisse] == 0: # Si le point est blanc
        ma_liste[abscisse] = 2 # Je change la couleur
        if abscisse - 1 >= 0:
            remplir_1D_mieux(ma_liste, abscisse - 1) # On poursuit l'exploration par la gauche
        if abscisse + 1 < len(ma_liste):
            remplir_1D_mieux(ma_liste, abscisse + 1) # On poursuit l'exploration par la droite
        
liste_pixels2 = [0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
remplir_1D_mieux(liste_pixels2, 16) # On lance le remplissage depuis la graine
print(liste_pixels2)
