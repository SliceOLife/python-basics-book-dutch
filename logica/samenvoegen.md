# Meerdere condities

Je kunt meerdere condities samenvoegen met "or" of "and" statements, om te testen of een van de twee of beide waar zijn.

Laten we zeggen dat je wilt testen of de waarde van x tussen de 10 en 20 ligt kun je dat als volgt doen:

```
if x > 10 and x < 20:
    ...
```

Als je zeker wilt weten dat land of "Engeland" of "Duitsland" is doe je dit:

```
if land == 'England' or land == 'Germany': {
    ...
```

**Opmerking**: Net als bewerkingen op getallen, kunnen condities gegroepeerd worden, bijv: ```if naam == "John" or naam == "Lisa" and land == "Frankrijk":```
