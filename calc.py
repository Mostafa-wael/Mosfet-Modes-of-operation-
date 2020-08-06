from sympy import symbols, solve,Function,sympify
####
def OhmicMode(vdd,vth,k,vds,vgs,Ir):
    ImOhmic = solve((k * ((vgs - vth) * vds - (vds ** 2) / 2))-Ir, vx)
    for sol in (ImOhmic):
        if (vds.subs(vx, sol) < vgs.subs(vx, sol) - vth) and (vgs.subs(vx, sol) > vth) and (vds.subs(vx, sol) >= 0 and vds.subs(vx, sol) <= vdd):
            return True,sol
    return False,0
def SatMode(vdd,vth,k,vds,vgs,Ir):
    ImSat = solve((k/2 *(vgs - vth)**2)-Ir, vx)
    for sol in (ImSat):
        if (vds.subs(vx, sol) > vgs.subs(vx, sol) - vth) and (vgs.subs(vx, sol) > vth) and (vds.subs(vx, sol) >= 0 and vds.subs(vx, sol) <= vdd):
            return True,sol
    return False,0
def solveMOSFET(vdd,vth,k,vds,vgs,Ir):
    ohmic = OhmicMode(vdd, vth, k, vds, vgs, Ir)
    if (ohmic[0]):
        print("M in OhmicMode")
        print(ohmic[1])
        return
    sat = SatMode(vdd, vth, k, vds, vgs, Ir)
    if (sat[0]):
        print("M in SatMode")
        print(sat[1])
        return
    print("CutOffMode")
####Constants
vdd=symbols('vdd')
vth=symbols('vth')
k=symbols('k')
print('please enter the following constants')
vdd=float(input('vdd = '))
vth =float( input('vth = '))
k = float(input("'in floating points'k = "))
####Sympols
vx=symbols('vx')
vd=symbols('vd')
vs=symbols('vs')
vg=symbols('vg')

####Functions
vds=Function('')
vgs=Function('')

Ir=Function('')
null=Function('')
null=vx-vx
###
print('\nfor the equation in the form of Im=Ir,we find (vx) for you and the mode of operation !')
print('note that in this program we assume that the M is connected in series with a resistor')
fine='y'
while fine=='y':
    print("at least one of the M terminals should contain 'vx':")

    temp=input("please enter the expression for vd, vd= ")
    vd= vdd if temp=='vdd' else sympify(temp)

    temp=input("please enter the expression for vs, vs= ")
    vs=vdd if temp=='vdd' else sympify(temp)

    temp = input("please enter the expression for vg, vg= ")
    vg=vdd if temp=='vdd' else sympify(temp)

    Ir=null+sympify(input("please enter the expression for Ir, Ir= "))
    ####
    vds=null+vd-vs
    vgs=null+vg-vs
    print('vds='+str(vds))
    print('vgs='+str(vgs))
    print('Ir='+str(Ir))
    print('\n')
    ####
    solveMOSFET(vdd, vth, k, vds, vgs, Ir)
    fine=input('continue with the same constants y/n')
