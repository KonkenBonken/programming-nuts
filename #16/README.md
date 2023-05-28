`@Programmeringsnöten` #16

Skriv en kod som får in ett positivt heltal `N` och sedan beräknar och skriver ut fakulteten av talet: `N!`

> `N! = N ⋅ (N-1) ⋅ … ⋅ 2 ⋅ 1`

Exempel 1:

```py
N: 4
Svar: 24
# 4! = 4 ⋅ 3 ⋅ 2 ⋅ 1 = 24
```

Exempel 2:

```py
N: 10
Svar: 3628800
# 10! = 10 ⋅ 9 ⋅ 8 ⋅ 7 ⋅ 6 ⋅ 5 ⋅ 4 ⋅ 3 ⋅ 2 ⋅ 1 = 3628800
```

---

I matematiken finns, utöver `fakultet`, en grej som kalla `dubbel fakultet` och `trippel fakultet` osv
Det `dubbel fakultet` innebär att du endast multiplicerar med vartannat heltal, istället för alla

> `N!! = N⋅(N-2)⋅(N-4)…(4)⋅(2)`
> Eller om talet är udda:
> `N!! = N⋅(N-2)⋅(N-4)…(3)⋅(1)`

Det samma gäller då för trippel: `(N-3)`

Nu, skriv ett program som tar in 2 tal, `N` och `K` och beräkna sedan `K fakulteten` av `N`

Exempel 1:

```py
N: 6   K: 2
Svar: 48
# 6!! = 6 ⋅ 4 ⋅ 2 = 48
```

Exempel 2:

```py
N: 7   K: 3
Svar:
# 7!!! = 7 ⋅ 4 ⋅ 1 = 28
```

Exempel 3:

```py
N: 130   K: 50
Svar: 312000
# 13!…!! = 130 ⋅ 80 ⋅ 30 = 312000
```
