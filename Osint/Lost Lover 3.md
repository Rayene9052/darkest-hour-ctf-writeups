## Lost Lover 3
## Description

Your investigation is picking up momentum.The social media account shared once a blog about the incident that happened on 14 fev 2013 but it's no longer there. Your mission is to discover where the incident happened.

Flag format: Securinets{Location_Name}

## Author : AKKINATOR

The description mentions that there was a blog that was no longer there which could mean the blog was deleted. Therefore we get the idea to look for the archives or cached pages of the user's twitter account. A famous online tool would be Wayback Machine
'https://web.archive.org' however this website doesn't show any results. So we continue to look for other archiving tools.
The one i used in this challenge is www.archive.is by copyinng the user profile URL and pasting it in the website we get an archived page of the account containing a new post which is the blog we're looking for 
(https://medium.com/@SilentEcho23/mystery-at-the-train-station-a-lovers-disappearance-leaves-more-68de9418af0a)

![image](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/a4e1f6c32e58b5b4e87321d7cd488db1487fc50b/assets/blog.png)

The title of this blog was all we needed to get to our flag. the title mentioned a train station so we go back to Google Maps and search for a train station near the street we found in previous challenge and there is our flag

![image](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/a4e1f6c32e58b5b4e87321d7cd488db1487fc50b/assets/gare.png)

## FLAG
```
Securinets{Gare_du_Nord}

```