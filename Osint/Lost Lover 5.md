## Lost Lover 5
## Description

The same person decided to leak some crucial data where
he uncovered the role of evelyn in the case, how, Why she
disappeared and where did she hide the ruby neckless.
Your mission is to find the new name she goes by and her
role in our case.
flag format: Securinets{Her_New_Name_Role_In_Case}

## Author : AKKINATOR

in this task you have to find the person's account (SilentEcho23) that leaked the data.
When searching i came across an instagram account with the same username which has a link in his bio and that is the link that has the data we're looking for.

![image](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/beb2e7556d118a92cf409930257efe35d40c79aa/assets/account.png)

the link gives us 2 files which we have to download

![image](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/beb2e7556d118a92cf409930257efe35d40c79aa/assets/leak.png)

the first file 'Legal Documents.rar' is a zipped file when trying to extarct it it will ask you for a password.
the second file is a hint to the password which is in one of the poems of the user's twitter account.

So we go back the twitter account and we find the following poem

![image](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/beb2e7556d118a92cf409930257efe35d40c79aa/assets/poem.png)

Now by copy pasting the poem in (https://codewithrockstar.com/online.html) you'll get the hidden password which is 'mysterious'
Once you unzip the file you'll have 3 .txt files. The only one you'll need is "Legal Documents.txt"

![image](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/beb2e7556d118a92cf409930257efe35d40c79aa/assets/legal.png)

By reading this file you'll find all the details you need for the flag

## FLAG
```
Securinets{Evelyn_Carter_Witness}

```
