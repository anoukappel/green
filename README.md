# Green
Tegenwoordig kiezen steeds meer huishoudens voor zonnepanelen. Door gebruik te maken van batterijen kan de energie die niet nodig is op de momenten dat het wordt opgewekt worden opgeslagen voor gebruik op momenten dat de consumptie hoger is dan de productie.

Om batterijen te kunnen gebruiken voor meerdere huizen, moeten er kabels gelegd worden.
Hoe minder kabels er gelegd worden hoe lager de kosten zijn. Er moet wel rekening gehouden worden met de maximale capaciteit van de batterij
en elk huis moet verbonden worden.

# Aan de slag

## De algoritmes
We hebben vier algoritmes geimplementeerd in de code om een tot een geldige oplossing te komen.
Een geldige oplossing betekend dat elk huis een connectie heeft met een batterij en dat de capaciteit van de
batterijen niet overschreden gaat worden.
Onze algoritmes focussen zich op de volgorde van huizen connecten met de dichtbijzijnde batterij.
Hierbij nemen we altijd de snelste route naar een batterij of een andere kabel.

##### Random + Greedy
Het random component zit in het selecteren van de huizen, het greedy element zit hem in dat wij telkens het huis verbinden met de dichtstbijzijnde beschikbare batterij of aan een stuk kabel dat al neergelegd is.

##### Housecounter
Dit algoritme verdeeld de grid over 25 blokken en probeerd dan zolang de batterij capaciteit het toelaat het
hele blok aan dezelfde batterij te koppelen. Hij begint de huizen te koppelen per blok en begint bij het blok
waar de meeste huizen in staan. Huizen die niet aan deze batterij gekoppeld kunnen worden, worden als laatste
op een random volgorde aan batterijen gekoppeld.

#### Hillclimber
Dit algoritme neemt als input een geldige oplossing verkregen uit de oplossing van random+greedy of housecounter. En verwisselt steeds 2 of meerdere huizen van batterij per iteratie. Wanneer de oplossing verbeterd (lees de totale kosten worden verlaagd), dan wordt deze oplossing
opgeslagen en gebruikt in de volgende iteratie.

#### Simulatedannealing
Dit algoritme lijkt veel op hillclimber, maar er zijn verschillen. Zo begint SA ook met een al eerder verkregen oplossing van random+greedy of housecounter. Vervolgens verwisseld het ook steeds twee huizen en kijkt of de oplossing geldig is. Als de nieuwe oplossing een verbetering is dan wordt dit het nieuwe model. Als het geen verbetering is, kan de nieuwe oplossing worden aangenomen. Of dit gebeurd is afhankelijk van de temperatuur.
Als de temperatuur hoog is dan is de kans dat een slechte verandering wordt aangenomen groot. Als de temperatuur laag is, is deze kans juist heel laag. De temperatuur zal steeds verder zakken naarmate het algoritme aan de gang is. Hierdoor zal naarmate het algoritme bezig is steeds minder slechte veranderingen worden aangenomen. Hierdoor kom je uiteindelijk op een zo laag mogelijk aantal kabels uit.

## Vereisten
De code is volledig geschreven in Python 3.7.  Verder zijn er geen packages nodig om de code succesvol te draaien.

## Gebruik
Een voorbeeld kan gerund worden door aanroepen van:
```
python main.py
```
Dan wordt het random algoritme gerund en van de beste oplossing uit 1000 iteraties worden meerder plots opgeslagen in de
experiments/random_experiment map, district 1 wordt nu standaard gebruikt om de oplossing te berekenen.
De wijk aanpassen kan door in main.py de variabele op regel 17 aan te passen naar 1, 2 of 3.


Om de andere twee algoritmes te runnen moeten de parameters ingevuld worden in main.py en de juiste regels uncomment worden.
Bij het runnen van bijvoorbeeld de hillclimber_experiment moeten de volgende regels uncomment worden.
```
number_of_runs = 20
houses_to_switch = 1
iterations = 2000
random_runs = 10
```
In combinatie met Random en Greedy, moet onderstaande regel uncommend worden:
```
hillclimber_experiment.multiple_runs(district_test, number_of_runs, houses_to_switch, iterations, random_runs)
```
In combinatie met Housecounte, moet onderstaande regel uncommend worden:
```
hillclimber_experiment.house_counter_hillclimb(district_test, number_of_runs,  houses_to_switch, iterations)
```
Alle andere code die onder de algoritmes staan moeten worden gecomment.
Het runnen van de simulated annealing algoritme werkt op een soortegelijke manier:
```
number_of_runs = 1
houses_to_switch = 1
iterations = 1000
start_temp = 50
raise_temp = 20
random_runs = 10
```
In combinatie met Random + Greedy, moet onderstaande regel uncommend worden:
```
simulatedannealing_experiment.random_simulated_an(district, random_runs, number_of_runs, houses_to_switch, iterations, start_temp, raise_temp)
```
In combinatie met Housecounter, moet onderstaande regel uncommend worden:
```
simulatedannealing_experiment.house_counter_simulated_an(district_test, number_of_runs, houses_to_switch, iterations, start_temp, raise_temp)
```
De plots worden opgelagen met een naam die aangeeft hoeveel iteraties er gedaan zijn en welk algoritme is gebruikt.
Wanneer twee dezelfde experimenten zijn uitgevoerd worden de laatste geproduceerde resultaten opgeslagen.

## Structuur

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de vier benodigde classes voor deze case
  - **/code/visualisation**: bevat de code voor het maken van de visualisaties van deze case
  - **/code/solutions**: bevat de code voor het opslaan van de oplossing als een json bestand
  - **/code/experiments**: bevat de code voor het uitvoeren van de experimenten en de plots die hieruit voorkwamen
- **/data**: bevat de verschillende databestanden die nodig zijn om het district te vullen en oplossingen te genereren

## Auteurs
- Anouk Appel
- Brenda Bax
- Isabelle van Leeuwen
