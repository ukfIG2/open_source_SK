import pandas as pd
try:
    poradie = ["1.","2.","3.","4.","5.","6.","7."]
    strany = ["SMER","REPUBLIKA","OLANO","SAS","SME-RODINA","Progresivci","Hlas"]
    vyherne_strany = ["Hlas", "Progresivci", "SAS", "SMER", "Republika", "Sme-rodina", "Olano"]
    hlasy = [0,0,0,0,0,0,0]
    falosne_hlasy = []
    realne_strany = []
    realne_hlasy = []
    realne_hlasovanie = [0,0,0,0,0,0,0]
    xxx = ["xxx", "xxx", "xxx", "xxx", "xxx", "xxx", "xxx"]

    #Nazbierame počet hlasov pre konkrétnu stranu.
    for i in range(len(strany)):
        hlasy[i] = int(input("Zadaj pocet hlasov pre stranu "+ strany[i]+": "))

    #Zoradíme zoznam "falosne_hlasy" od najvyššej hodnoty po najmenšiu.
    falosne_hlasy = sorted(hlasy, reverse=True)

    #Falošným výsledkom priradíme reálne počty hlasov.
    realne_hlasovanie[0]=hlasy[6]
    realne_hlasovanie[1]=hlasy[5]
    realne_hlasovanie[2]=hlasy[3]
    realne_hlasovanie[3]=hlasy[0]
    realne_hlasovanie[4]=hlasy[1]
    realne_hlasovanie[5]=hlasy[4]
    realne_hlasovanie[6]=hlasy[2]

    #Vypočítame celkový počet hlasov.
    hlasovalo = sum(realne_hlasovanie)

    #Zoradíme  strany podľa počtu nazbieraných hlasov od najviac po najmenej.
    for i in range(len(strany)):
        a = hlasy.index(max(hlasy))
        realne_strany.append(strany[a])
        realne_hlasy.append(hlasy[a])
        strany.pop(a)
        hlasy.pop(a)    

    #Vytvoríme tabuľku, aby to bolo prehladnejšie.
    tabulka = pd.DataFrame({"Falošné poradie strán":vyherne_strany, "Zfalšované počty hlasov":falosne_hlasy, "Reálne hlasovanie zfalšovaného hlasovania":realne_hlasovanie, "xxx":xxx, "Realné poradie":realne_strany, "Realne hlasy":realne_hlasy})
    print()     #Odriadkovanie
    print(tabulka.to_string())
    print()     #Odriadkovanie
    print("4 377 565 je počet voličov z referenda 2023. Voľby do NRSR 2020 bolo 4 432 419.")
    if hlasovalo>4377565:       #Ak ste zadali viac ako 4 377 565 hlasov tak percentá sú zbytočné. 
        print("Dali ste vačší počet hlasov ako 4 377 565. Dali ste "+str(hlasovalo)+" hlasov.")
    else:                       #Percento hlasovania z celkových voličov z referenda 2023.
        print("Hlasovalo "+str(hlasovalo)+" z 4 377 565. "+str(round(((hlasovalo/4377565)*100),2))+"% volilo.")
    print("\nAk to vypadá zle, zmenši si to 'ctr' + '-' alebo zvacsi 'ctr' + '+'.")
except ValueError as Err:
    print()     #Odriadkovanie
    print("Zadaj cisla bez medzie napr.1000000000")
    print("\nSpusti znova")
