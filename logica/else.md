# Else & Elif

Er is ook een `else` clausule die gebruikt wordt telkens dat de eerste conditie niet waar is. Dit is een handig hulpmiddel als je overal op wilt reageren maar een aparte handeling wilt uitvoeren voor één ding:

```python
land = 'Engeland'

if land == 'England':
    parapluNodig = True
else:
    parapluNodig = False
```

De `else` clausule kan ook worden samengevoegd met nog een `if`, zoals deze versie van het vorige onderdeel:

```python
land = 'Engeland'

if land == 'England':
    # etc
elif land == 'France':
    # etc
elif land == 'Germany':
    # etc
```
