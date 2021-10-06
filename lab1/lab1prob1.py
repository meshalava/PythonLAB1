s = float(input("Площа трикутника:"))
a = float(input("ВелиЧИНА:"))
h1 = ((0-a)+(a*a+(8*s))**0.5)/2;
h2 = ((0-a)-(a*a+(8*s))**0.5)/2;
#x.toFixed(2)
h1 = round(h1,2)
h2 = round(h2,2)
if(h1>0):
    print(h1)
if(h2>0):
    print(h2)
