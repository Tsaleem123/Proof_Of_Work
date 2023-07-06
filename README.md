PROOF OF WORK SYSTEM, AND VERIFIER. (Program tested for python 2.7)

This program is a proof of work similar to hash-cash (system used to show proof of work to reduce spam.), a similar 
application was adapted in bitcoin (and other software) as proof of work for adding a new block to the block chain.

POW CREATE

FORMAT: python pow-create.py "LEADING ZERO BITS COMPLEXITY" "FILE NAME"

This program creates a proof of work for a specified puzzle. This puzzle goes as follows. Take the SHA-256 hash of the bytes of any file namingly H. 
Then join that hash H with a text T such that, the resulting string's hash contains the specified complexity leading zero bits. This text T is the proof
of work. Running this program generates a header file (POW-Filename.txt), containing Filename, Intial Hash, Proof of work, Hash, Leading bits and Iterations.
Some of this information will be used by the pow-create program to verify proof of work. 

POW CHECK

FORMAT: python pow-check.py "HEADERFILE" "FILE NAME"

Verifies if a proof of work is legitmate by examining the header file. Takes the header and extracts Filename, Intial Hash, Proof of work, Hash, Leading bits and Iterations.
Checks the proof-of-work in the file powheader against the original file used the proof of work header.
- Validates the hash in the Initial-hash header
– Computes hash of the Proof-of-work string prepended to the original hash string
– Compares this value with the Hash header
– The Leading-bits data must match the # of leading 0 bits in the Hash header.

EXAMPLES:
py -2.7 pow-create.py 2 Walrus.txt
py -2.7 pow-check.py POW-Walrus.txt Walrus.txt

OVERVIEW:


[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/FlKlKm4gnqw/0.jpg)](https://www.youtube.com/watch?v=FlKlKm4gnqw)
