#matricola: 1216413  - nome: Albu Cosmin Andrei  - Data consegna: 22/05/2022 

import numpy
import os.path
import pandas

def linear_regr(dataset, value): 
    if not os.path.exists(dataset):
        return None
    
    alpha = 0.01
    iters = 1000
    
    def computeCost(X, y, theta):
	    inner = np.power(((X * theta.T) - y),2)
	    return np.sum(inner) / (2 * len(X))

    def gradientDescent(X, y, theta, alpha, iters):
        temp = numpy.matrix(numpy.zeros(theta.shape))
        parameters = int(theta.ravel().shape[1])
        cost = numpy.zeros(iters)
        for i in range(iters):
            error = (X * theta.T) - y
            for j in range(parameters):
                term = numpy.multiply(error, X[:,j])
                temp[0,j] = theta[0,j] - ((alpha / len(X)) * numpy.sum(term))
            theta = temp
            cost[i] = computeCost(X, y, theta)
        return theta, cost

    header = 0
    with open(dataset) as file:
        if file.read()[0].isdecimal():
            header = None

    data = pandas.read_csv(dataset, header=header, names=['x','y'])
    
    data.insert(0,'ones',1)

    cols = data.shape[1]
    X = data.iloc[:,0:cols - 1]
    y = data.iloc[:,cols - 1:cols]

    X = numpy.matrix(X.values)
    y = numpy.matrix(y.values)
    theta = numpy.matrix(numpy.array([0, 0]))

    g,cost = gradientDescent(X,y,theta,alpha,iters)
    return g[0,0] + (g[0,1] * value)

def vertical_stack(a,b):
    if len(a) == len(b):
        return numpy.array([a,b])
    return numpy.array([])

def match(a,b):
    if len(a) == len(b):
        list_indexes = []
        i = 0
        i_max = len(a) 
        while i < i_max:
            if a[i] == b[i]:
                list_indexes.append(i)
            i = i + 1
        
        return list_indexes
    return []            

"""
#main utilizzato per testare il codice            
if __name__ == "__main__":
    #esercizio 2
    a = numpy.array([1,3,56])
    b = numpy.array([1,54,8])
    result = vertical_stack(a,b)
    print(result)
    
    #esercizio 3
    a = numpy.array([1,45,4,6,2,23])
    b = numpy.array([1,2,4,2,5,0])
    result = match(a,b)
    print(result)
"""   
    
