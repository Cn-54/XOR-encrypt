import sys





def encrypt(content,key):
    output = []
    for byte in content:
        output.append(byte^key)
    return bytes(output)



english_freq = {
    'e': 12.7, 't': 9.1, 'a': 8.2, 'o': 7.5, 'i': 7.0,
    'n': 6.7, 's': 6.3, 'h': 6.1, 'r': 6.0, 'd': 4.3,
    'l': 4.0, 'c': 2.8, 'u': 2.8, 'm': 2.4, 'w': 2.4,
    'f': 2.2, 'g': 2.0, 'y': 2.0, 'p': 1.9, 'b': 1.5,
}
def score(content):
    total = 0
    for byte in content:
        char = chr(byte).lower()
        if char in english_freq:
            total += english_freq[char]
    return total

def crack(content):
    results = []
    for key in range(256):
        attempt = encrypt(content, key)
        results.append((score(attempt), key, attempt))
    results.sort(reverse=True)
    top = results[0]
    print(f"most likely key: {top[1]} ({chr(top[1])})")
    print(f"decoded: {top[2].decode('utf-8', errors='replace')}")
    print("\ntop 5 candidates:")
    for s, k, attempt in results[:5]:
        print(f"  key {k} ({chr(k)}): {attempt.decode('utf-8', errors='replace')[:50]}")



def brute(content):
    for key in range(256):
        attempt = bytes([b ^ key for b in content])
        try:
            decoded = attempt.decode('utf-8')
        except:
            decoded = repr(attempt)
        print(f"key {key} ({chr(key) if 32 <= key <= 126 else '?'}): {decoded}")
        

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python xor.py <encrypt/decrypt> <file> <key>")
        sys.exit(1)
    type = sys.argv[1]
    filepath = sys.argv[2]

    match type.upper():
        case "ENCRYPT" | "DECRYPT":
            if len(sys.argv) < 4:
                print("encrypt/decrypt requires a key")
                sys.exit(1)
            if len(sys.argv[3]) != 1:
                print("key must be a single character")
                sys.exit(1)
            key = ord(sys.argv[3])
            with open(filepath, 'rb') as file:
                content = file.read()
            result = encrypt(content, key)
            if type.upper() == "ENCRYPT":
                outpath = filepath + ".enc"
            else:
                outpath = filepath.replace(".enc", ".dec")
            with open(outpath, 'wb') as file:
                file.write(result)
            print(f"done: {outpath}")

        case "BRUTE":
            with open(filepath, 'rb') as file:
                content = file.read()
            brute(content)
        case "CRACK":
            with open(filepath, 'rb') as file:
                content = file.read()
            crack(content)
        