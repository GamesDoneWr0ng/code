import re
data = """x00: 1
x01: 1
x02: 1
x03: 1
x04: 0
x05: 1
x06: 0
x07: 1
x08: 0
x09: 1
x10: 1
x11: 1
x12: 1
x13: 1
x14: 0
x15: 1
x16: 1
x17: 0
x18: 0
x19: 1
x20: 1
x21: 0
x22: 1
x23: 1
x24: 0
x25: 0
x26: 0
x27: 0
x28: 1
x29: 1
x30: 1
x31: 0
x32: 1
x33: 0
x34: 1
x35: 1
x36: 1
x37: 0
x38: 1
x39: 1
x40: 0
x41: 0
x42: 0
x43: 1
x44: 1
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1
y05: 0
y06: 0
y07: 0
y08: 0
y09: 0
y10: 1
y11: 0
y12: 0
y13: 1
y14: 0
y15: 1
y16: 0
y17: 1
y18: 1
y19: 0
y20: 1
y21: 0
y22: 0
y23: 0
y24: 1
y25: 0
y26: 0
y27: 0
y28: 1
y29: 1
y30: 0
y31: 1
y32: 0
y33: 0
y34: 0
y35: 0
y36: 1
y37: 1
y38: 0
y39: 0
y40: 1
y41: 1
y42: 1
y43: 1
y44: 1

kgv OR rdq -> stt
y00 AND x00 -> pjf
y13 XOR x13 -> wqh
y21 AND x21 -> ccs
wws AND cds -> kgv
x09 AND y09 -> sgj
x14 XOR y14 -> tnm
msn OR ssj -> vfb
cwt AND wfd -> wjk
y41 XOR x41 -> fsh
jhn AND hjd -> nfk
kvg OR sgj -> cwt
trk OR trs -> nvk
jnf XOR wgh -> z09
bkg AND tgw -> vrw
dvr OR wtv -> dwg
vch AND css -> cjn
wmf AND mdn -> qnn
gbv AND pth -> hns
jgb AND qbm -> jdb
x05 XOR y05 -> wcq
gtv OR pjr -> crc
y23 XOR x23 -> vph
jwq AND fqf -> tgv
y38 XOR x38 -> ghm
dgc OR ntm -> hrs
y22 XOR x22 -> tgw
stt AND wcr -> krw
gvt AND kns -> nmv
y03 AND x03 -> scc
x42 XOR y42 -> vcf
jbj OR rrc -> cvn
pth XOR gbv -> z17
hpb OR scc -> ngk
mvf XOR hrs -> z29
x17 XOR y17 -> gbv
y22 AND x22 -> kkq
y37 XOR x37 -> vcr
sqq XOR fgt -> z36
wcq AND knc -> gnw
krw OR hbj -> nkt
hpm OR mrw -> knc
vts OR hsk -> vfw
y19 AND x19 -> sjt
qbm XOR jgb -> z21
x28 AND y28 -> ntm
bwv XOR wsh -> z12
y43 XOR x43 -> cch
vfb XOR fpt -> z03
qkc OR sqw -> hjd
vqr OR ndj -> fqf
mcf AND cch -> kcq
qjb XOR kjr -> z35
y44 AND x44 -> mgv
vfw AND mqt -> ndj
x34 XOR y34 -> jwk
jnf AND wgh -> kvg
x41 AND y41 -> dqw
x02 AND y02 -> msn
vfb AND fpt -> hpb
swb AND qvq -> gtv
vnq XOR wqh -> z13
trn XOR pgk -> z06
cvn XOR gmp -> z30
vfw XOR mqt -> z07
ctf XOR tnm -> z14
hwb OR wmb -> ctf
ghm XOR hjg -> z38
wkt OR qjj -> tgj
kcq OR dcc -> cpw
x06 XOR y06 -> pgk
cjn OR jmv -> jgb
y00 XOR x00 -> z00
mdn XOR wmf -> z39
y36 AND x36 -> gst
tgw XOR bkg -> z22
tgv OR cfk -> wgh
y25 XOR x25 -> ktd
wdj AND fvw -> dvr
kbk OR wpm -> sgn
x44 XOR y44 -> dph
wsh AND bwv -> tnr
y24 XOR x24 -> skp
y30 XOR x30 -> gmp
y05 AND x05 -> gdd
x11 AND y11 -> rsw
qnn OR rrn -> fvw
x34 AND y34 -> hgg
wcs OR rpr -> fgt
x07 AND y07 -> vqr
fvw XOR wdj -> z40
y29 AND x29 -> rrc
fsh XOR dwg -> z41
cpw XOR dph -> z44
y32 XOR x32 -> hbg
pjf AND fcg -> vms
cwt XOR wfd -> z10
x27 AND y27 -> hbj
y04 AND x04 -> mrw
vcf XOR btn -> z42
vnq AND wqh -> wmb
x43 AND y43 -> dcc
vrw OR kkq -> jjr
cds XOR wws -> z26
x39 XOR y39 -> wmf
y29 XOR x29 -> mvf
rfn OR pmm -> mhh
y35 XOR x35 -> qjb
ngk XOR vvf -> z04
kht OR gfk -> cds
bgb OR tnr -> vnq
kns XOR gvt -> z33
sjt OR pbd -> vch
hvp OR nfk -> pth
x38 AND y38 -> dtt
y18 AND x18 -> pjr
x07 XOR y07 -> mqt
gst OR bmm -> nwb
y21 XOR x21 -> qbm
jwk AND gfr -> cph
nvk XOR brp -> z31
x17 AND y17 -> nkr
sqt OR nqs -> kns
qbs OR vht -> sfw
brp AND nvk -> rfn
hrs AND mvf -> jbj
x12 AND y12 -> bgb
y36 XOR x36 -> sqq
jdb OR ccs -> bkg
x04 XOR y04 -> vvf
y19 XOR x19 -> vmj
vms OR vpb -> kmq
y35 AND x35 -> wcs
vph AND jjr -> qbs
fgt AND sqq -> bmm
vcf AND btn -> fbb
wjk OR ktk -> kmn
x08 AND y08 -> cfk
y01 XOR x01 -> fcg
y23 AND x23 -> vht
kgm AND nkt -> dgc
swb XOR qvq -> z18
x09 XOR y09 -> jnf
cch XOR mcf -> z43
sgn XOR smv -> z15
y40 XOR x40 -> wdj
gnw OR gdd -> trn
dgn OR pqt -> hjg
y30 AND x30 -> trs
ngk AND vvf -> hpm
y12 XOR x12 -> bwv
kmn XOR dmk -> z11
y20 AND x20 -> jmv
stt XOR wcr -> z27
vph XOR jjr -> z23
nmv OR wjj -> gfr
x02 XOR y02 -> jdc
y28 XOR x28 -> kgm
gfr XOR jwk -> z34
x16 AND y16 -> hvp
gkb OR mgv -> z45
mhh AND hbg -> sqt
fqf XOR jwq -> z08
x13 AND y13 -> hwb
vmj AND crc -> pbd
dwg AND fsh -> brb
sfw AND skp -> qjj
knc XOR wcq -> z05
x31 XOR y31 -> brp
fcg XOR pjf -> z01
dqw OR brb -> btn
cvn AND gmp -> trk
y16 XOR x16 -> jhn
y27 XOR x27 -> wcr
x33 XOR y33 -> gvt
y08 XOR x08 -> jwq
trn AND pgk -> hsk
nkt XOR kgm -> z28
y15 AND x15 -> sqw
crc XOR vmj -> z19
hbg XOR mhh -> z32
smv AND sgn -> qkc
vcr XOR nwb -> z37
x14 AND y14 -> kbk
jhn XOR hjd -> z16
x10 AND y10 -> ktk
kmq AND jdc -> ssj
y15 XOR x15 -> smv
sqd OR dtt -> mdn
x24 AND y24 -> wkt
hgg OR cph -> kjr
ktd XOR tgj -> z25
ctf AND tnm -> wpm
x40 AND y40 -> wtv
x10 XOR y10 -> wfd
y33 AND x33 -> wjj
x39 AND y39 -> rrn
y03 XOR x03 -> fpt
x31 AND y31 -> pmm
y32 AND x32 -> nqs
x11 XOR y11 -> dmk
y18 XOR x18 -> qvq
x37 AND y37 -> dgn
skq OR rsw -> wsh
vch XOR css -> z20
kmn AND dmk -> skq
ghm AND hjg -> sqd
kjr AND qjb -> rpr
y01 AND x01 -> vpb
cpw AND dph -> gkb
y26 AND x26 -> rdq
tgj AND ktd -> kht
x26 XOR y26 -> wws
sfw XOR skp -> z24
y42 AND x42 -> thc
nkr OR hns -> swb
y20 XOR x20 -> css
vcr AND nwb -> pqt
fbb OR thc -> mcf
x06 AND y06 -> vts
jdc XOR kmq -> z02
y25 AND x25 -> gfk"""

def forward(values, gates):
    change = True
    while change:
        change = False
        for i in gates.split("\n"):
            a, op, b, arr, res = i.split(" ")
            match op:
                case "OR":
                    if (values[a] or values[b]) and not values[res]:
                        change = True
                        values[res] = 1
                    elif (not (values[a] or values[b])) and values[res]:
                        change = True
                        values[res] = 0
                case "AND":
                    if (values[a] and values[b]) and not values[res]:
                        change = True
                        values[res] = 1
                    elif (not (values[a] and values[b])) and values[res]:
                        change = True
                        values[res] = 0
                case "XOR":
                    if (values[a] ^ values[b]) and not values[res]:
                        change = True
                        values[res] = 1
                    elif (not (values[a] ^ values[b])) and values[res]:
                        change = True
                        values[res] = 0

    return values

startingValues, gates = data.split("\n\n")
values = {i: 0 for i in re.findall(r"[a-z]\w+", data)}

# for i in startingValues.split("\n"):
#     values[i[:3]] = int(i[-1])

# values = forward(values, gates)

# result = ""
# for i in sorted(filter(lambda i:i[0]=="z", values.keys()), reverse=True):
#     result += str(values[i])
# print(int(result, 2))

for i in sorted(filter(lambda x:x[0]=="x", values.keys())):
    values = {i: 0 for i in re.findall(r"[a-z]\w+", data)}
    values[i] = 1
    #values["x"+i[1:]] = 1
    result = forward(values, gates)

#    if result["z"+str(int(i[1:])+1).zfill(2)] != 1:
#        pass
    if result["z"+i[1:]] != 1:
        pass

    # swap z05 and gdd
    # swap cwt and z09
    # swap jmv and css
    # swap pqt and z37
# region z05
    # x05 -> wcq trn z06 gdd

    # x05 XOR y05 -> wcq # good
    # y05 AND x05 -> z05 # prob gdd
    # knc XOR wcq -> gdd # prob z05
    # wcq AND knc -> gnw
    # gnw OR  gdd -> trn # trn = c out
    # trn XOR pgk -> z06 # prob good

    # hpm OR mrw -> knc # knc = carry inn
    # y04 AND x04 -> mrw
# endregion
# region x09
    # x09 -> cwt jnf z10

    # x09 AND y09 -> sgj
    # x09 XOR y09 -> jnf
    # jnf AND wgh -> kvg
    # jnf XOR wgh -> cwt
    # kvg OR  sgj -> z09


# endregion
# region x20
    # x20 -> jgb z21 jmv

    # y20 XOR x20 -> jmv # wrong
    # y20 AND x20 -> css # wrong
    # vch XOR css -> z20
    # vch AND css -> cjn
    # cjn OR jmv -> jgb
    
    # vch = c inn

# endregion
# region x37
    # x37 -> vcr hjg z38 pqt

    # x37 AND y37 -> dgn
    # y37 XOR x37 -> vcr
    # dgn OR pqt -> hjg
    # vcr XOR nwb -> pqt
    # vcr AND nwb -> z37

    # ghm AND hjg -> sqd

# endregion
# region rest
    # y05 -> wcq trn z06 gdd
    # y09 -> cwt jnf z10
    # y20 -> jgb z21 jmv
    # y37 -> vcrhjg z38 pqt

    # wrong
    # y05 AND x05 -> z05
# endregion
