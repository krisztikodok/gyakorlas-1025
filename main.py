#types
x=int(input("Adjon meg egy egész számot:"))
print('{0} szám típusa ',type(x))

a=3.22
b="Lackó"
c=False
d=6+4j
e=None
tmb=[a,b,c,d,e,x] #list
for i in tmb:
  print(i," = ",type(i))

txt="For just the small price of {money:.2f} dollars!"
print(txt.format(money=49))
