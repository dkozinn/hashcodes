#!/usr/bin/env python3

""" An implementation of hashcodes.f90 in python.

This is a Python implementation of hashcodes.f90 from WSJT-X. The source code
for hashcodes.f90 is available from the ARRL QEX Additional Resources archive
at https://www.arrl.org/files/file/QEX%20Binaries/2020/ft4_ft8_protocols.tgz
from "The FT4 and FT8 Communications Protocols" published in the July/August
2020 issue of QEX written by Steve Franke, K9AN, Bill Somerville, G4WJS (SK),
and Joe Taylor, K1JT.

Python implementation author: David Kozinn, K2DBK

"""
import sys

NTOKENS = 2063592
NPRIME = 47055833459
n8 = [0, 0, 0]
nbits = [10, 12, 22]
ihash = [0, 0, 0]
C = " 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ/"

if len(sys.argv) != 2:
    print(f"Usage:    {sys.argv[0]} <callsign>")
    print(f"Examples: {sys.argv[0]} PJ4/K1ABC")
    print(f"          {sys.argv[0]} YW18FIFA")
    sys.exit(1)

callsign = sys.argv[1]
callsign = callsign.strip().ljust(11).upper()

for k in range(3):  # k = num of bits for hash
    for i in range(11):  # i = index into callsign
        j = C.index(callsign[i])
        n8[k] = 38 * n8[k] + j
    ihash[k] = ((NPRIME * n8[k]) >> abs(nbits[k] - 64)) % 2 ** nbits[k]

IH22_BIASED = ihash[2] + NTOKENS
print("Callsign    h10        h12          h22")
print("---------------------------------------")
print(f"{callsign:<11} {ihash[0]:<9} {ihash[1]:<9} {ihash[2]:<9}")
print(f"Biased for storage in c28: {IH22_BIASED}")
