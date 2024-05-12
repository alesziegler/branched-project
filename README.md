# a-ziegler-test-project-python
Project for obtaining ITNetwork Python certificate.

Nahrán projekt v betaverzi, která myslím splňuje základní zadání, ale nejsem s ní spokojen a ještě bych ji chtěl dopracovat.

Princip je, že je uživatel zadává jména pojištěných jako hodnoty do slovníku, 
jehož keys jsou jméno (sloučené křestní+příjmení, jelikož mi nedává smysl je oddělovat), věk a telefon.

Validace je 
0) prázdný input to nevezme,

1) pro jméno:
1a) křestní i příjmení musejí obsahovat jen písmena české abecedy, bez mezer,
1b)křestní i příjmení musejí začínat velkým písmenem,
1c) kromě prvních písmen musejí být všechna další písmena malá.

2)pro věk - celé číslo nejméně 18,

3) pro telefon
3a) přesně 9 znaků,
3b) jen číslice.

Co tam chybí:

	- dokumentace/komentáře jsou útržkovité a nehotové (jsou všechny v angličtině, doufám, že to nevadí?).

	- konzolové výstupy vypadají velmi vidlácky, pokusim se vylepšit formátování
(internety mi napovídají, ať si k tomu stáhnu nějaký modul, což ale tady asi nejde, počítám)

	- nelíbí se mi stupidně repetitivní kód zajišťující interakci mezi uživatelským rozhraním a settery Customer class provádějícími validaci.
Metoda, kterou jsem si k tomu napsal, bohužel nefunguje a nevím proč; ještě se ji pokusím zprovoznit.


