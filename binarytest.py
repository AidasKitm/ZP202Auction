# Binary data conversion to human language

# 256
# 0   1   1   0   0   0   1   0
# 128 64  32   16   8   4   2   1
# 64+32+2= 98

binary_data = 0o0101010
number = chr(binary_data)
print(number)
