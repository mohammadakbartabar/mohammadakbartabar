
import math
a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
delta = (b**2-4*a*c)
if delta<0 :
                print ("moadele rishe haghighi nadarad")
elif delta == 0 :
                x=(-b)/(2*a)
                print("moadele yek rishe haghighi darad")
                print(x)
else:
                x_alfa = (-b-(math.sqrt(delta)))/(2*a)
                x_beta = (-b+(math.sqrt(delta)))/(2*a)
                print("moadele do rishe haghighi darad")
                print(x_alfa)
                print(x_beta)






