with open("16.txt") as f:
    hexcodes = f.readline().strip()
#hexcodes = '620080001611562C8802118E34'
#hexcodes = 'C0015000016115A2E0802F182340'
#hexcodes = 'A0016C880162017C3686B18A3D4780'
#hexcodes = '805311100469800804A3E488ACC0B10055D8009548874F65665AD42F60'

bits = ''.join(bin(t)[2:].rjust(8, '0') for t in bytearray.fromhex(hexcodes))

def parse_literal(bits, pos):
    num = ''
    while True:
        #print('chunk at', pos, pos+4)
        chunk = bits[pos:pos+5] 
        #print('  chunk', chunk)
        num += chunk[1:]
        pos += 5

        if chunk[0] == '0':
            #if pos % 4 != 0:
            #   pos += 4 - (pos % 4)
            return (int(num, 2), pos)

def parse_operator(bits, pos, versions, depth):
    def parse_op(bits, pos, totpackets, totbits):
        if totpackets is not None:
            #print(' ' * depth, 'parsing', totpackets, 'subpackets')
            for packet in range(0, totpackets):
                pos = parse(bits, pos, versions, depth + 1)
        elif totbits is not None:
            #print(' ' * depth, 'parsing', totbits, 'subpacket bits')
            pos = parse(bits[:pos + totbits], pos, versions, depth + 1)
        return pos

    i = bits[pos]
    pos += 1

    #print('i', i)

    if i == '0':
        length = int(bits[pos:pos+15], 2)
        pos += 15
        return parse_op(bits, pos, None, length)
    else:
        npackets = int(bits[pos:pos+11], 2)
        pos += 11
        return parse_op(bits, pos, npackets, None)

def parse(bits, pos, versions, depth):

    while pos < len(bits):
        #print(' ' * depth, bits[pos:])

        if all((b == '0' for b in bits[pos:])):
            break

        ver = int(bits[pos:pos+3], 2)
        pos += 3

        #print(' ' * depth, 'ver', ver)
        versions.append(ver)

        typ = int(bits[pos:pos+3], 2)
        pos += 3
        #print(' ' * depth, 'typ', typ)

        if typ == 4: # literal
            #print(' ' * depth, '=> literal')
            (literal, pos) = parse_literal(bits, pos)
            #print('got', literal)
        else: # operator
            #print(' ' * depth, '=> operator')
            pos = parse_operator(bits, pos, versions, depth + 1)

    return pos

#print(bits)

versions = []
parse(bits, 0, versions, 0)
print('part1', sum(versions))