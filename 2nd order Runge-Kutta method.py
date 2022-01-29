#2nd order runge kutta method

def fp(t,y):
    return t*y #put function here

y0=1 #initial y
t0=0 #initial t
h=.1 #h size
iterations=5 #number of iterations


string="k=0"
string+="\tt0="+str(t0)
string+="\ty0="+str(y0)
string+="\t\ts1="+str(fp(t0,y0))
string+="\t\ts2="+str(fp(t0+h,y0+h*fp(t0,y0)))
string+="\t\th="+str(h)
string+="\th(s1+s2)/2="+str(round(h*(fp(t0,y0)+fp(t0+h,y0+h*fp(t0,y0)))/2,4))
print(string)

yb=y0
tb=t0
avgslope=h*(fp(t0,y0)+fp(t0+h,y0+h*fp(t0,y0)))/2

for i in range(1,iterations+1):
    string="k="+str(i)
    string+="\tt"+str(i)+"="+str(round(i*h,4))
    string+="\ty"+str(i)+"="+str(round(yb+avgslope,4))
    string+="\ts1="+str(round(fp(i*h,yb+avgslope),4))
    string+="\ts2="+str(round(fp(i*h+h,yb+avgslope+h*fp(i*h,yb+avgslope)),4))
    string+="\th="+str(h)
    string+="\th(s1+s2)/2="+str(round(h*(fp(i*h,yb+avgslope)+fp(i*h+h,yb+avgslope+h*fp(i*h,yb+avgslope)))/2,4))
    oldavg=avgslope
    avgslope=h*(fp(i*h,yb+avgslope)+fp(i*h+h,yb+avgslope+h*fp(i*h,yb+avgslope)))/2
    yb=yb+oldavg
    tb=(i)*h
    print(string)
    
