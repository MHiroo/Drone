# Drone

hdmi_drive=2

Config.txt se trouve dans /boot et je l'ai édité en chargeant LXTerminal et en utilisant la ligne de commande suivante :

$ sudo nano /boot/config.txt

Après avoir ajouté la ligne "hdmi_drive=2" en bas, J'ai tapé ctrl-o pour écrire les modifications et ctrl-x pour quitter l'éditeur de texte nano. J'ai redémarré et le son HDMI a finalement fonctionné !
