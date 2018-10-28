hh,mm = input('').split(':')
hh = int(hh)
mm = int(mm)
if hh < 5:
    hh2 = hh+2
    hh = str(hh)
    mm = str(mm)
    print("0",hh2,":",mm,sep="")
