import csv

def kopa_csv(pirmaiscsv, otraiscsv):
    with open(pirmaiscsv, 'r' ,encoding="utf-8") as fails:
        lasit_csv = csv.reader(fails)
        saturs=[]
        for rinda in lasit_csv:
            saturs.append(rinda)

    with open(pirmaiscsv, 'r' ,encoding="utf-8") as fails:
        lasit_csv = csv.reader(fails)
        saturs_otraja=[]
        for rinda in lasit_csv:
            saturs_otraja.append(rinda)

    if len(saturs) == len(saturs_otraja):
        with open('divka.csv', 'w',encoding="utf-8",newline='') as fails:
            csvwrite=csv.writer(fails)
            csvwrite.writerows(saturs)
            csvwrite.writerows(saturs_otraja)
    unikalie=[]

    for unik in saturs:
        if unik not in saturs_otraja:
            unikalie.append(unik)

    print(unikalie)

kopa_csv("pirmais.csv","otrais.csv")