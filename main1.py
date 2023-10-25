#vezérlési szerkezetek

#páros számok
for i in range(1,10):
  if i%2==0:
    print(i,end=" ")

def paros(val):
  print("\n\nPárosak:")
  for i in range(1,val):
    if i%2==0:
      print(i,end=" ")

paros(21)

def paratlan(var):
  print("\nPáratlanok:")
  for i in range(1,var):
    if i%2!=0:
      print(i,end=" ")

paratlan(21)
print("\n\n\n")
paros(int(input("Adjon egy számot:")))

x=int(input("Kérek egy páros számot:"))
while x%2!=0:
  x=int(input("Kérek egy páros számot:"))
print(x)