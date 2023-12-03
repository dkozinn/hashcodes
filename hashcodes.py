
NTOKENS = 2063592
nprime = 47055833459
n8 = [0, 0, 0]
nbits = [10, 12, 22]
ihash = [0, 0, 0]
callsign = ''
c = ' 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ/'

#nargs = len(sys.argv) - 1
# if nargs != 1:
#     print('Usage:    hashcodes <callsign>')
#     print('Examples: hashcodes PJ4/K1ABC')
#     print('          hashcodes YW18FIFA')
#     sys.exit()

# callsign = sys.argv[1]
callsign = "k2dbk  "  # K2DBK 584 2339 2396005
callsign = callsign.strip().ljust(11).upper()

for k in range(3):  # k = num of bits for hash
    for i in range(11): # i = index into callsign
        j = c.index(callsign[i]) # - 1 not needed, python array index start is 0
        n8[k] = 38 * n8[k] + j
    ihash[k] = ((nprime * n8[k]) >> abs(nbits[k] - 64)) % 2**nbits[k]

ih22_biased =(ihash[2] + NTOKENS) % 64
print('Callsign         h10         h12         h22')
print('-------------------------------------------')
print(f'{callsign:<11} {ihash[0]:<9} {ihash[1]:<9} {ihash[2]:<9}')
print(f'Biased for storage in c28: {ih22_biased}')
