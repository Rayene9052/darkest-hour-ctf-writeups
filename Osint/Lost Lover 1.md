## Lost Lover 1
## Description

The case begins with a single, seemingly unimportant clue—a handwritten letter, left behind at the scene of the heist. At first glance, it appears to be a personal note filled with regret and cryptic reflections. But something feels off. The words are emotional, but they don’t reveal much.

However, a true investigator knows that secrets often hide beneath the surface. Could the letter itself contain something more?

https://dh.securinets.tn/files/8f5bf3b58bb4bb775ed135ff0f124cda/Letter.jpg?token=eyJ1c2VyX2lkIjo1LCJ0ZWFtX2lkIjoyLCJmaWxlX2lkIjoyN30.Z7NY5Q.dtwvKiKQDgs2H0ksM6D0zKAG0e4

Flag format: Securinets{Sender}

## Author : AKKINATOR

This challenge comes with an image once you download the image the first thing you do is to check the metadata. 
If you are on Kali Linux, you can just run the following command:
exiftool Letter.jpg
if you don't have Kali you can just go to https://www.aperisolve.com then upload the image and scroll down to to the exiftool section.
Once you have the metadata all you have to do is try to find something  catchy.
By scrolling down you will see that the authour of the image is a strange name and that is the flag we're looking for.
![image](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/7b978f0f174719c34bde6bd64b1bb5d3a04d1c43/assets/Capture%20d'%C3%A9cran%202025-02-17%20164544.png)

## FLAG
```
Securinets{AphroWhisper}

```