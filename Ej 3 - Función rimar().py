#Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
#las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
#últimas tiene que decir que riman un poco y si no, que no riman.

def rimar(x,y):
    if(len(x) > 3 and len(y) > 3):
        if(x[-3:] == y[-3:]):
            print("Riman")
        elif(x[-2:] == y[-2:]):
            print("Riman un poco")
        else:
            print("No riman")
    
    exit()

def main():
    x = input("Introduce la primera palabra: ")
    y = input("Introduce la segunda palabra: ")
    rimar(x,y)

main()

