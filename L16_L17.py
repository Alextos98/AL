Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 160
>>> # Aleksejs Lucinskis
>>> # 181RDB146
>>> g = 9.81

v0 = 0 # bumbas sakuma miera stavoklis
t = 0.1 # laiks no bumbas atlaisanas briza ir 0.1 sekunde
y = v0 - 0.5*g*t**2 # aprekinata bumbas pozicija uz y ass
print (y) # rezultats uz ekrana

t = 1 # pec vienas sek kas notiks?
y= 0*t - 0.5*g*t**2
print (y)

v0 = 5 # bumba tiek pamesta gaisa ar atrumu 5 m/s
t = 0.7 # pec 0.7 sekundem kas notiks?
y = v0*t - 0.5*g*t**2
print (y)

v0 = 5 ; t = 1; y = v0*t - 0.5*g*t**2
print ('\nPec %g sekundes bumba bus %.2f metru augstuma \n '%(t,y))
print ('Sakotnejais bumbas atrums bus %g m/s^2 %.2f metru augstuma \n '%(v0,y))
