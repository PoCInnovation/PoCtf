# PoCTF

## Introduction

POCTF is a CTF made by PoC Innovation. The goal of this project is to make a CTF with few challenges (~12) but to work all challenges with a very specific attention to detail. All challenges are made to be innovative.

## Platform

To focus only on the process of making challenges, we used [CTFd](https://github.com/CTFd/CTFd) in order to help us building the platform. With the base of CTFd, we made a custom theme in order to make our platform and not just a generic CTFd site. This is what the platform looks like:
![Platform](https://i.ibb.co/2h93TPd/image-2021-01-29-083825.png)

You can access the platform  and the challenges with this URL: [https://poctf-beta.poc-innovation.com](https://poctf-beta.poc-innovation.com)
## Challenges
### Introduction

We made 2 introduction challenges: 
 - **BIP**: An audio file that you have to analyse in order to get the flag from it.
 - **Find me if you can**: This challenge is a GEOINT challenge. You give you an image, and you have to find in which city the photo was taken.

### ROP
**R**eturn-**o**riented **p**rogramming (**ROP**) is a computer security exploit technique that allows an attacker to execute code in the presence of security defenses such as executable space protection and code signing.

We made 3 ROP challenges: 
 - **Please be nice**: An introduction challenge in order to give you the base of ROP.
 - **Abuse me**: An intermediate challenge which need you to use harder breach in the binary in order to get the data that you need in order to flag the challenge.
 - **Inspector Gadget**: A very hard challenge, here to make you a master in ROP if you can access the flag that we hide in it.

### Cryptography
Cryptography is a method of protecting information and communications through the use of codes, so that only those for whom the information is intended can read and process it. The prefix "crypt-" means "hidden" or "vault" -- and the suffix "-graphy" stands for "writing."

We made 3 Cryptography challenges: 

 - **RSA Fault**: In this challenge you will need to use a breach in the implementation of the RSA encrypting process in order to hack the given key and access the flag.
 - **Remote classes**: A friend of you made you a little prank by encrypting your school pdf. You will need to find how to access the data in the file. Be careful, it's not because the filename ends with `.pdf` that it is a pdf. :)
 - **RSA Cracker**: In this challenge we want you to hack a 512 RSA public key in order to give us the flag in `flag.txt`.

###  Reverse Engineering
  
Reverse engineering, sometimes called back engineering, is a process in which software, architectural structures and other products are deconstructed to extract design information from them. Often, reverse engineering involves deconstructing individual components of larger products. The reverse engineering process enables you to determine how a part was designed so that you can recreate it.

We made 3 Reverse Engineering challenges: 

 - **Vault**: We made a polymorphic binary and now we want you to inspect it in order to find the data we hide in the ELF sections.
 -**Robbery**: This time we made a polymorphic AND metamorphic binary. We want you to find what is the real instruction at offset 401ad1. Our binary is tricky, it changes it's hash and instructions everytime you run it.
 - **Reverse PCAP**: We give you a binary that acts like a virus by sending files to someone. You don't need to run the virus but only to reverse it in order to understand how he is encrypting the files. Once you've done that, you will have to inspect the pcapng capture in order to find the malicious data packets in order to decrypt their data.

 ###  Steganography
 Steganography is the use of various methods to hide information from unwanted eyes. In ancient times, steganography was mostly done physically.

For our steganography challenges we used a method called polyglot files.
Polyglots, in a security context, are files that are a valid form of multiple different file types. For example, a  [GIFAR](https://en.wikipedia.org/wiki/Gifar)  is both a GIF and a RAR file. There are also files out there that can be both GIF and JS, both PPT and JS, etc.

Polyglot files are often used to bypass protection based on file types. Many applications that allow users to upload files only allow uploads of certain types, such as JPEG, GIF, DOC, so as to prevent users from uploading potentially dangerous files like JS files, PHP files or Phar files.

For this occasion we made Ditto. A file that can be interpreted as numerous format in order to introduce you to this practice.

Ditto has 3 main challenges in order to find three flags hidden in the file. The challenges are:

 - **Upsidedown Relic**
 - **Opened Relic**
 - **The Archives**

