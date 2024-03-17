# format()-  format he specified value(s) and insert the inside the string placeholder
# PLACEHOLDER IS DEFINED Using curlybrackets {}

txt1="welcome to {fname} {lname}".format(fname="manish",lname="kumar")
print(txt1)

txt2="welcome to {0} {1}".format("manish","kumar")
print(txt2)
txt3="welcome to {} {}".format("manish","kumar")
print(txt3) 