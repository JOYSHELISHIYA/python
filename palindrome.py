a = int(input());
b = a;
rev = 0;
while(a!=0):
  rem = a%10;
  rev = rev*10+rem;
  a = a//10;
if(rev==b):
  print("yes");
else:
  print("no");
