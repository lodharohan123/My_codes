##palindrome project
s=input("enter string")
s1=s.replace('',"")
rev=s1[::-1]
if(s1.casefold()==rev.casefold()):
  print(s)
else:
  palindrome=s1.casefold()+rev.casefold()
  print(palindrome)

