
def cetakPrima(x,y):
    if x >= 1 and y > 1:
        for x in range(x,y):
            prima = True
            for i in range(2,x):
                if (x%i==0):
                    prima = False
            if prima == True:
               print (x)
cetakPrima(2,1000)
