# hashcodes

This is an implementation of hashcodes.f90 in Python. The source code for
hashcodes.f90 is available from the [ARRL QEX Additional Resources archive](https://www.arrl.org/files/file/QEX%20Binaries/2020/ft4_ft8_protocols.tgz)
as part of the article
"[The FT4 and FT8 Communications Protocols](https://wsjt.sourceforge.io/FT4_FT8_QEX.pdf)" published in the July/August
2020 issue of QEX written by Steve Franke, K9AN, Bill Somerville, G4WJS (SK),
and Joe Taylor, K1JT.

Run hashcodes.py from the command line. Provide a callsign as an argument and
it will provide the 10, 12, and 22 bit hashcodes as calculated by WSJT-X.

This can be useful to determine if two callsigns generate the same hash, which
can result in what appears to be an incorrect decode.

Included in this repository is a small application using Flask that can be hosted on a website. A WSGI 
server is needed to host the application. My implementation uses nginx as the server and uWSGI as the
WSGI interface. 

I recommend reviewing and modifying the install.sh script before using it. This, along with some of the 
support files expect that the code will be run under /home/ubunbtu as it's root. You'll need to adjust that for your
environment.
