def check_fermat(a,b,c,n):
    a = int (a)
    b = int (b)
    c = int (c)
    n = int (n)
    if a**n+b**n==c**n:
        print "Holy smokes! Fermat was wrong!"
    else:
        print "No, that doesn't work."
        
