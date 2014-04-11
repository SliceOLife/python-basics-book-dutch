# Variabel types

Computers zijn geavanceerd en kunnen gebruiken maken van meer complexere variabelen dan alleen getallen. Dit is waar variabel types in het spel komen. Variabelen komen in verschillende types en verschillende talen ondersteunen verschillende types.

De meest voorkomende types zijn:

* **Getallen**
    * **Float**: een getal, zoals 1.21323, 4, 100004 or 0.123
    * **Integer**: een natuurlijk(heel) getal zoals 1, 12, 33, 140 maar niet 1.233

* **String**: een regel tekst zoals "boot", "olifant" of "kijk, tekst!"

* **Boolean**: alleen true(waar) of false(onwaar), maar niets anders

* **Arrays**: een collectie van waardes zoals: 1,2,3,4,'Goh, wat saai'

Python is een *"dynamic and strongly typed"* taal, dit betekent dat je niet expliciet hoeft aan te geven wat voor type je variabelen zijn. De interpreter bepaalt gelukkig zelf wat voor type de variabele moet zijn aan de hand van de waarde die je er aan geeft.

Waardes converteren kan worden gedaan met de str en int functies zoals hieronder:

```python
x = 5 # type integer
y = 6 # type integer
resultaat = x + y # type integer
tekst = str(resultaat) # type string

test2 = "27" # type string
getal2 = int(test2) # type getal
```
