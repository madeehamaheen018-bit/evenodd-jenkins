import sys
def simint(principal,interest,time):
    return(p*i*t)/100

    if__name__=="__main__":
        p = int(sys.argv[1])
        i = int(sys.argv[2])
        t = int(sys.argv[3])

        print("simple interest:",simint(p,i,t))