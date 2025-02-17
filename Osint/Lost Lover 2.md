## Lost Lover 2
## Description

A social media account led you to an old post. A post stands out—a sentimental message about a place where they always met. It seems like someone tried to cover their tracks. However, you know that the internet never forgets.Uncover the name of the street where they used to meet.

Flag format: Securinets{Street_Name}

## Author : AKKINATOR

The first step in this challenge is to find the social media account in question. To do that we'll use  www.idcrawl.com.
You type the name we found on the previous challenge and you will see that there is Twitter account with that username.

![Twitter](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/3fe50ab217fe3a9e15e33ca4b25a640133046dcb/assets/twitter.png)

in this account you will see a post that has an image of some location. In order to find the place we first need to download the image and then perform reverse image search.

![image](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/3fe50ab217fe3a9e15e33ca4b25a640133046dcb/assets/image.jpg)

 Now all you have to due is try to find more info about that place.
 I found this website which has almost the same exact image 
 https://www.desmoulin-architectures.com/diapo?page=realisations&groupe=nouveau-morax
 from there we can see that the building name is "HOPITAL LARIBOISIERE" and that's our final clue.
 The final step is to look for the location on Google Maps and copy paste the street name.

 ![image](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/3fe50ab217fe3a9e15e33ca4b25a640133046dcb/assets/maps.png)

## FLAG
```
Securinets{Rue_Ambroise_Pare}

```
