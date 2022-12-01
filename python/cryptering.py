# Kapittel 31 i CLRS heter 'Number-Theoretic Algorithms' side 926-984 inneholder mye snacks!
'''
Mangler:
    - Samle ting i funksjoner
    - Skrive det litt pent og didaktisk
    - Blokkinndeling
    - Hadde vært gøy med fullverdig RSA-løsning (kunne hatt katalog på kurssiden og sånt)

Fuck Python liste:
    - q = 35028926852816670, da er q/2 % 2 lik 0, men q//2 % 2 er 1...
'''
import time
import numpy as np
import random as rnd

# Euklids algoritme

# Det virker ikke som at det spiller noen rolle hvilken av a og b som er størst,
# men jeg tror egentlig det bør ha noe å si. Undersøk og forstå.

def gcd(a, b):
    r      = b # For å initialisere slik at while-løkken kjøres
    rvals  = []
    while r > 0:
        r = a - a//b * b
        rvals.append(r)
        a = b
        b = r

    # Koden nedenfor håndterer caset der a=b
    if len(rvals) > 1:
        rvals = rvals[:-1]
    else:
        rvals = [a]
    return rvals[-1]

'''
print(gcd(630, 224))
print(gcd(48, 30))
print(gcd(420, 150))
print(gcd(76084, 63020))
print(gcd(49, 36))
print(gcd(0, 8))
print(gcd(7, 7))

print(gcd(63020, 76084))
'''
# Diofantisk likning løser


# Effektiv eksponentiering


############################ Kalender/Ukedag-greie #############################

# Implementasjon av ukedagsformelen som gitt i boken "I tallkongruensenes verden"
# side 50-56
dato = "03/04/1989" # Mandag
dato = "04/02/2000" # Fredag

d = int(dato[0:2])
m = ((int(dato[3:5]) - 3) % 12) + 1 # mars=1, april=2, ..., februar=12
H = int(dato[-4:-2])
A = int(dato[-2:])

# I formelen skjer ikke overgangen til nytt år før 1. mars så må trekke fra en på
# året i januar og februar
if m in [11, 12]:

    # Hvis hundreårsskifte må vi også håndtere H:
    if A == 0:
        H = H-1

    # Trekker 1 fra året (hvis 00 får vi 99 og dette kan håndteres med mod)
    A = (A - 1) % 100


U = (d + int((13*m-1)/5) + A + int(A/4) + int(H/4) - 2*H) % 7

U2d = {0: "søndag", 1:"mandag", 2:"tirsdag", 3:"onsdag", 4:"torsdag", 5:"fredag", 6:"lørdag"}

# print(f'{dato} var en {U2d[U]}.')
################################################################################


#### KRYPTERING #####
# For å gjøre ting litt mer leselig er også punktum og mellomrom tatt med i 'alfabetet'.

#%%
# Bokstav til tall
b2t = {' ': 0, 'A': 1, 'B': 2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, 'Æ':27, 'Ø':28, 'Å':29, '.': 30, ',': 31, '!': 32}
t2b = {i: j for j, i in b2t.items()} # Lager en ordbok som kan brukes til å gjøre om tall til bokstaver

antallBokstaver = len(b2t.values())


Tekststreng = 'Dette er en hemmelighet'
Tekststreng = Tekststreng.upper() # Gjør om alt til store bokstaver
#%%

# Cæsar-shift
shift = 3

kodet = list(Tekststreng)
kodet = [b2t[i] for i in kodet]
kodet = [(i+shift) % antallBokstaver for i in kodet]

#print('Kodet beskjed (Cæsar-shift) er:', "".join([t2b[i] for i in kodet]))

dekodet = [(i-shift) % antallBokstaver for i in kodet]
dekodet = [t2b[i] for i in dekodet]
dekodet = "".join(dekodet)

#print('Dekodet beskjed er:', dekodet)

# Multiplikativ
n  = 65
q  = 18
q2 = 47 # q2 velges slik at q*q2 = 1 mod n.

kodet = list(Tekststreng)
kodet = [b2t[i] for i in kodet]
kodet = [(i * q) % n for i in kodet]
# kodetSomTekst = [t2b[i] for i in kodet] # Gir feilmelding siden noen tall ikke er i listen
#print('Kodet beskjed er: ', kodet)

dekodet = [(i * q2) % n for i in kodet]
dekodet = [t2b[i] for i in dekodet]
dekodet = "".join(dekodet)

#print("Dekodet beskjer er: ", dekodet)


# Eksponentiering
# FYLL UT
#def fastExp(a,b,n):
c = 0
d = 1

# RSA
# Pass på å få med støtte for flere personer slik at man kan sende krypterte meldinger til flere

def base2(n):
    # Returns list with base 2 representation of input number
    base2 = []
    while n>0:
        if n % 2 == 0:
            base2.append(0)
            n = n//2
        else:
            base2.append(1)
            n = (n-1)//2

    base2.reverse() # !

    return base2

def modexp(a,b,n):
    # Implementation of fast modular exponentiation
    # Calculates a**b % n.
    # Implementation of algorithm from CLRS p. 957
    c = 0
    d = 1
    base2rep = base2(b)

    for i in range(len(base2rep)):
    #for i in range(len(base2rep)-1,-1,-1):
        c = 2*c
        d = (d*d) % n
        if base2rep[i] == 1:
            c = c + 1
            d = (d*a) % n

        #print(d)

    return d

#print(1)
#q = 35028926852816671
#print(modexp(2,q-1,q))   
#print(base2(q-1))
#print(base2(560))
#print(modexp(7,560,561))
#1111100011100101001111110010101111011001101111100011110 # Fra internett
#1111100011100101001111110010101111011001101111100100000 # Fra min
#print(modexp(7,560,561)) # 12423
#print('DENNE')
#print(modexp(81,560,561)) # 12423

def RSA(n, key, message):
    # Encrypts/decrypts RSA coded message
    # Message is assumed to be a list where each element is one 'block'

    newMessage = []
    for i in message:
        newMessage.append(modexp(i,key,n))

    return newMessage

Tekststreng = 'Dette er en hemmelighet'.upper()
kodet = list(Tekststreng)
kodet = [b2t[i] for i in kodet]
#print(kodet)
kodet = RSA(13*17,55,kodet)
#print(kodet)
dekodet = RSA(13*17,7,kodet)
#print(dekodet)

#def block(message, blocksize):
    # Input er en liste med tall.
    # Output er en ny liste der tallene er slått sammen i blokker med
    # størrelse blocksize.
#    newMessage = []

def euclid(a,b):
    # Implementation of the Euclidean algorithm
    # From CLRS p. 935
    # Returns gcd(a,b)
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

def extendedEuclid(a,b):
    # Implementation of the extended Euclidean algorithm
    # From CLRS p. 937
    # Returns a triplet (d,x,y) where d=gcd(a,b) and x*a+y*b=d.

    if b == 0:
        return (a, 1, 0)
    else:
        (d,x,y) = extendedEuclid(b, a % b)
        (d,x,y) = (d,y, x - (a//b)*y)
        return (d,x,y)

def modularLinearSolver(a,b,n):
    # Implementation of a modular linear equation solver
    # From CLRS p. 949
    # Returns a list of all solutions of a*x=b mod n (empty list if no solution)
    (d,x,y) = extendedEuclid(a,n)
    sols = []
    if (b % d) == 0:
        x = (x * (b//d)) % n
        for i in range(d):
            sols.append(int((x+ i*(n//d)) % n))

    return sols

#print(euclid(99,78))
#print(extendedEuclid(99,78))
#print(modularLinearSolver(14,30,100))
# EN MULIG OPPGAVE KAN VÆRE Å UTVIDE TIL Å LØSE 4 ELLER 5 SIMULTANE KONGRUENSER

def CRT(a,b,c,n1,n2,n3):
    # Løser de samtidige kongruensene x=a mod n1, x=b mod n2, x=c mod n3
    # Returnerer -1 hvis kongruensene ikke er løsbare.

    sff1 = euclid(n1,n2)
    sff2 = euclid(n1,n3)
    sff3 = euclid(n2,n3)

    if sff1 == 1 and sff2 == 1 and sff3 == 1:
        x1 = modularLinearSolver(n2*n3,1,n1)[0]
        x2 = modularLinearSolver(n1*n3,1,n2)[0]
        x3 = modularLinearSolver(n1*n2,1,n3)[0]

        x = a*x1*n2*n3 + b*x2*n1*n3 + c*x3*n1*n2
        x = x % (n1*n2*n3)

        return x
    else:
        return -1


def erPrimtall(n):
    # CLRS side 967
    # Ideen: Vi vet fra Fermats lille teorem at a^(p-1)=1 mod p for primtall
    # Dette vil ofte ikke stemme hvis tallet p ikke er et primtall.
    # Vi regner derfor ut 2^(n-1) mod n og sier at tallet er et primtall
    # hvis dette blir 1. Denne testen kan bomme. Vi vil aldri ende opp med å
    # si at et primtall ikke er et primtall, men vi kan ende opp med å si at noe
    # som ikke er et primtall er et primtall (f. eks. 1105 som er et pseudoprimtall)
    if modexp(2,n-1,n) != 1:
        return False # Kan ikke være primtall hvis vi ender her
    else:
        return True # Kan bomme her (pseudoprimtall)



def witness(a,n):
    # CLRS s. 969
    # Sjekker om a kan brukes som et 'vitne' for at n ikke er et primtall.
    # Vi gjør samme sjekk som med Fermats lille teorem, men vi regner ut
    # a^(n-1) på en litt annen måte og legger inn noen ekstra sjekker.
    # Vi skriver n-1=2^t * u der u er et oddetall. Vi har da at a^(n-1)=(a^u)^(2t).
    # Vi kan derfor regne ut a^(n-1) ved å først regne ut a^u, og så kvadrere dette
    # tallet t ganger (alle utregninger modulo n). Vi vet at hvis n er et primtall
    # har 1 ingen ikke-trivielle kvadratrøtter (likningen x^2=1 mod p har kun
    # løsningene x=+-1), og vi kan derfor ved hver kvadrering undersøke om tallet
    # vi får er en ikke-triviell kvadratrot av 1. Hvis det er tilfelle kan vi
    # terminere og si at a er et 'vitne' for at n ikke er et primtall.
    # Denne funksjonen vil aldri si at et primtall ikke er et primtall, men den
    # kan si at noe som ikke er et primtall er et primtall. 
    t  = 0
    u  = n-1
    while (u % 2) == 0:
        u = u//2
        t = t + 1

    xi0 = modexp(a,u,n)
    #print(xi0)

    for i in range(t):
        xi1 = (xi0**2) % n
        if xi1 == 1 and xi0 != 1 and xi0 != (n-1):
            return True
        xi0 = xi1
    if xi1 != 1:
        return True

    return False

def erPrimtallMillerRabin(n,s):
    # CLRS s. 970
    # Ideen: Vi utvider erPrimtall til å sjekke om a^(n-1)=1 mod n
    # for s tilfeldig valgte tall. Dette er noe sikrere enn å kun sjekke for 2
    # (som vi gjør med erPrimtall), men vi kan fortsatt bomme.
    # Teorem 31.39 fra CLRS side 973: Hvis n>2 er et oddetall så er sannsynligheten
    # for at Miller-Rabin gir feil resultat <=2^(-s).
    # Korollar: Hvis vi f. eks. velger s=10 er sannsynligheten for at vi får feil
    # resultat litt under 1 promille.
    # CLRS skriver at i praksis er ofte s=3 nok, og s=50 'should suffice for any
    # imaginable situation' (s. 974)
    for j in range(s):
        a = rnd.randrange(2,n)
        #a = 12423
        if witness(a,n):
            return False # Ikke primtall
    return True # Sannsynligvis primtall

'''
print('Pseudoprimtall:')
print(erPrimtall(5521)) # Er primtall
print(erPrimtall(1105)) # Ikke primtall men pseudoprimtall
print(erPrimtall(5005)) # Ikke primtall
print('Miller-Rabin:')
#print(erPrimtallMillerRabin(5791,2))
print(erPrimtallMillerRabin(5521,10))
print(erPrimtallMillerRabin(1105,10))
print(erPrimtallMillerRabin(5005,10))
'''

def faktorPollardRho(n, maxIter=10000):
    # CLRS s. 976
    # Finner en ikke-triviell faktor av n. Kan bomme.

    i   = 1
    #xi0 = np.random.randint(0,n)
    xi0 = rnd.randint(0,n)
    y   = xi0
    k   = 2
    d   = 1

    while (d == 1 or d == n) and i<maxIter:
        i   = i + 1
        xi1 = (xi0**2 - 1) % n
        d   = euclid(y-xi1, n)
        #if d != 1 and d != n:
        #    faktorer.append(d)
        if i == k:
            y = xi1
            k = 2*k

        xi0 = xi1

    if i==maxIter:
        print('Error! Pollard-Rho terminerer etter maks antall iterasjoner')
        d = -1

    return d

#x = faktorerPollardRho(353452345)
#print(faktorPollardRho(485766159834553576789343534526511335673459192146354687843567)) # 60 sifre
#print(erPrimtallMillerRabin(114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541,5))
#print(faktorPollardRho(114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541)) # 129 sifre
#print(faktorPollardRho(4857661545612658497805421698780985533198357554999603755840002368421008945535767893435345265113356734591921463546878435675489654123)) # 130 sifre
#print(faktorPollardRho(15485863*15485857*15485843*15485689))
#print(x)
'''
# Illustration of fast modular exponentiation
# Without below choice of a,b,n the fast exp takes 0.0 seconds and
# the naive method takes about 12 seconds
a = 7
b = 10000000
n = 561
start = time.time()
print(modexp(a,b,n))
times = [time.time()-start]
start = time.time()
print( (a**b) % n)
times.append(time.time()-start)
print(times)
'''

def finnPrimtall(nbits,s=5):
    # Funksjon som finner et tall som sannsynligvis er et primtall
    # Dette gjøres ved å generere et tilfeldig oddetall og sjekke om det er 
    # et primtall. Hvis ikke genereres et nytt tall. Dette gjentas til man
    # finner et tall som passerer Miller-Rabin primtallsjekken.
    # Bakgrunnsteori: La pi(n) være en funksjon som teller antall primtall
    # mindre enn eller lik n. F. eks. er pi(15)=6 og pi(17)=7.
    # Primtallsteoremet sier at lim_(n->uendelig) pi(n)/(n*ln(n)) = 1.
    # Det betyr at for et tilfeldig valgt tall n er sannsynligheten for at n er
    # et primtall omtrent 1/ln(n). Hvis vi tenker på å gjette et tall som et forsøk
    # kan vi anta en geometriskfordeling som betyr at vi må prøve omtrent ln(n) tall
    # før vi finner et primtall. Dette kan halveres ved å kun prøve oddetall.

    erPrimtall = False
    while not erPrimtall:
        n = 2
        while n % 2 == 0:
            n = rnd.randrange(2**(nbits-1) + 1, 2**nbits - 1)
        erPrimtall = erPrimtallMillerRabin(n,s)

    return n

#q = 141428491832287307802045848373705417117314779791540752555606026748124084248448251596685834090671493941409176609655869477257988686080113247357853006790698180884702892846650111975527952260158289468768371076039794723484581473946543280391433872980684306471059726283720069036075051203142839403622282464367573288017
#q = 750721329677959794275931331381 # DENNE ER ET PRIMTALL
#q = 614942752064693057
#q = 35028926852816671
#print(erPrimtallMillerRabin(q,1))
#print(isMillerRabinPassed(q))
#p = finnPrimtall(1024,3)
#print(p)
#q = 35028926852816671
#print(modexp(2,q-1,q))    

#p1 = 30853587387303149569
#p2 = 34069340494001274881
#n  = 1051161374159454189717212259512625676289 # p1*p2
#print(faktorPollardRho(p1*p2,1000000)) # Pollard Rho klarer ikke denne


def generateRSAKeys(nbits):
    # Genererer RSA nøkkelpar.
    # Returnerer en liste på formen ((n,private),(n,public))

    p = finnPrimtall(nbits)
    q = finnPrimtall(nbits)

    n   = p*q
    phi = (p-1)*(q-1)

    r = phi

    while euclid(r,phi) > 1:
        r = rnd.randrange(2,phi)

    s = modularLinearSolver(r,1,phi)[0]

    public = (n,r)
    private = (n,s)

    return (public, private)

test = generateRSAKeys(500)
print(test)