# Muhammad Saleem
# Hashcash-like Proof of Work Verifier.
import sys
import hashlib


# This method reads the header file and
# stores necessary values in an array for comparison.
# and then verifies if the proof of work is correct.

def pow_check(headerfile, filename):
    try:
        file = open(headerfile, "r")
        verify_array = {}
        # Storing important fields into the array.
        for line in file:
            split = line.split(":")
            field = split[0]
            entry = split[1]
            len_entry = len(entry) - 1
            entry = entry[0:len_entry]
            verify_array[field] = entry
        # Retrieving Important values from the array.
        initial_hash = verify_array['Initial-hash'].lstrip()
        proof_of_work = verify_array['Proof-of-work'].lstrip()
        confirmation_hash = verify_array['Hash'].lstrip()
        leading_zeros_check = verify_array['Leading-bits'].lstrip()
        cflag = True
    except:
        print("Provided header file is faulty.")
        return
    try:
        with open(filename, "rb") as f:
            bytes = f.read()  # read entire file as bytes
            readable_hash = hashlib.sha256(bytes).hexdigest().encode('utf-8');
            if initial_hash == readable_hash:
                pass

            else:
                print('Failure Wrong Initial Hash')
                cflag = False
            final_hash = hashlib.sha256(proof_of_work + initial_hash).hexdigest();
            if final_hash == confirmation_hash:
                pass

            else:
                print('Failure Wrong Hash')
                cflag = False
            if str(leading_zeros(final_hash)) == leading_zeros_check:
                pass
            else:
                print('Failure Wrong Leading Bits')
                cflag = False
            if cflag:
                print('pass')
    except:
        print("Provided hash file doesn't exist.")
        return

# Returns leading zero bits from the final hash.
def leading_zeros(final_hash):
    h_size = len(final_hash) * 4
    h_zero = (bin(int(final_hash, 16))[2:]).zfill(h_size)
    zero_lead = len(h_zero) - len(h_zero.lstrip('0'))
    return zero_lead

# Main method to the run the file.
if __name__ == '__main__':
    pow_check(sys.argv[1], sys.argv[2])
# EXAMPLE: python pow-check.py POW-Walrus.txt Walrus.txt
