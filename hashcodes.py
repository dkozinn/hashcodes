#!/usr/bin/env python3

""" An implementation of hashcodes.f90 in python.

This is a Python implementation of hashcodes.f90 from WSJT-X. The source code
for hashcodes.f90 is available from the ARRL QEX Additional Resources archive
at https://www.arrl.org/files/file/QEX%20Binaries/2020/ft4_ft8_protocols.tgz
from "The FT4 and FT8 Communications Protocols" published in the July/August
2020 issue of QEX written by Steve Franke, K9AN, Bill Somerville, G4WJS (SK),
and Joe Taylor, K1JT.

Python implementation author: David Kozinn, K2DBK

5 Dec 2023 Reino Talarmo, OH3mA
A common hash base calculated before the calculation of the individual hashes
"""
import sys


def calc_hash(callsign: str):
    """ Calculate WSJT-X callsign hash.
    Args:
        callsign (str): Callsign to process. Will be converted to uppercase
            and padded/truncated to 11 characters.

    Returns:
        callsign: processed callsign
        ihash: list of hashes for 10, 12, and 22 bits
        biased storage size
    """

    ntokens = 2063592
    nprime = 47055833459
    n8 = 0
    nbits = [10, 12, 22]
    ihash = [0, 0, 0]
    c = " 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ/"

    callsign = callsign.strip().ljust(11).upper()

    for i in range(11):
        j = c.index(callsign[i])
        n8 = 38 * n8 + j

    for k in range(3):
        ihash[k] = ((nprime * n8) >> abs(nbits[k] - 64)) % 2 ** nbits[k]

    return callsign, ihash, ihash[0] + ntokens


def main():
    """ Run calc_hash() with input on command line """
    if len(sys.argv) != 2:
        print(f"Usage:    {sys.argv[0]} <callsign>")
        print(f"Examples: {sys.argv[0]} PJ4/K1ABC")
        print(f"          {sys.argv[0]} YW18FIFA")
        sys.exit(1)

    callsign, ihash, ih22_biased = calc_hash(sys.argv[1])

    print("Callsign    h10        h12          h22")
    print("---------------------------------------")
    print(f"{callsign:<11} {ihash[0]:<9} {ihash[1]:<9} {ihash[2]:<9}")
    print(f"Biased for storage in c28: {ih22_biased}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
