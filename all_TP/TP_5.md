# TP5 : pfSense – Bases d’un pare-feu

## Partie 1 – Prise en main et sécurisation

### 1. Accès à l’interface
Connectez-vous à l’interface web de pfSense.

**Questions :**
- Quelle est l’adresse IP du LAN ?
  > 192.168.56.99
- Quelle est l’adresse IP du WAN ?
  > 10.0.2.15
- Pourquoi utilise-t-on HTTPS ?
  > Pour sécuriser les échanges entre l'utilisateur et l'interface du pare-feu, en chiffrant les données transmises pour protéger les utilisateurs.
- Pourquoi faut-il changer les identifiants par défaut sur un pare-feu ?
  > Sinon tout le monde y a accès.

### 2. Sécurisation de l’accès administrateur
Modifiez les paramètres du compte administrateur.

**Questions :**
- Où se gèrent les utilisateurs ?
  > System/User Manager/Users
- Qu’est-ce qu’un mot de passe robuste ?
  > Un mot de passe robuste est assez long, complexe, avec des caractères spéciaux et unique qu'on utilise une seule fois.
- Pourquoi sécuriser en priorité l’accès admin sur un équipement réseau ?
  > Car l'admin a accès à tout, y compris les pare-feu.

---

## Partie 2 – Comprendre les interfaces réseau

### 3. Vérification des interfaces
Vérifiez l’affectation WAN / LAN.

**Questions :**
- Quelle interface permet l’accès Internet ?
  > le WAN
- Quelle interface correspond au réseau interne ?
  > le LAN
- Que se passerait-il si les interfaces étaient inversées ?
  > Le réseau interne serait exposé directement à Internet, ce qui annulerait la protection du pare-feu.

---

## Partie 3 – Configuration des services réseau

### 4. DHCP
Configurez le serveur DHCP pour le réseau LAN.

**Questions :**
- Pourquoi utiliser DHCP plutôt qu’une IP fixe ?
  > Le DHCP permet d'attribuer automatiquement des adresses IP aux appareils du réseau. C'est plus pratique pour les réseaux avec beaucoup d'appareils ou des connexions temporaires.
- Quelle plage d’adresses choisir ?
  > Il faut choisir une plage d'adresses correspondant au sous-réseau du LAN, par exemple 192.168.56.100 à 192.168.56.200 si le LAN est en 192.168.56.0/24.
- Quelles adresses faut-il éviter d’inclure dans la plage ?
  > Il faut éviter d'inclure l'adresse du pare-feu, les adresses réservées à des serveurs ou à des équipements configurés en IP fixe, ainsi que l'adresse de broadcast du réseau.

**Vérification :**
Ubuntu obtient-elle automatiquement une adresse IP ?
> Je l'ai récupérée avec "ip a"

![Capture d'écran](../all_TP_pictures/tp5_1.png)

### 5. DNS
Activez et configurez le résolveur DNS.

![Capture d'écran](../all_TP_pictures/tp5_3.png)

**Questions :**
- Pourquoi un pare-feu peut-il jouer le rôle de serveur DNS ?
  > Un pare-feu peut jouer le rôle de serveur DNS pour centraliser la résolution des noms dans le réseau local, filtrer les requêtes DNS et améliorer la sécurité en contrôlant les domaines accessibles.
- Que se passe-t-il si le DNS ne fonctionne pas mais que le ping vers 8.8.8.8 fonctionne ?
  > Cela signifie que la connexion Internet fonctionne, mais la résolution des noms de domaine ne fonctionne pas. On peut accéder aux sites via leur adresse IP, mais pas via leur nom.

---

## Partie 4 – Autoriser l’accès Internet

### 6. Règles de pare-feu
Configurez les règles nécessaires pour permettre aux machines du LAN d’accéder à Internet.

info : pfSense applique les règles de haut en bas.

![Capture d'écran](../all_TP_pictures/tp5_4.png)

**Questions :**
- Quelle doit être la source ?
  > le LAN
- Quelle doit être la destination ?
  > Any
- Faut-il autoriser tous les protocoles ?
  > Non, il vaut mieux privilégier les protocoles vraiment nécessaires.

**Tests :**
- Ping vers pfSense
- Ping vers 8.8.8.8
- Test DNS
- Accès web

Si ça ne fonctionne pas :
Où regarder ? (Logs ? NAT ? Règles ?)

### 7. NAT
Vérifiez la configuration du NAT sortant.

![Capture d'écran](../all_TP_pictures/tp5_5.png)

**Questions :**
- Pourquoi le NAT est-il nécessaire avec une interface WAN en NAT ?
  > Les IP privées LAN ne sont pas routables sur Internet.
- Quelle est la différence entre NAT automatique et manuel ?
  > Automatique = pfSense gère tout, Manuel = admin configure chaque règle.
- Comment vérifier qu’une traduction d’adresse a lieu ?
  > Ping IP publique et comparer avec les logs NAT.

---

## Partie 5 – Filtrage

### 8. Blocage d’un site spécifique
Bloquez l’accès à un site web de votre choix.

![Capture d'écran](../all_TP_pictures/tp5_6.png)

**Questions :**
- Faut-il bloquer par IP ou par nom de domaine ?
  > Par nom de domaine (plus efficace).
- Que se passe-t-il si le site utilise HTTPS ?
  > Le blocage par nom de domaine peut être contourné si le site utilise HTTPS.
- Pourquoi le blocage par IP peut-il être contourné ?
  > Car les sites peuvent changer d'IP ou utiliser des CDN.

Testez et observez les logs.

### 9. Blocage d’une catégorie de sites (jeux d’argent)
Créez une solution propre et maintenable pour bloquer plusieurs sites.

tips : réfléchissez à l’intérêt des alias.

**Questions :**
- Pourquoi ne pas créer une règle par site ?
  > Maintenance difficile.
- Où se créent les alias ?
  > On va dans Firewall/Aliases/Add.
- Comment vérifier qu’une règle bloque réellement le trafic ?
  > Vérifier les logs pfSense.

---

## Partie 6 – Aller plus loin (partie plus tendue)

### 10. Blocage par catégorie (réseaux sociaux)
Créez un alias pour une nouvelle catégorie.
Implémentez une règle.
Analysez les logs.

![Capture d'écran](../all_TP_pictures/tp5_7.png)

**Question :**
- Que se passe-t-il si la règle est placée sous une règle "Pass Any" ?
  > La règle de blocage est ignorée car pfSense lit les règles de haut en bas.

### 11. Règles horaires
Créez un horaire.
Appliquez-le à une règle existante.

![Capture d'écran](../all_TP_pictures/tp5_8.png)

**Questions :**
- Pourquoi les règles horaires sont-elles utiles en entreprise ?
  > Ça permet de contrôler l'accès à certaines heures pour éviter de se connecter en dehors des heures de travail par exemple.

### 12. Serveur web local
Installez un serveur web sur Ubuntu.

Objectifs :
- Autoriser un accès spécifique
- Bloquer les autres

![Capture d'écran](../all_TP_pictures/tp5_9.png)

**Questions :**
- Filtrer par IP source ?
  > On autorise ou bloque selon l’adresse IP de la machine qui fait la demande.
- Filtrer par port ?
  > On autorise seulement le port utilisé par le service (ex : port 80 ou 443 pour un site web).
- Pourquoi le pare-feu protège-t-il le LAN même en réseau interne ?
  > Parce qu’un appareil du LAN peut être infecté ou malveillant.

### 13. Logs et analyse
Activez la journalisation sur certaines règles.

**Questions :**
- Différence entre paquet bloqué et autorisé
  > Un paquet bloqué ne passe pas, un paquet autorisé passe.
- Identifier quelle règle a déclenché le blocage
  > En regardant les logs.
- Comprendre le sens du trafic
  > Source/destination, protocole, port.

### 15. Filtrage MAC
Testez le filtrage par adresse MAC.

**Questions :**
- Le filtrage MAC est-il réellement sécurisé ?
  > Non, il est peu sécurisé.
- Pourquoi est-il facilement contournable ?
  > Car le MAC est spoofable.

### 16. Portail captif
Implémentez un portail captif.

![Capture d'écran](../all_TP_pictures/tp5_10.png)

**Questions :**
- Dans quels contextes utilise-t-on cela ?
  > Utilisation comme Wi-Fi invité, hôtels, écoles.
- Quelle(s) avantage(s) avec une simple règle de pare-feu ?
  > Authentification centralisée + journalisation.

### 17. Sauvegarde / restauration
Sauvegardez la configuration.
Modifiez-la.
Restaurez-la.

![Capture d'écran](../all_TP_pictures/tp5_11.png)

**Question :**
- Pourquoi la sauvegarde régulière est-elle essentielle en production ?
  > La sauvegarde est essentielle, elle permet une restauration rapide en cas de problème et réduit le downtime.