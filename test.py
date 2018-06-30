from bs4 import BeautifulSoup

def charger_fichier_html(source):
	fichier = open(source,"r")
	chaine = fichier.read()
	fichier.close()
	return chaine

def verifier_presence_balise_html():
	if soupetudiant.html is None: return 0
	return 1

def verifier_presence_balise_head():
	if soupetudiant.html.head is None: return 0
	return 1

def verifier_presence_balise_title():
	if soupetudiant.html.head.title is None: return 0
	return 1

def valider_title():
	if soupmodele.html.head.title==soupetudiant.html.head.title: return 1
	return 0

def verifier_presence_balise_body():
	if soupetudiant.html.body is None: return 0
	return 1
	
def verifier_presence_balise_div():
	cpt_etudiant=0
	cpt_modele=0
	for div in soupmodele.html.body.find_all('div'):
		cpt_modele+=1
	for div in soupetudiant.html.body.find_all('div'):
		cpt_etudiant+=1
	if cpt_etudiant>=cpt_modele and cpt_etudiant!=0: return 1
	return 0

def verifier_presence_balise_paragraphe():
	cpt_etudiant=0
	cpt_modele=0
	for div in soupmodele.html.body.find_all('p'):
		cpt_modele+=1
	for div in soupetudiant.html.body.find_all('p'):
		cpt_etudiant+=1
	if cpt_etudiant>=cpt_modele and cpt_etudiant!=0: return 1
	return 0

def verifier_presence_balise_image():
	cpt_etudiant=0
	cpt_modele=0
	for img in soupmodele.html.body.find_all('img'):
		cpt_modele+=1
	for img in soupetudiant.html.body.find_all('img'):
		cpt_etudiant+=1
	if cpt_etudiant>=cpt_modele and cpt_etudiant!=0: return 1
	return 0

def verifier_contenu_balise_div_ou_image(balise):
	liste_modele=[]
	liste_etudiant=[]
	i=0
	j=0
	k=0
	t=0
	validator=0
	for b in soupmodele.html.body.find_all(balise):
		liste_modele.append(b)
		j+=1
	for b in soupetudiant.html.body.find_all(balise):
		liste_etudiant.append(b)
		t+=1		
	while i<j: 
		if liste_modele[i]!=liste_etudiant[i]: #on compare le contenu des deux listes, on s'arrête si c'est différent		
			break
		i+=1
	if i==j: return 1 #on retourne 1 si i vaut j : les balises correspondent !
	else: 	
		while(k<t):
			i=0
			while(i<j): #on cherche si les balises sont dans le désordre
				if liste_etudiant[k]==liste_modele[i]: #si on trouve une balise au contenu identique à l'autre quelque part, on sort de la boucle 
					validator+=1
					break
				i+=1
			k+=1
		if validator==j: return 1 #on retourne 1  si validator vaut j : cela veut dire que tout a été retrouvé sur le fichier étudiant
		return 0

def verifier_contenu_balise_paragraphe():
	liste_modele=[]
	liste_etudiant=[]
	i=0
	j=0
	k=0
	t=0
	validator=0
	for b in soupmodele.html.body.find_all('p'):
		liste_modele.append(b.string)
		j+=1
	for b in soupetudiant.html.body.find_all('p'):
		liste_etudiant.append(b.string)	
		t+=1	
	while i<j: 
		if liste_modele[i]!=liste_etudiant[i]: #on compare le contenu des deux listes, on s'arrête si c'est différent		
			break
		i+=1
	if i==j: return 1 #on retourne 1 si i vaut j : les balises correspondent !
	else: 	
		while(k<t):
			i=0
			while(i<j): #on cherche si les balises sont dans le désordre
				if liste_etudiant[k]==liste_modele[i]: #si on trouve une balise au contenu identique à l'autre quelque part, on sort de la boucle 
					validator+=1
					break
				i+=1
			k+=1
		if validator==j: return 1 #on retourne 1  si validator vaut j : cela veut dire que tout a été retrouvé sur le fichier étudiant
		return 0

etudiant="etudiant2.html"
modele="modele.html"
html_modele = charger_fichier_html(modele)
html_etudiant = charger_fichier_html(etudiant)
soupmodele = BeautifulSoup(html_modele,"lxml")
soupetudiant = BeautifulSoup(html_etudiant,"lxml")
