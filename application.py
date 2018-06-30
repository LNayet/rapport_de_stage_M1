from test import *

print("Fichier de référence :", modele)
print("0 : test rejeté")
print("1 : test validé")
print("\n")

print("POUR LE FICHIER :", etudiant)
print("Résultat de la présence de la balise html :", verifier_presence_balise_html())
if verifier_presence_balise_html()==1:
	print("Résultat de la présence de la balise head :",verifier_presence_balise_head())
	if verifier_presence_balise_head()==1:
		print("Résultat de la présence de la balise title :",verifier_presence_balise_title())
		if verifier_presence_balise_title()==1:
			print("Résultat de la comparaison du contenu de title :",valider_title())
	print("Résultat de la présence de la balise body :",verifier_presence_balise_body())
	if verifier_presence_balise_body()==1:
		print("Résultat de la présence de la balise div et du nombre :",verifier_presence_balise_div())
		print("Résultat de la présence de la balise p et du nombre :",verifier_presence_balise_paragraphe())
		print("Résultat de la présence de la balise img et du nombre :",verifier_presence_balise_image())
		if verifier_presence_balise_div()==1:			
			print("Résultat de la comparaison du contenu de div :",verifier_contenu_balise_div_ou_image('div'))
		if verifier_presence_balise_paragraphe()==1:
			print("Résultat de la comparaison du contenu de p :",verifier_contenu_balise_paragraphe())
		if verifier_presence_balise_image()==1:
			print("Résultat de la comparaison du contenu de img :",verifier_contenu_balise_div_ou_image('img'))

