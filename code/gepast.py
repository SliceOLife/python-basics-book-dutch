# Een bedrag gepast betalen met zo min mogelijk euromunten(in eurocenten)

bedrag = input ('Geef een bedrag in: ')

for munt in 200, 100, 50, 20, 10, 5, 2, 1 :
    aantal = 0

    while bedrag >= munt :
        aantal = aantal + 1
        bedrag = bedrag - munt

    if aantal > 0 :
        print str(aantal) + ' x ' + str(munt)c 
