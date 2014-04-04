# If conditie

De makkelijkste conditie is een if statement en de syntax is `if condition: do this`. De conditie moet waar zijn om de code na de dubbelepunt uit te voeren. Je kunt bijvoorbeeld een string testen en de waarde van een andere string aanpassen afhankelijk van de conditie:

```python
land = 'Frankrijk'

if land == 'Engeland':
    weer = 'bagger'
    eten = 'vullend'
    valuta = 'pound sterling'

if land == 'Frankrijk':
    weer = 'lekker'
    eten = 'culinair'
    valuta = 'euro'

if land == 'Duitsland':
    weer = 'matig'
    eten = 'braadworst!'
    valuta = 'euro'
}

bericht = 'Dit is ' + land + ', het weer is ' +
            weer + ', het eten is ' + eten + ' en de ' +
            'valuta is ' + valuta
```

**Opmerking:** Conditions kunnen ook ineensluitend zijn.
