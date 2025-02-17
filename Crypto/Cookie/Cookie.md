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
![CyberChef3](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/9dd1d2eaaed74c2a8378883344893292f4f5eea8/assets/cookie3.PNG)
We got something really interesting !! a boolean logic variable named isadmin set to 0 and the username ! So let's try changing isadmin to 1 and the username name to admin , XOR it again with the same key , and put it back in the website !
[!CyberChef4](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/83cd8e0a73fdc11f3ee79c9cdc49936239917416/assets/cookie4.PNG)

AND HERE IS OUR FLAG !! This challenge got few solves ( 2 or 3 ) meanwhile it wasn't that hard as an idea 

[!FLAG]