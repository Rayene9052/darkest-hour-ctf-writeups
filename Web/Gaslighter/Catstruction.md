## Catstruction
## Description
the flag is at /flag

## Author : Chuuya

[Link](http://catstruction.dh.securinets.tn/)

When we start the challenge we see this website

![Cats1](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/3ad235f65f6136c93d76c25671d2ab3bdf912455/assets/catrsut1.PNG)

The first idea is to check robots.txt , gobuster and other methods but all led to nothing , let's just focus on the source code 
![Cats2](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/3ad235f65f6136c93d76c25671d2ab3bdf912455/assets/catrsut2.PNG)

We see we don't have hints or smth here but we have the image we see in the initial website .Let's click on it.

![Cats3](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/3ad235f65f6136c93d76c25671d2ab3bdf912455/assets/catrsut3.PNG)

When we see the word file , a commun idea here is to check LFI(local file inclusion) vuln !

And after adding paths again and again i got  an  image 

![Cats4](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/3ad235f65f6136c93d76c25671d2ab3bdf912455/assets/catrsut4.PNG)

Editing it with NotePad gave us our flag !

![Cats5](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/3ad235f65f6136c93d76c25671d2ab3bdf912455/assets/catrsut5.PNG)

