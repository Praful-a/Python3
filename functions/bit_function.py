# num = 7
# print(num.bit_length())

# num = -7
# print(num.bit_length())


# Returns byte representation of 1024 in a big
# endian machine
print((1024).to_bytes(2, byteorder = 'big'))

# Returngs integer value of '\x00\x10' in big endian machine.
print(int.from_bytes(b'\x00\x10', byteorder='big'))
