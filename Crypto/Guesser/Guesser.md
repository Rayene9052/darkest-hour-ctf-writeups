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

\[
S(t) = \prod_{i=0}^{4} (s_i - t) \mod 29
\]

where:
- \( s_0, s_1, s_2, s_3, s_4 \) are the modular values of the first five letters of the secret word.
- \( t \) is a chosen integer (determined by the guess).
- The score \( S(t) \) is the product of the differences between the secret letters and \( t \), modulo 29.

The challenge is to determine the original values \( s_0, s_1, s_2, s_3, s_4 \) given different values of \( S(t) \).

---

## **Step-by-Step Approach**

### **1. Establishing the Score Pattern**
We start by sending six specific guesses where only one letter is different in each, allowing us to compute different \( S(t) \) values.

```python
guesses = ['aaaaaa', 'baaaaa', 'abaaaa', 'aabaaa', 'aaabaa', 'aaaaba']
```

Each of these words ensures that one specific character's modular value is shifted. By observing the score, we gather equations for different values of \( t \).

### **2. Extracting Modular Values of the Secret Word**
For each score \( S(t) \), we compute a related ratio \( R_i \):

\[
R_i = \frac{S(i+1)}{S(0)} \mod 29
\]

Using this ratio, we solve for each letter's modular representation:

\[
w_i = \frac{R_i \cdot 97 - 98}{R_i - 1} \mod 29
\]

Here:
- \( 97 \) corresponds to `'a'` in ASCII.
- \( w_i \) gives us the modular representation of the letter.

Finally, we map these values back to ASCII letters.

### **3. Computing the Last Letter**
The sixth letter doesn't directly affect the score. However, the symmetric sum property tells us:

\[
S(0) = \prod_{i=0}^{4} (w_i - 97) \mod 29
\]

Rearranging:

\[
w_5 = 97 + \left(\frac{S(0)}{\prod_{i=0}^{4} (w_i - 97)} \right) \mod 29
\]

This ensures we correctly reconstruct the full six-letter word.

---

## **Final Execution**
1. **Connect to the server**
2. **Send six strategically crafted guesses**
3. **Extract modular letter values using division and modular inversion**
4. **Convert modular values back to ASCII letters**
5. **Send the final word as our last guess**
6. **Retrieve the flag**

```python
s.sendall(correct_word.encode() + b'\n')
data = read_until(s, b'What\'s your guess? ')
print(data)
```

---

## **Conclusion**
This approach allows us to efficiently determine the secret word using mathematical techniques instead of brute force. The key ideas include:
- Using modular arithmetic properties.
- Leveraging polynomial relationships to recover letter values.
- Applying elementary symmetric sums to reconstruct missing values.

By following these steps, we successfully cracked the challenge and obtained the flag.