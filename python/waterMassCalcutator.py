# amount of flowing water blocks at the top of layer n
def l(n):
    return 15 * 7 * (2 * n + 1) - 2 * (7 * n - 4) - 1

y = 319
n = 1
sum = 384
while y >= -64:
    sum += l(n) * (y + 65)
    y -= 1
    n += 1

print(sum)
#9_697_039_134_695_424_000
#9697039134695424000 kg
# around 1_643_565_955 times as heavy as the pyramid of giza
# or 10_666_743 times as heavy as the meteor that killed the dinosaures
# but nowhere close to your mom