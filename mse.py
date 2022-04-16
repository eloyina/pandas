import numpy as np



def b_(x,y):
    b=0.0
    n= len(x)
    for i in range(1):
        third_=(np.mean(x)**2)
        sec_= (x[i]**2)
        b+=((x[i]*y[i]) - (n*(np.mean(x))*(np.mean(y)))) / (sec_ - n*third_ ) 
    formatted_b = '{0:.1f}'.format(b)
    return formatted_b                                                       


def a_(prom_y, b, prom_x):
    a= float(prom_y) - float(b)* float(prom_x)
    ap=float('{0:.1f}'.format(a))

    return ap

def y_pri(a,b,x):
    n= len(x)
    lista_=[]
    for i in range(n):
        ypo= a + b*x[i]
        lista_.append(ypo)
    return lista_

def y_final(y, yi):
    yip=0
    for i in range(len(y)):
        yip= yip+(y[i]-yi[i])**2
        mse= yip/ (len(y))
    return mse

x=[1,2,3,4,5]
y=[1,1,2,2,4]
x_pred=[0.6,1.29,1.99,2.69,3.4]
prom_x=np.mean(x)
print(prom_x)
prom_y= np.mean(y)
print(prom_y)
k=float((b_(x,y)))
a=(a_(prom_y,k, prom_x))
yi=(y_pri(a,k,x))
print(y_final(y,yi))
