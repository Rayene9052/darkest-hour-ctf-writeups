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

