# lower

a="whiskey"
print(a.lower())

# UPPER  
print(a.upper())

#title
print(a.title())

#Captilize
print(a.capitalize())

#find
print(a.find('s',6))
print(a.find('S')) # agar ni mila to -1 dega

#index
print(a.index('k')) # agar ni ila to error dega

#isaplha
print(a.isalpha())

#isdigit                 isdigit,isaplha,isalnum space and specail charchter give false
w="1249"
print(w.isdigit())
 
# isalnum
m="man72379"
print(m.isalnum())


# chr() -   this takes integer and coverts into charchter
a=chr(98)
print(a)

a=65
print(chr(a))


# ord() -  this takes a single unicode charchter and returns an integer,

y=ord('A')
print(y)
y=ord('a')
print(y)