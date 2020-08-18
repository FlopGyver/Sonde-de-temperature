******Sonde de température******
--------VALLET Florian----------
___________18/08/2020___________

1°) Placer les fichiers "lecteur.py" et "alert.py" dans /home/pi

	- Saisir la commande "$ sudo crontab -e" pour enclencher une routine :
		
		-Ajouter à la fin du fichier les deux lignes suivante :
	
		"*/1 * * * * sudo python /home/pi/lecteur.py" (toutes les minutes)

		"*/30 * * * * sudo python /home/pi/alert.py" (toutes les demis heures)

2°) Placer le dossier "température" dans /var/www/html

3°) Se connecter à l'interface Web

Enjoy !
