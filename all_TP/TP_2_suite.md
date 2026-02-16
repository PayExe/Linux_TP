## TP_2 suite (partie 2)
#### Tp by Paolo Antonini / Antoine Mathié


### 1. Prérequis
Pour connecter deux ordinateurs, il faut un câble RJ45 et que les firewalls soient désactivés pour éviter les blocages.

### 2. Câblage
Il suffit de brancher le câble entre les deux PCs. C’est comme relier deux maisons avec une route.


### 3. Création du réseau
Quand on donne une adresse IP à une carte réseau, le réseau existe automatiquement. Pas besoin de créer un réseau, il suffit de configurer les IP.

![Création du réseau](../all_TP_pictures/tp2.2_5.png)


### 4. Modification d’adresse IP
On vérifie avec `ping` si les deux peuvent se parler.

![Modification IP 1](../all_TP_pictures/tp2.2_1.png)
![Modification IP 2](../all_TP_pictures/tp2.2_2.png)

### 5. Utilisation d’un PC comme gateway
Un PC peut partager sa connexion internet avec l’autre. On désactive le WiFi sur un PC, puis on configure l’autre comme passerelle. Ainsi, le PC sans WiFi peut accéder à internet grâce à l’autre.

### 6. Chat privé avec netcat
Netcat permet de discuter entre deux PCs comme un chat très simple. Un PC écoute, l’autre se connecte, et on peut échanger des messages.

![Netcat 1](../all_TP_pictures/tp2.2_3.png)
![Netcat 2](../all_TP_pictures/tp2.2_6.png)
![Netcat 3](../all_TP_pictures/tp2.2_7.png)

### 7. Wireshark
Wireshark sert à voir ce qui se passe sur le réseau, comme observer les messages qui circulent entre les deux PCs.

![Wireshark 1](../all_TP_pictures/tp2.2_8.png)
![Wireshark 2](../all_TP_pictures/tp2.2_9.png)
![Wireshark 3](../all_TP_pictures/tp2.2_10.png)
### 8. Firewall
Le firewall protège le PC, mais il peut bloquer certains échanges. On doit le configurer pour autoriser le ping et netcat sur un port précis.

![Firewall 1](../all_TP_pictures/tp2.2_11.png)
![Firewall 2](../all_TP_pictures/tp2.2_4.png)
