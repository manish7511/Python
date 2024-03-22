# format()-  format he specified value(s) and insert the inside the string placeholder
# PLACEHOLDER IS DEFINED Using curlybrackets {}

txt1="welcome to {fname:<10} {lname:>15}".format(fname="manish",lname="kumar")
print(txt1)

txt2="welcome to {1} {0}".format("manish",20)
print(txt2)
txt3="welcome to {} {}".format("manish","kumar")
print(txt3) 
