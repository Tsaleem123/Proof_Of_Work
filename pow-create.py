# Muhammad Saleem
# Hashcash-like Proof of Work
import hashlib
import sys
from itertools import product
from string import ascii_letters, digits
import time


# Tries to create a proof of work for a specific puzzle.
# Puzzle is as follows: Take the SHA-256 hash of the bytes of any file H.
# Then joins that hash H with a text T such that, the resulting string's hash contains
# the specified complexity leading zero bits. This text T is the proof of work.
# (Example leading zero bits of complexity 6: 000000O23OPJFsZ)

def p_create(difficulty, filename):
    ender = difficulty
    flag_found = False
    max_nonce = 1, 000, 000, 000  # Max number of iterations before program closes.
    i_num = 0
    n = 1
    try:
        with open(filename, "rb") as f:
            bytes = f.read()  # Reads entire file as bytes.
            readable_hash = hashlib.sha256(bytes).hexdigest().encode('utf-8');  # Takes SHA256 hash of the bytes read
            # in previous file.
    except:
        print("File does not exist.")
        return
    while not flag_found:
        # This block of code looks for a prefix, when joined with the bytecode hash produces a
        # hash code with the number of leading zero bits equivalent or greater to the specified difficulty.
        for i in product(ascii_letters, digits, '!#$%&\()*+,-./:;?<=>@[\\]^_`{|}~', repeat=n):
            if i_num < max_nonce:
                i_num = i_num + 1
                proof_of_work = ''.join(i) + readable_hash
                final_hash = hashlib.sha256(proof_of_work).hexdigest()
                zeros = leading_zeros(final_hash)
                if zeros >= ender:
                    with open("POW-" + filename, "w+") as f:
                        f.write("File: " + filename + "\n")
                        f.write("Initial-hash: " + readable_hash + "\n")
                        f.write("Proof-of-work: " + ''.join(i) + "\n")
                        f.write("Hash: " + final_hash + "\n")
                        print(final_hash)
                        f.write("Leading-bits: " + str(zeros) + "\n")
                        f.write("Iterations: " + str(i_num) + "\n")
                    return

            else:
                print('Too hard exceeds max nonce')
                return False
        n = n + 1


# This method returns the leading zero bits of the final hash.
def leading_zeros(final_hash):
    h_size = len(final_hash) * 4
    h_zero = (bin(int(final_hash, 16))[2:]).zfill(h_size)
    zero_lead = len(h_zero) - len(h_zero.lstrip('0'))
    return zero_lead

# Main method to run the file.
if __name__ == '__main__':
    start_time = time.time()
    p_create(int(sys.argv[1]), sys.argv[2])
    print("Compute-time: %s " % (time.time() - start_time))

# EXAMPLE: python pow-create.py 2 Walrus.txt
