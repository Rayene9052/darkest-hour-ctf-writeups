# Guesser


## Description
You got 7 tries to make it work .
 nc 3.250.32.255 2031

## Author : Nedim
And we're giving a python file

The remote service updates a cumulative score after each guess. This score is updated by multiplying by a product based on differences between the secret letters (converted into m
## **Overview**

This challenge involves a remote server running a word-guessing game on `3.250.32.255:2031`. The objective is to deduce a secret six-letter word using a mathematical scoring system based on modular arithmetic (mod 29). The score after each guess provides indirect information about the word, which we can extract using a carefully crafted approach.

Instead of brute-forcing all possible words, we use mathematical techniques like modular inversion, polynomial interpolation, and elementary symmetric sums to reconstruct the secret word efficiently.

---

## **Understanding the Score Mechanism**

Each guessed word is a 6-letter string. The server evaluates the first five letters and computes a **score** based on the following function:

$$
S(t) = \prod_{i=0}^{4} (w_i - t) \mod 29
$$

where:
- $$ \( s_0, s_1, s_2, s_3, s_4 \) $$ == are the modular values of the first five letters of the secret word.
- $$ \( t \) $$ is a chosen integer (determined by the guess).
- The score \( S(t) \) is the product of the differences between the secret letters and \( t \), modulo 29.

The challenge is to determine the original values $$ \( s_0, s_1, s_2, s_3, s_4 \) $$ given different values of $$ \( S(t) \) $$.

---

## **Step-by-Step Approach**

### **1. Establishing the Score Pattern**
We start by sending six specific guesses where only one letter is different in each, allowing us to compute different \( S(t) \) values.

```python
guesses = ['aaaaaa', 'baaaaa', 'abaaaa', 'aabaaa', 'aaabaa', 'aaaaba']
```

Each of these words ensures that one specific character's modular value is shifted. By observing the score, we gather equations for different values of \( t \).

### **2. Extracting Modular Values of the Secret Word**
For each score $$ \( S(t) \) $$ , we compute a related ratio $$ \( R_i \) $$ :

$$
R_i = \frac{S(i+1)}{S(0)} \mod 29
$$

Using this ratio, we solve for each letter's modular representation:
$$
w_i = \frac{R_i \cdot 97 - 98}{R_i - 1} \mod 29
$$
Here:
- $$ \( 97 \) $$ corresponds to `'a'` in ASCII.
- $$ \( w_i \) $$ gives us the modular representation of the letter.

Finally, we map these values back to ASCII letters.

### **3. Computing the Last Letter**
The sixth letter doesn't directly affect the score. However, the symmetric sum property tells us:
$$

S(0) = \prod_{i=0}^{4} (w_i - 97) \mod 29

$$
Rearranging:
$$

w_5 = 97 + \left(\frac{S(0)}{\prod_{i=0}^{4} (w_i - 97)} \right) \mod 29

$$
This ensures we correctly reconstruct the full six-letter word.



## ** Solver **
```
import socket

def mod29_to_ascii(r):
    return 97 + (r - 10) % 29

HOST = '3.250.32.255'
PORT = 2031

def read_until(sock, prompt):
    data = b''
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        data += chunk
        if prompt in data:
            break
    return data.decode()

def get_score(data):
    lines = data.split('\n')
    for line in reversed(lines):
        if line.startswith('> Score is '):
            return int(line.split()[-1])
    raise ValueError("Score not found")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Read initial prompt
read_until(s, b'What\'s your guess? ')

# Send initial guesses and collect scores
guesses = ['aaaaaa', 'baaaaa', 'abaaaa', 'aabaaa', 'aaabaa', 'aaaaba']
scores = []

for guess in guesses:
    s.sendall(guess.encode() + b'\n')
    data = read_until(s, b'What\'s your guess? ')
    score = get_score(data)
    scores.append(score)

s0, s1, s2, s3, s4, s5 = scores

w = [0] * 6

# Compute w0-w4
for i in range(5):
    s_i_plus_1 = scores[i+1]
    R_i = (s_i_plus_1 * pow(s0, 27, 29)) % 29
    numerator = (R_i * 97 - 98) % 29
    denominator = (R_i - 1) % 29
    inv_denominator = pow(denominator, 27, 29)
    w_i_mod29 = (numerator * inv_denominator) % 29
    w[i] = mod29_to_ascii(w_i_mod29)

# Compute w5
product = 1
for i in range(5):
    term = (w[i] - 97) % 29
    product = (product * term) % 29

if product == 0:
    # This case shouldn't happen if S0 is non-zero
    w[5] = 97  # Fallback, but likely incorrect
else:
    inv_product = pow(product, 27, 29)
    w5_minus_97 = (s0 * inv_product) % 29
    w5_mod29 = (10 + w5_minus_97) % 29  # Because w5 mod29 = 97 + (w5-97) mod29
    w[5] = mod29_to_ascii(w5_mod29)

# Construct the correct word
correct_word = ''.join([chr(c) for c in w])

# Send the correct word
s.sendall(correct_word.encode() + b'\n')

# Read the response
data = read_until(s, b'What\'s your guess? ')
print(data)

s.close()


```
## Flag
![FlagGuesser](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/dada45b421e75021ae7e0115d782aa61b56231c9/assets/guess%20solver%20output.PNG)
```
Securinets{N1ce_Gu3ss1nG_K33p_G01nG}
``` 