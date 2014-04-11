# Uitleg

Is het je niet gelukt om de opdracht succesvol te maken? Volgende keer beter!

De volledige code kun je hieronder vinden:

```python
# Een bedrag gepast betalen met zo min mogelijk euromunten(in eurocenten)

bedrag = input ('Geef een bedrag in: ')

for munt in 200, 100, 50, 20, 10, 5, 2, 1 :
    aantal = 0

    while bedrag >= munt :
        aantal = aantal + 1
        bedrag = bedrag - munt

    if aantal > 0 :
        print str(aantal) + ' x ' + str(munt) # getallen converteren naar het type string met de str functie!
```
We vragen allereerst de gebruiker om een getal met de input functie.

Hierna doen wij een for loop over alle waarden in eurocent(2 euro is 200 eurocent, enz)

In onze while loop kijken we of het bedrag gelijk aan over meer dan de munt is en voeg dan 1 aan het aantal toe en trekken munt van het bedrag af.

Als het uiteindelijke aantal benodigde munten meer dan 0 is printen we naar het scherm hoeveel munten we nodig hebben!
