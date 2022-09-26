#matricola: 1216413  - nome: Albu Cosmin Andrei  - Data consegna: 15/05/2022 
from constraint import *
from networkx import *
import matplotlib.pyplot as plt


def sistema3():
    problem = Problem()
    
    #Imposta le variabili e i loro domini
    problem.addVariable('x', [13,12,34])
    problem.addVariable('y', [40,57,76])
    problem.addVariable('z', [6,8,20])
    
    #Modella i vincoli sulle variabili ('x','y','z')
    problem.addConstraint(lambda a,b,c : a<b and a+b+c<65 , ('x','y','z'))
    
    solutions = problem.getSolutions()
    
    if not len(solutions) == 0:
        return solutions[0]  #restituisco solo la prima soluzione
    else:
        return "Non ci sono soluzioni valide."

def grafo_vincoli(grafo):
    problem = Problem()
    
    for node in grafo.nodes():
        problem.addVariable(node,(["rosso", "verde", "blu"]))
        for neighbor in grafo.neighbors(node):
            problem.addConstraint(lambda a,b : a!=b, (node,neighbor))
            
    solutions = problem.getSolutions()
    
    if not len(solutions) == 0:
        return solutions[0]  #restituisco solo la prima soluzione
    else:
        return "Non ci sono soluzioni valide."
    
def nqueen(n):
    problem = Problem()
    
    #lista che contiene il dominio delle regine, ossia le posizioni 
    #che le regine possono assumere sulla scacchiera con il formato
    #seguente [i,j] dove i e j assumono valori tra 0(incluso) e n(escluso)
    dominio = []
    for i in range(n):
        for j in range(n):
            dominio.append([i,j])
    
    #inserisco i nomi delle variabili con il formato 'regina' + str(n+1)
    variabili = [] 
    for i in range(n):
        num = i + 1
        variabili.append("regina" + str(num))
    
    for regina in variabili:
        problem.addVariable(regina,(dominio))
        
    for regina in variabili:
        #creo una lista con tutte le regine tranne la regina che sto 
        #considerando in questo momento nel ciclo for
        altre_regine = variabili[:]
        altre_regine.remove(regina)
        
        for altra_regina in altre_regine:
            problem.addConstraint(lambda a,b : a[0]!=b[0] and a[1]!=b[1] and diagonali_libere(a,b,n), (regina,altra_regina))
    
    solutions = problem.getSolutions()
    
    if not len(solutions) == 0:
        return solutions[0] #restituisco solo la prima soluzione
    else:
        return "Non ci sono soluzioni valide."
        
#controlla che le diagonali di una regina non contengano un'altra regina
def diagonali_libere(a,b,max_value): 
    i = 0
    while i < max_value:
            if nella_scacchiera(a[0]+i,max_value) and nella_scacchiera(a[1]+i,max_value): #controllo che gli indici siano tra 0(incluso) e n(escluso)
                if a[0] + i == b[0] and a[1] + i == b[1]: #sono sulla stessa diagonale se True
                    return False #una diagonale non e' libera
            elif nella_scacchiera(a[0]-i,max_value) and nella_scacchiera(a[1]-i,max_value): #controllo che gli indici siano tra 0(incluso) e n(escluso)
                if a[0] - i == b[0] and a[1] - i == b[1]: #sono sulla stessa diagonale se True
                    return False #una diagonale non e' libera
            elif nella_scacchiera(a[0]+i,max_value) and nella_scacchiera(a[1]-i,max_value): #controllo che gli indici siano tra 0(incluso) e n(escluso) 
                if a[0] + i == b[0] and a[1] - i == b[1]: #sono sulla stessa diagonale se True
                    return False #una diagonale non e' libera
            elif nella_scacchiera(a[0]-i,max_value) and nella_scacchiera(a[1]+i,max_value): #controllo che gli indici siano tra 0(incluso) e n(escluso) 
                if a[0] - i == b[0] and a[1] + i == b[1]: #sono sulla stessa diagonale se True
                    return False #una diagonale non e' libera
            
            i = i+1
    return True
    
#controlla che un indice non sia fuori dalla scacchiera
def nella_scacchiera(value,max_value):
    if value>=0 and value < max_value:
        return True
    return False

"""
#main utilizzato per testare il codice    
if __name__ == '__main__':
   #problema1
    print(sistema3())
    
    #problema2
    grafo = Graph()
    grafo.add_nodes_from(["A","B","C","D","E"])
    grafo.nodes()
    
    grafo.add_edge("A","B")
    grafo.add_edge("A","D")
    grafo.add_edge("D","C")
    grafo.add_edge("D","E")
    grafo.add_edge("B","C")
    grafo.edges()
    
    print(grafo_vincoli(grafo))
    
    #draw(grafo)
    #plt.show()
    
    print(nqueen(5))
"""
    
    
    
    
    
    



