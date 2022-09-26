#matricola: 1216413  - nome: Albu Cosmin Andrei  - Data consegna: 01/05/2022 
def massimo(a,b):
    if a>b:
       return 1
    elif b>a:
       return -1
    else:
       return 0
       
def moltiplicatrice(lista_numeri):
    if not len(lista_numeri) == 0:
       sum = 1
       for elem in lista_numeri:
          sum = sum * elem
       return sum
       
    return 0 #se il codice arriva in questa riga la lista e' vuota

def rovescia(stringa):
    s1 = stringa.lower().strip() #la stringa viene impostata in minuscolo e poi con strip() vengono tolti i caratteri vuoti all'inizio e alla fine della stringa 
    s2 = ""  #stringa da restituire e in cui verranno inseriti i caratteri dopo essere stati invertiti
    
    if not len(s1) == 0:
        list1 = list(s1) #strip toglie gli eventuali spazi dall'inizio e la fine della stringa s
        #list1 e' una lista che contiene tutti i caratteri della list s
        
        list2 = []
        for i in range(len(list1)-1,-1,-1):
           list2.append(list1[i])
           
        list2[0] = list2[0].upper() #primo carattere della stringa invertita viene impostato in maiuscolo
        
        #trasformo list2 in una stringa
        s2 = s2.join(i for i in list2)
        
    return s2
    
def frequenza(stringa):
    list1 = list(stringa.lower().strip())
    dict1 = {}
    
    for c in list1:
        if not c in dict1:
           dict1[c] = 1 #il carattere c non e' presente nel dizionario, quindi lo inserisco con moltiplicita' 1
        else:   
            dict1[c] = dict1[c] + 1 # se il carattere c e' gia' presente nel dizionario, aumento la sua moltiplicita' di 1        

    return dict1  
    
"""
#main per i test    
if __name__ == '__main__':
    print("test funzione massimo(a,b)")
    print("Expected: -1 - value:",massimo(3,8))
    
    print("test moltiplicatrice(lista_numeri)")
    print("Expected: 336 - value:",moltiplicatrice([3,7,2,2,4]))
    print("Expected: 0 - value:",moltiplicatrice([])) #test lista vuota
    
    print("test funzione rovescia(stringa)")
    print("Expected: Olleb 'e erammargorp - value:",rovescia("ProgrAmmaRe e' belLo"))
    print("Expected:  - value:",rovescia("")) #test stringa vuota
    print("Expected:  - value:",rovescia(" ")) #test stringa con uno spazio
    print("Expected: Trops eraf ecaip im - value:",rovescia("Mi piace fare sport"))
    print("Expected: Acinemod - value:",rovescia("domenica"))
    
    print("test funzione frequenza(stringa)")
    print("Expected: {'p': 1,'a': 1,'n': 1,'e': 1}  - value:",frequenza("pane"))
    print("Expected: {'p': 1,'a': 2,'l': 2}  - value:",frequenza("palla"))
    print("Expected: {'g': 5}  - value:",frequenza("ggggg"))
    print("Expected: {}  - value:",frequenza(""))
"""
