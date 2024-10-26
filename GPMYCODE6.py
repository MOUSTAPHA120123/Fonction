def calculatrice():
    # Saisie du premier nombre
    nombre1 = float(input("Entrez le premier chiffre : "))

    # Saisie du second nombre
    nombre2 = float(input("Entrez le deuxième chiffre : "))

    # Saisie de l'opérateur
    operateur = input("Entrez l'opérateur (+, -, *, /) : ")

    # Calcul selon l'opérateur choisi
    if operateur == "+":
        resultat = nombre1 + nombre2
    elif operateur == "-":
        resultat = nombre1 - nombre2
    elif operateur == "*":
        resultat = nombre1 * nombre2
    elif operateur == "/":
        if nombre2 != 0:  # Vérification pour éviter la division par zéro
            resultat = nombre1 / nombre2
        else:
            return "Erreur : Division par zéro."
    else:
        return "Erreur : Opérateur invalide."

    return f"Le résultat est : {resultat}"

# Appel de la fonction
print(calculatrice())