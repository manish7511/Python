# & AND	Result bit 1,if both operand bits are 1;otherwise results bit 0.
#   a = 10 = 1010 (Binary)
#   b = 4 =  0100 (Binary)

#   a & b = 1010
#            &
#           0100
#         = 0000
#         = 0 (Decimal)
x=10
y=8
print(bin(x))
print(bin(y))

print(bin(x&y),x&y)

# 2. Bitwise or operator Returns 1 if either of the bit is 1 else 0.

# a = 10 = 1010 (Binary)
# b = 4 =  0100 (Binary)

# a | b = 1010
#          |
#         0100
#       = 1110
#       = 14 (Decimal)
print(bin(x|y),x|y)

# 3. xor Returns 1 if one of the bits is 1 and the other is 0 else returns false.

# a = 10 = 1010 (Binary)
# b = 4 =  0100 (Binary)

# a ^ b = 1010
#          ^
#         0100
#       = 1110
#       = 14 (Decimal)

print(bin(x^y),x^y)


