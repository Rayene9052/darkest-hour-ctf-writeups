# Love Portal
## Description
Be creative
[Challenge Link](http://love_portal.dh.securinets.tn/)
## Author : Enigma
### This challenge was quite fun ! Let's see how it's done

![LovePotal1](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/95f013fd44dbb1af13db313e8e76185748c0d795/assets/love_portal1.PNG)

### Let's see the source code 

![LovePortal2](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/95f013fd44dbb1af13db313e8e76185748c0d795/assets/love_portal2.PNG)

### Now we're gonna try some LFI exploitation! I tried on every page and then decoded from base64 but only got something interessting from the messages page !

![LovePortal3](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/95f013fd44dbb1af13db313e8e76185748c0d795/assets/love_portal3.PNG)

### Here's some explanation of the used command :

![LovePortal4](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/95f013fd44dbb1af13db313e8e76185748c0d795/assets/love_portal4.PNG)

### And that's what we get from decoding what we got from the messages page exploitation ! 

![LovePortal45](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/95f013fd44dbb1af13db313e8e76185748c0d795/assets/love_portal4%2C5.PNG)

### Let's do what we did earlier but with the navbar bcz we see its name in the decoded script

![LovePortal475](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/95f013fd44dbb1af13db313e8e76185748c0d795/assets/love%20portal4.75.PNG)

### And when we decode from base64 again we see a hidden directory !

![LovePortal5](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/95f013fd44dbb1af13db313e8e76185748c0d795/assets/love_portal5.PNG)

### Now we access to /log_546545/index.php 

![LovePortal6](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/95f013fd44dbb1af13db313e8e76185748c0d795/assets/love_portal6..PNG)

### Let's go back to burpsuite and manipulate the User-Agent field ! 

![LovePortal7](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/95f013fd44dbb1af13db313e8e76185748c0d795/assets/love_portal7.PNG)

### We clearly see the result of 'ls' command

![LovePortal8](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/95f013fd44dbb1af13db313e8e76185748c0d795/assets/love_portal8.PNG)

### Now we go back to burpsuite and do cat our flag

![LovePortal9](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/95f013fd44dbb1af13db313e8e76185748c0d795/assets/love_portal9.PNG)

## And here's our flag !

![LovePortal10](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/95f013fd44dbb1af13db313e8e76185748c0d795/assets/love_portal_flag.PNG)
