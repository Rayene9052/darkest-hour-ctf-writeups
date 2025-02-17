# Cookie




## Description

This is a cryptography task I swear ...

[Challenge Link](http://cookie.dh.securinets.tn/register)

**Author:** Nedim

So we're just given a register and a login page , after making an account and trying to login to it we have a look at the cookie there 
![Access Denied](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/f2eb0f11601b7020b20fd99b0ce2c9d9fa6510d6/assets/access_denied.PNG)

Let's try to decode it with cyberchef 

![CyberChef](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/85a46dda1a84350f59b4d8014549512e3478425c/assets/cookie1.PNG)

Well there is nothing to see here , but the thing is  we must notice that the cookie changes everytime when you change the username . It's like  the cookie  depends  somehow on  the username . After some thinking i noticed that the operation occuring is a XOR operation between the username and the cookie . 
## Time to get the key ! 
![CyberChef2](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/5af6dd064b9ed26347d057877af1dd39b915f42c/assets/cookie2.PNG)
The XOR operation is occuring in the middle of the cookie , so the key here is EAXYXOR ! We're almost there , now let's decode the cookie with that key .