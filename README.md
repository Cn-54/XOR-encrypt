# XOR Encryptor

A simple XOR encryption tool with 2 built in crackers

## Usage

```bash
python xor.py encrypt <file> <key>
python xor.py decrypt <file> <key>
python xor.py crack <file>
python xor.py crack <file> --verbose
```

## Examples

```bash
python xor.py encrypt test.txt K
python xor.py decrypt test.txt.enc K
python xor.py brute test.txt.enc
python xor.py crack test.txt.enc
```

## How it works

Encrypts files by XORing every byte with a single character key.

2 crackers included, A brute forcer that just displays all possible combinations and one that shows all possible combinations but displays reulsts with the highest likely hood by using a frequency analysis
## Disclaimer

For educational purposes only. Do not use on files or systems you do not own.
