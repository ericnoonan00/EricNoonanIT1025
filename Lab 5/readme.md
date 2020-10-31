# Executive Summary

___

# 1. LucidChart
LucidChart is a cloud-based software that allows the user to create flowcharts for programming, business operations, etc. Today I used LucidChart to create a flowchart for a simple program that tells the user if their input was greater than or less than 15 by saying "Big" or "Small," respectively. LucidChart is incredibly user friendly without sacrificing ability. I never felt lost while using the software and I plane to use it again in the future.
___

# 2. Introduction to Networking
### Data Transmission
* Packet - Unit of Data
* Packet Switching - Technology that allows packets of data to be routed based on destination address
* IP Address - Unique identifying number
* DNS - Directory of IP address common names
* Protocal - Set of rules that allow devices to communicate

### Network Hardware
* A switch has the advantage of being able to send a packet to a specific device that is connected to the switch. This is impossible while using a hub because a hub broadcasts the packet to every device connected to it. This is beneficial because it doesn't waste bandwith and is much more secure.
* Hubs and switches can only communicate within a local area network (LAN), which means they cannot communicate with other **IP** addresses via the internet. This is the advantage that routers have over hubs and switches.

### Network Topologies
* Single Point failure - when the central hub/switch fails or a device fails. Wired topologies experience this such as: Star, Ring, or Bus.
* I like the wireless mesh architecture better as it seems much easier to set up.

### Network Design
I made an infrastructure topology. Data is received through the modem and brought to a switch which sends the packets to the appropriate devices. The switch also sends data to a router which acts as a wireless access point for the cell phone and printer. The arrows that connect the PC's and switch point both ways. I included this because the PC's are able to send data to the other places on the network. I also included the double arrow that connects the switch to the router because the data from the wireless devices travel through the router to access the other devices on the network. Finally, the dotted lines that connect the router to the wireless devices are dotted because it represents the lack of a real wire.

### NSA/CSS
* The NSA/CSS is a government agency that detects, prevents, and stops cyber attacks. In this day and age, cyber attacks are a real threat to our nation and without an incredibly fine tuned and dependable organization to stop them, the whole country's information would be at risk, making us vulnerable to physical attack and economic crisis.

___

# 3. Cybersecurity and Encryption

### Information Systems Security
1. 
2. Three daily tasks that require authentication are: Entering a passcode to unlock your phone, entering your email address and password to sign into your email (which is done mostly automatically now), completing a ReCaptcha.
3. ACL (Access Control List) and RBAC (Role Based Access Control) are two forms of Access Control, which basically sorts out who can access what. For example, a janitor won't have access to a company's network of clients. ACL takes everybody in the firm and one-by-one assigns them certain access privilages. RBAC assigns the privilages to certain roles, but then assigns those roles to certain people - a two step process.
4. A ciphertext is encrypted using a public key, and decrypted using two private keys.
5. Ciphers encrypted with public key encryption can take 1,000's of years to solve if they public key is very large and the method of encryption is modular mathematics.

### Cryptography
1. <a href="https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/caesar-cipher" style="color: black;">The Caesar Cypher</a> was an encryption method that took each letter written and moved it back three places (e.g. N would become L). This was a rudementary but effective way of encryption. However, hundreds of years after its creation, someone cracked it using a letter frequency analysis. They observed how many times a letter was likely to apppear on average (which varies depending on the language) and created a chart. They can then overlay that chart on top of a chart which shows the frequency of letter in the encrypted text, and figure out the shift used to encrypt. <a href="https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/caesar-cipher" style="color: black;">
___
# Summary



