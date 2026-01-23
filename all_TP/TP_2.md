## B1 Linux - TP2
### I. Exploration locale en solo
#### 1. Affichage d'informations sur la pile TCP/IP locale
__En ligne de commande__
_a) Affichez les infos des cartes réseau de votre PC_

![tp2_1](../all_TP_pictures/tp2_1.png)
 Avec la commande : ipconfig /all
 



| Interface | A-MAC | IP |
| -------- | -------- | -------- |
| Wifi     | B4-B5-B6-77-3D-AD     | 10.33.69.86     |
| Ethernet     | 70-8B-CD-A2-3A-C5     | /     |


_b) Affichez votre gateway_
Voici une commande qui m'affiche directement la passerelle : ipconfig | findstr /i "passerelle Wi-Fi"
ce qui donne : 10.33.79.254

__En graphique (GUI : Graphical User Interface)__
Je vais dans les parametres -> réseau et internet -> Wifi
![tp2_2](../all_TP_pictures/tp2_2.png)

- à quoi sert la gateway dans le réseau d'Ingésup ?
        - le gateway va avoir plusieur role différent il est une sorte de pont vers internet (la porte de sortie) il permet aussi de faire un routage entre réseaux, de sécurisé et filtré des contenus site web ect et surtout de centralisé tout l'acces internet et donc de le gestionner

#### 2. Modifications des informations
_a) Modification d'adresse IP - pt. 1_
- Calcul des ip dispo 
        - donc avec notre adresse ip = 10.33.69.86 et notre Gateway : 10.33.79.254



| 10.33.69.86  | 255.255.240.0   | 
| -------- | -------- |
| 00001010.00100001.01000101.01010110     | 11111111.11111111.11110000.00000000     |

Si on fait le calcul on retrouve :10.33.64.0 = 00001010.00100001.01000000.00000000

En faisant l’ET logique entre l’adresse IP et le masque, on obtient l’adresse de réseau :

Adresse de réseau : 10.33.64.0

Adresse broadcast : 10.33.79.255

Première IP disponible : 10.33.64.1

Dernière IP disponible : 10.33.79.254

- pour le changement d'ip : parametre -> réseaux et internet -> wifi

![tp2_3](../all_TP_pictures/tp2_3.png)

J'ai choisis une ip qui était
libre et remplis les autres infos 

_b)nmap_
J'installe nmap et je tape cette commande qui va scanner le réseau
nmap -sn -PE 10.33.64.0/20
![tp2_4](../all_TP_pictures/tp2_4.png)



_c) Modification d'adresse IP - pt. 2_
On a donc une ip en .120 qui est libre alors je m'y connecte
![tp2_5](../all_TP_pictures/tp2_5.png)
![tp2_6](../all_TP_pictures/tp2_6.png)
![tp2_7](../all_TP_pictures/tp2_7.png)
### On a pu ping alors on va tester sur un navigateur
![tp2_8](../all_TP_pictures/tp2_8.png)
### youtube marche alors c'est bon




### III. Manipulations d'autres outils/protocoles côté client

_1) DHCP_

![tp2_9](../all_TP_pictures/tp2_9.png)
Je remarque que le DHCP n'est pas activé 
Sur le réseau Ingésup, l’attribution des adresses IP est normalement effectuée automatiquement par un serveur DHCP.
Lors de la configuration initiale, une adresse IP a été attribuée dynamiquement par le serveur DHCP du réseau.
Adresse du serveur DHCP : 10.33.79.254
Le DHCP attribue une adresse IP pour une durée limitée appelée bail DHCP. À l’expiration de ce bail, l’ordinateur doit renouveler son adresse IP ou en obtenir une nouvelle.
Dans la configuration actuelle, la carte WiFi est configurée en adresse IP statique, le DHCP est donc désactivé.
Les commandes suivantes permettent de libérer et renouveler une adresse IP via DHCP :


ipconfig /release
ipconfig /renew

![tp2_10](../all_TP_pictures/tp2_10.png)

Windows indique qu’aucune opération ne peut être effectuée.
Cela s’explique par le fait que la carte WiFi est configurée en adresse IP statique et ne dépend donc pas du serveur DHCP à ce moment-là.

La commande ipconfig /release ne fonctionne que lorsque l’adresse IP est attribuée dynamiquement par DHCP.


_2) DNS_

Mon serveur DNS est le suivant : 8.8.8.8

Ensuite je fais faire ceci : nslookup google.com et nslookup ynov.com

![tp2_11](../all_TP_pictures/tp2_11.png)

On remarque que le domaine ynov.com utilise plusieurs adresses IP afin d’assurer la disponibilité du service et la répartition de charge via un service comme Cloudflare.

Pour google on remarque que la réponses est "non autoritaire"  car elle provient d'un serveur DNS intermédiaire.

Maintenant reverse lookup

![tp2_12](../all_TP_pictures/tp2_12.png)
j'ai donc utilisé : nslookup 78.78.21.21
j'ai recu : host-78-78-21-21.mobileonline.telia.com

Le nom de domaine indique qu’il s’agit d’une adresse appartenant à Telia, un fournisseur d’accès Internet.

Le format host-78-78-21-21 montre qu’il s’agit très probablement d’une adresse IP attribuée dynamiquement à un client (connexion mobile ou résidentielle).

ensuite j'ai : nslookup 92.16.54.88
j'ai recu : host-92-16-54-88.as13285.net

Le domaine as13285.net correspond un réseau géré par un opérateur.
Comme pour l’adresse précédente, le nom suggère une IP client.