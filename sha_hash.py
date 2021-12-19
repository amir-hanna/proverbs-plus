import hashlib

def sha_512(fname):
    hash = hashlib.sha3_512()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()

def sha512_ok(fname, original_hash):
    if sha_512(fname) == original_hash:
        return True
    return False

def main():
    import sys
    # slash argv[0], ie, holding script path and get the rest of command line arguments
    args = sys.argv[1:]
    x = len(args)

    if x == 1:
        print(sha_512(args[0]))
    elif x == 2:
        print(sha512_ok(args[0], args[1]))
    else:
        print("Please enter either:\n    File name to get sha3_512 hash.\n    File name followed by sha3_512 hash to authenticate.")


if __name__ == '__main__':
    main()

#print(sha512_ok('/home/amir/Documents/proverbs.json', 'fef08fec8be3919359bb0780c0e3320d37f49997f6dcd3e2cbf54ecc45a8c912eec80abcec9f394a295b0b16889bfbe2a90a2ca6530ab3a79a45c222168a46d9'))
#print(sha_512('/home/amir/Documents/proverbs.json'))