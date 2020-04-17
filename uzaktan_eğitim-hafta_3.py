import sympy as sym
from sympy import Symbol
from sympy import pprint
from sympy import matplotlib


p=Symbol('p')
x=Symbol('x')
n=Symbol('n')

my_f_3_part_0=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
print(my_f_3_part_0)

pprint(my_f_3_part_0)


my_f_3_part_1=p**x
print(my_f_3_part_1)

pprint(my_f_3_part_1)


my_f_3_part_2=(1-p)**(n-x)
print(my_f_3_part_2)

pprint(my_f_3_part_2)


my_f_3=my_f_3_part_0*my_f_3_part_1*my_f_3_part_2
print(my_f_3)

pprint(my_f_3)


sym.plot(my_f_3.subs({p:0.5,n:50}), (x, 0, 50), title='Binomial Distribution Plot for n=50')



1111111111111111111111111111111111111111111111111

from sympy import Symbol, Limit

t = Symbol('t') 
St = 5*t**2 + 2*t + 8

t1 = Symbol('t1')
delta_t = Symbol('delta_t')

St1 = St.subs({t: t1})
St1_delta = St.subs({t: t1 + delta_t})

Limit((St1_delta-St1)/delta_t, delta_t, 0).doit()



222222222222222222222222222222

from sympy import Symbol, exp, sqrt, pi, Integral 


x = Symbol('x') 
p = exp(-(x - 10)**2/2)/sqrt(2*pi)

Integral(p, (x, 11, 12)).doit().evalf() vvvvvvvvvvvv


