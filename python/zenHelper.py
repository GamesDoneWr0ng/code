import random
zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

letters = set(zen)
chars = list(sorted(set(open("zen.py").read())))
print(chars)
print(len(chars))

parts = 2
step = 4
assert len(zen) % (parts * step) == 0
result = {i: [0 for i in range(parts)] for i in chars}

# targets = {zen[i*step:i*step+step]: chars[i//parts] for i in range(len(zen)//step)}
#
# seed = 0
# found = 0
# while found < len(targets):
#     rng = random.Random(seed)
#     key = "".join(chr(rng.randint(10,121)) for k in range(step))
#     if key in targets:
#         idx = sorted(i for i in targets if targets[i] == targets[key]).index(key)
#         if result[targets[key]][idx] == 0:
#             result[targets[key]][idx] = seed
#             found += 1
#             print(f"key: {key.replace('\n','\\n')}  letter: {targets[key].replace('\n','\\n')}  seed: {seed}  found: {found}/{len(targets)}")
#     seed += 1
# #    if seed % 1000000 == 0:
# #        print(f"seed: {seed}")
#
# print(result)

# import re
# x = """key: impl  letter: .  seed: 233200  found: 4
# key: ter   letter: 5  seed: 450379  found: 8
# key: way   letter: h  seed: 1941682  found: 12
# key: y on  letter: c  seed: 4112576  found: 16
# key: .
# Sp  letter: ;  seed: 4641713  found: 20
# key: rror  letter: M  seed: 5016094  found: 24
# key:  har  letter: |  seed: 5346995  found: 28
# key: Name  letter: ι  seed: 6396205  found: 32
# key: plex  letter: 2  seed: 6852711  found: 36
# key:  fac  letter: U  seed: 7571928  found: 40
# key: thou  letter: g  seed: 10565140  found: 44
# key: tion  letter: γ  seed: 11253188  found: 48
# key: gh t  letter: g  seed: 11674596  found: 52
# key: a.
# I  letter: ͷ  seed: 12534684  found: 56
# key: lain  letter: ~  seed: 12813440  found: 60
# key: lity  letter: J  seed: 13495979  found: 64
# key: r is  letter: t  seed: 13797478  found: 68
# key:  is   letter: γ  seed: 16039960  found: 72
# key: expl  letter: ε  seed: 16664238  found: 76
# key:  are  letter: C  seed: 17591712  found: 80
# key: .
# Co  letter: 3  seed: 20352681  found: 84
# key: ss y  letter: m  seed: 24179171  found: 88
# key:  let  letter: ϛ  seed: 24675087  found: 92
# key: bvio  letter: j  seed: 24747444  found: 96
# key: rule  letter: G  seed: 26486996  found: 100
# key: re o  letter: ϝ  seed: 27187854  found: 104
# key: ltho  letter: r  seed: 27439575  found: 108
# key: ters  letter: "  seed: 27484344  found: 112
# key: an u  letter: (  seed: 27658597  found: 116
# key: empt  letter: Y  seed: 28486416  found: 120
# key: t fi  letter: k  seed: 29924953  found: 124
# key: ous   letter: d  seed: 33656613  found: 128
# key: t* n  letter: w  seed: 35022865  found: 132
# key: prac  letter: I  seed: 36947368  found: 136
# key: s be  letter: 8  seed: 37077747  found: 140
# key: efer  letter: a  seed: 37192662  found: 144
# key: s.
# A  letter: H  seed: 38383402  found: 148
# key:
# Now  letter: o  seed: 39720887  found: 152
# key: s sh  letter: M  seed: 41448173  found: 156
# key: ou'r  letter: m  seed: 44038031  found: 160
# key: ial   letter: D  seed: 45005250  found: 164
# key: us a  letter: k  seed: 45269416  found: 168
# key: ty c  letter: @  seed: 48208806  found: 172
# key:
# Exp  letter: )  seed: 48618989  found: 176
# key: es a  letter: κ  seed: 50043037  found: 180
# key: Ther  letter: ]  seed: 50360838  found: 184
# key: .
# Al  letter: f  seed: 50400049  found: 188
# key: ytho  letter:    seed: 50603176  found: 192
# key: ose!  letter: ϳ  seed: 51286535  found: 196
# key: nced  letter: T  seed: 51914634  found: 200
# key: e of  letter: V  seed: 53741454  found: 204
# key: ss.
#   letter: [  seed: 54657443  found: 208
# key:  exp  letter: }  seed: 55865877  found: 212
# key: tica  letter: J  seed: 57064114  found: 216
# key:  imp  letter: -  seed: 57963334  found: 220
# key: reat  letter: μ  seed: 57993925  found: 224
# key: ow.
#   letter: x  seed: 58178188  found: 228
# key: n, b  letter: !  seed: 58669051  found: 232
# key: bili  letter: ?  seed: 59230550  found: 236
# key: o it  letter: f  seed: 59509909  found: 240
# key:  be   letter: ^  seed: 59737914  found: 244
# key: Zen   letter:
#   seed: 62391708  found: 248
# key: e is  letter: 0  seed: 63034088  found: 252
# key: plic  letter: 6  seed: 63056167  found: 256
# key: ass   letter: O  seed: 64453240  found: 260
# key: e.
# R  letter: >  seed: 68139977  found: 264
# key: one-  letter: _  seed: 68581964  found: 268
# key: ugh   letter: s  seed: 71336163  found: 272
# key:
#
# Be  letter: #  seed: 73224597  found: 276
# key: ases  letter: B  seed: 73592839  found: 280
# key: ain,  letter: ε  seed: 74267552  found: 284
# key: urit  letter: L  seed: 74429620  found: 288
# key: n to  letter: Z  seed: 77186263  found: 292
# key: ne h  letter: λ  seed: 78518770  found: 296
# key: o br  letter: F  seed: 78585093  found: 300
# key: e sh  letter: ]  seed: 81965930  found: 304
# key: be a  letter: η  seed: 84557424  found: 308
# key: f th  letter: ϳ  seed: 85466802  found: 312
# key: y Ti  letter: !  seed: 88973771  found: 316
# key: n't   letter: C  seed: 89760213  found: 320
# key: er t  letter: p  seed: 90709325  found: 324
# key:  the  letter: U  seed: 92034450  found: 328
# key: not   letter: i  seed: 95642892  found: 332
# key: the   letter: G  seed: 95672877  found: 336
# key: dens  letter: >  seed: 95765104  found: 340
# key: t is  letter: *  seed: 96327418  found: 344
# key: r th  letter: v  seed: 98005030  found: 348
# key: mple  letter: y  seed: 102241374  found: 352
# key: e Du  letter: n  seed: 103790128  found: 356
# key:  amb  letter: V  seed: 104644834  found: 360
# key: ated  letter: 7  seed: 111702127  found: 364
# key: is b  letter: %  seed: 114658983  found: 368
# key: x is  letter: 4  seed: 115934454  found: 372
# key: t.
# S  letter: .  seed: 116582381  found: 376
# key: d pr  letter: a  seed: 116762182  found: 380
# key: lici  letter: R  seed: 118782685  found: 384
# key: o mo  letter: ϝ  seed: 122325891  found: 388
# key: se t  letter: X  seed: 123343965  found: 392
# key: bett  letter: p  seed: 126565734  found: 396
# key: spec  letter: D  seed: 127480667  found: 400
# key:  onl  letter: b  seed: 129412182  found: 404
# key: rst   letter: l  seed: 130372744  found: 408
# key: The   letter:
#   seed: 131539809  found: 412
# key: er p  letter: O  seed: 131990558  found: 416
# key: en b  letter: u  seed: 138186834  found: 420
# key:  goo  letter: η  seed: 141363478  found: 424
# key:  nev  letter: N  seed: 143060123  found: 428
# key: .
# Un  letter: Q  seed: 143328839  found: 432
# key: r.
# A  letter: r  seed: 145227410  found: 436
# key: ful   letter: %  seed: 145670073  found: 440
# key:  it   letter: ζ  seed: 150165881  found: 444
# key: s.
# S  letter: A  seed: 150618409  found: 448
# key: enta  letter: β  seed: 156282483  found: 452
# key: tter  letter: 9  seed: 157346355  found: 456
# key: easy  letter: δ  seed: 157860746  found: 460
# key: a --  letter: ν  seed: 158672243  found: 464
# key: e im  letter: α  seed: 159992850  found: 468
# key: atio  letter: {  seed: 163131054  found: 472
# key: neve  letter: s  seed: 171740362  found: 476
# key: less  letter: Q  seed: 179397520  found: 480
# key: peci  letter: A  seed: 180664860  found: 484
# key: If t  letter: x  seed: 185142541  found: 488
# key:  com  letter: 6  seed: 185357459  found: 492
# key: ount  letter: @  seed: 186511796  found: 496
# key: tch.  letter: n  seed: 191175115  found: 500
# key:  oft  letter: t  seed: 192635623  found: 504
# key: may   letter: ζ  seed: 199791110  found: 508
# key: ould  letter: ^  seed: 205520475  found: 512
# key: plem  letter: β  seed: 207142820  found: 516
# key: spac  letter: ι  seed: 208220183  found: 520
# key: d id  letter: θ  seed: 208953631  found: 524
# key: auti  letter: #  seed: 209200751  found: 528
# key: ment  letter: {  seed: 213259301  found: 532
# key: ntly  letter: P  seed: 219115128  found: 536
# key: igui  letter: W  seed: 220811523  found: 540
# key: at i  letter: 8  seed: 221381330  found: 544
# key: be o  letter: j  seed: 223281736  found: 548
# key: onki  letter: λ  seed: 227238769  found: 552
# key: arse  letter: ;  seed: 227484735  found: 556
# key: n ne  letter: :  seed: 235593842  found: 560
# key: enou  letter: E  seed: 247349008  found: 564
# key:  bea  letter: K  seed: 248807122  found: 568
# key:  to   letter: δ  seed: 255664356  found: 572
# key: tly   letter: S  seed: 257304738  found: 576
# key: .
# Fl  letter: 7  seed: 258340909  found: 580
# key: to d  letter: e  seed: 265003210  found: 584
# key: , it  letter: ~  seed: 277161634  found: 588
# key: eak   letter: F  seed: 286775654  found: 592
# key: y.
# E  letter: L  seed: 289050974  found: 596
# key: eada  letter: ?  seed: 291297874  found: 600
# key: he t  letter: Y  seed: 291474455  found: 604
# key: ably  letter: b  seed: 298658890  found: 608
# key: m Pe  letter: "  seed: 310717496  found: 612
# key:  bet  letter: 4  seed: 322873572  found: 616
# key: n is  letter: |  seed: 323034535  found: 620
# key: 's a  letter: ͱ  seed: 341014253  found: 624
# key: of P  letter:    seed: 342109267  found: 628
# key: sted  letter: :  seed: 342759225  found: 632
# key: righ  letter: w  seed: 349384515  found: 636
# key: unle  letter: l  seed: 351136104  found: 640
# key: hat   letter: h  seed: 354602885  found: 644
# key: gly.  letter: (  seed: 359025670  found: 648
# key:  tha  letter: 9  seed: 363689336  found: 652
# key: han   letter: q  seed: 380435276  found: 656
# key:  bad  letter: ͱ  seed: 395965381  found: 660
# key: refu  letter: X  seed: 425036848  found: 664
# key: ty,   letter: W  seed: 429246170  found: 668
# key: - an  letter: _  seed: 433257006  found: 672
# key: than  letter: 5  seed: 434889969  found: 676
# key: 's d  letter: ϛ  seed: 456509331  found: 680
# key: ng g  letter: μ  seed: 465094888  found: 684
# key: sile  letter: S  seed: 467156736  found: 688
# key: ette  letter: u  seed: 494566494  found: 692
# key: .
# In  letter: T  seed: 496531772  found: 696
# key: e --  letter: c  seed: 555016234  found: 700
# key: al c  letter: B  seed: 571442855  found: 704
# key:  ide  letter: ν  seed: 594174600  found: 708
# key: ts p  letter: K  seed: 599090622  found: 712
# key: an *  letter: v  seed: 628001241  found: 716
# key: ea.
#   letter: θ  seed: 679479209  found: 720
# key: d to  letter: }  seed: 736719868  found: 724
# key: obvi  letter: d  seed: 753023204  found: 728
# key:  gue  letter: [  seed: 754222734  found: 732
# key: he i  letter: y  seed: 762456942  found: 736"""
#
# seeds = []
# for seed in re.finditer(r'\d{6,}', x):
#     seeds.append(int(seed.group()))
# print(seeds)
#
# for seed in seeds:
#     rng = random.Random(seed)
#     key = "".join(chr(rng.randint(10,121)) for k in range(step))
#     idx = -1
#     while (idx := zen.find(key, idx+1)) != -1:
#         if idx % step == 0:
#             result[chars[idx//step//parts]][(idx//step)%parts] = seed
#
# print(result)
# for char in chars:
#     for j in range(parts):
#         rng = random.Random(result[char][j])
#         for k in range(step):
#             print(chr(rng.randint(10,121)), end="")



result = {'\n': [131539809, 62391708], ' ': [342109267, 50603176], '!': [58669051, 88973771],
'"': [310717496, 27484344], '#': [73224597, 209200751], '%': [145670073, 114658983], '&': [494566494, 98005030],
'(': [27658597, 359025670], ')': [48618989, 118782685], '*': [96327418, 322873572], ',': [450379, 434889969],
'-': [57963334, 118782685], '.': [116582381, 233200], '0': [63034088, 322873572], '1': [450379, 434889969],
'2': [185357459, 6852711], '3': [20352681, 102241374], '4': [115934454, 322873572], '5': [450379, 434889969],
'6': [185357459, 63056167], '7': [111702127, 258340909], '8': [221381330, 37077747], '9': [157346355, 363689336],
':': [235593842, 342759225], ';': [4641713, 227484735], '<': [16039960, 126565734], '=': [90709325, 380435276],
'>': [95765104, 68139977], '?': [291297874, 59230550], '@': [48208806, 186511796], 'A': [150618409, 180664860],
'B': [571442855, 73592839], 'C': [17591712, 89760213], 'D': [127480667, 45005250], 'E': [247349008, 11674596],
'F': [78585093, 286775654], 'G': [95672877, 26486996], 'H': [38383402, 27439575], 'I': [71336163, 36947368],
'J': [57064114, 13495979], 'K': [248807122, 599090622], 'L': [74429620, 289050974], 'M': [5016094, 41448173],
'N': [205520475, 143060123], 'O': [131990558, 64453240], 'P': [467156736, 219115128], 'Q': [143328839, 179397520],
'R': [55865877, 118782685], 'S': [257304738, 467156736], 'T': [51914634, 496531772], 'U': [92034450, 7571928],
'V': [53741454, 104644834], 'W': [220811523, 429246170], 'X': [425036848, 123343965], 'Y': [291474455, 28486416],
'Z': [163131054, 77186263], '[': [754222734, 54657443], ']': [50360838, 81965930], '^': [205520475, 59737914],
'_': [68581964, 433257006], 'a': [116762182, 37192662], 'b': [298658890, 129412182], 'c': [4112576, 555016234],
'd': [753023204, 33656613], 'e': [1941682, 265003210], 'f': [59509909, 50400049], 'g': [10565140, 11674596],
'h': [354602885, 1941682], 'i': [199791110, 95642892], 'j': [223281736, 24747444], 'k': [45269416, 29924953],
'l': [130372744, 351136104], 'm': [24179171, 44038031], 'n': [103790128, 191175115], 'o': [39720887, 16039960],
'p': [126565734, 90709325], 'q': [380435276, 171740362], 'r': [145227410, 27439575], 's': [71336163, 171740362],
't': [13797478, 192635623], 'u': [138186834, 494566494], 'v': [98005030, 628001241], 'w': [349384515, 35022865],
'x': [58178188, 185142541], 'y': [762456942, 102241374], '{': [213259301, 163131054], '|': [323034535, 5346995],
'}': [736719868, 55865877], '~': [12813440, 277161634], 'ͱ': [341014253, 395965381], 'ͷ': [594174600, 12534684],
'α': [85466802, 159992850], 'β': [207142820, 156282483], 'γ': [11253188, 16039960], 'δ': [157860746, 255664356],
'ε': [16664238, 74267552], 'ζ': [150165881, 199791110], 'η': [84557424, 141363478], 'θ': [208953631, 679479209],
'ι': [6396205, 208220183], 'κ': [50043037, 27187854], 'λ': [78518770, 227238769], 'μ': [465094888, 57993925],
'ν': [594174600, 158672243], 'ϛ': [24675087, 456509331], 'ϝ': [122325891, 27187854], 'ϳ': [85466802, 51286535]}

values = list(result.values())
newResult = {chars[i]: values[i] for i in range(107)}

print(newResult)