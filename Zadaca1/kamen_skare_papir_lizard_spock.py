igrac1=input ('Unesi k,p,s,g,sp')
igrac2=input ('Unesi k,p,s,g,sp')
if igrac1=='k' and igrac2=='p':
    print('Pobjednik je igrac 2')
elif igrac2=='k' and igrac1=='p':
    print('Pobjednik je igrac 1')
elif igrac1=='s' and igrac2=='p': 
    print('Pobjednik je igrac 1')
elif igrac2=='s' and igrac1=='p':
    print('Pobjednik je igrac 2')   
if igrac1=='k' and igrac2=='s': 
    print('Pobjednik je igrac 1')
elif igrac2=='k' and igrac1=='s':
    print('Pobjednik je igrac 2') 
elif igrac2=='k' and igrac1=='g':
    print('Pobjednik je igrac 2')
elif igrac1=='g' and igrac2=='sp':
    print('Pobjednik je igrac 1') 
elif igrac1=='s' and igrac2=='sp':
    print('Pobjednik je igrac 2')
elif igrac1=='s' and igrac2=='g':
    print('Pobjednik je igrac 1')
elif igrac1=='g' and igrac2=='p':
    print('Pobjednik je igrac 1')
elif igrac1=='sp' and igrac2=='p':
    print('Pobjednik je igrac 2')
elif igrac1=='sp' and igrac2=='s':
    print('Pobjednik je igrac 1')

if igrac1=='k' and igrac2=='k': 
    print('Nerješena igra')
if igrac1=='p' and igrac2=='p': 
    print('Nerješena igra')   
if igrac1=='s' and igrac2=='s': 
    print('Nerješena igra')
if igrac1=='sp' and igrac2=='sp': 
    print('Nerješena igra')
if igrac1=='g' and igrac2=='g': 
    print('Nerješena igra')
 


if igrac1!='s' and igrac1!='p' and igrac1!='k'and igrac1!='sp'and igrac1!='g':
    print('Greška igrača 1')
if igrac2!='s' and igrac2!='p' and igrac2!='k'and igrac1!='sp'and igrac1!='g':
    print('Greška igrača 2')
