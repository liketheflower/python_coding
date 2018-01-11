n,m = int(raw_input()), int(raw_input())
if len(bin(m))-2<=n:
    print m
else:
    print int('0b'+bin(m)[-n:],2)
