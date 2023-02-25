from sympy import *

a, F, G = var("a, F, G")

Ah, Av, Bv = var('A_h A_v B_v')

eqns = [
    Eq(0, Ah + F),
    Eq(0, Av + Bv - G),
    Eq(0, - G * a + Bv * 2 * a - F * a),
    ]

unknowns = [Bv,Ah,Av]
sol = solve(eqns, unknowns)
pprint(sol)

Bv = sol[Bv]

S4, S5, S7    = var('S4 S5 S7')

c=sqrt(2)/2

eqns = [
    Eq(0, -G - S7 - S5 - S4*c + F - G*c),
    Eq(0, -G*c + S4*c + Bv),
    Eq(0, a*S4*c + a*S5),
    ]

unknowns=[S4, S5, S7]
sol = solve(eqns, unknowns)
pprint(sol)
