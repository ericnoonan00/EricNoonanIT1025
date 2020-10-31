# Executive Summary
In lab 5 we will cover the cloud chart making software LucidChart, introduce networking, and take a short dive into cybersecurity and encryption, which go hand-in-hand. I look forward to leraning about encryption as it used to be a small hobby of my friends and I.
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
1. Confidentiality would be important, as the customer would not want their messages leaked or stolen. Integrity is important because you, as a customer, would want only true information. Availability around the clock is important as not everybody can adjust their schedules to match the available hours of your firm.
2. Three daily tasks that require authentication are: Entering a passcode to unlock your phone, entering your email address and password to sign into your email (which is done mostly automatically now), completing a ReCaptcha.
3. ACL (Access Control List) and RBAC (Role Based Access Control) are two forms of Access Control, which basically sorts out who can access what. For example, a janitor won't have access to a company's network of clients. ACL takes everybody in the firm and one-by-one assigns them certain access privilages. RBAC assigns the privilages to certain roles, but then assigns those roles to certain people - a two step process.
4. A ciphertext is encrypted using a public key, and decrypted using two private keys.
5. Ciphers encrypted with public key encryption can take 1,000's of years to solve if they public key is very large and the method of encryption is modular mathematics.

### Cryptography
1. <a href="https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/caesar-cipher">The Caesar Cypher</a> was an encryption method that took each letter written and moved it back a certain number of places (e.g. if the numer was 3, N would become L). This was a rudementary but effective way of encryption.
2. However, hundreds of years after its creation, someone cracked it using a letter frequency analysis. They observed how many times a letter was likely to apppear on average (which varies depending on the language) and created a chart (called the language's Fingerprint). They can then overlay that chart on top of a chart which shows the frequency of letter in the encrypted text, and figure out the shift used to encrypt.
3. <a href="https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/polyalphabetic-cipher">Polyalphabetic Cypher</a> - instead of using a single shift number, polyalphabetic encryption uses a shift **word** to encrypt. The letter position of each letter in the key is laid over each of the letters in the plaintext. Then, whatever letter is laid over the plaintext is the shift. This method varies the shift letter to letter. The longer the key, the stronger the encryption.
4. With a word like SNAKE, one would move each letter 19, 14, 1, 11, and 5 times. <a href="http://www.satya-weblog.com/tools/find-alphabets.php">Here</a> is a reference to what the position of each letter is in the alphabet. Here is an example using SNAKE as the key:

Plaintext: the caesar cypher is over two thousand years old

Cyphertext: mvf nfxgbc hrdipw bg pgjk hxz yacvdfgr zpfkg pwi

### Brute-Force
Kerckhoffs' Principle states that the security of an encryption should lie solely in the choice of the **key**. Brute-force hacking is a form of codebreaking that tries every possible combination of letters, numbers, and symbols against an encryption in an attempt to find the key, until eventually it decrypts the message. These two principles are related to eachother as an incredibly long acnd complex key would take very very long to break using brute-force.
___
# Summary
In lab 5, we covered and experimented with LucidChart by making multiple types of charts: one for a short program and one for a network topology. In the next module, we covered the basics of networking. I enjoyed learning about network hardware and network topologies the most because now I have a deeper understanding of how a home network would work, allowing me to better troubleshoot and identify problems. In the third module, we covered encryption, a couple different cyphers, and a way to crack them using computers and python code. I would like to learn more about brute-force decryption and how to use it, so I will dedicate some time into learning some python and come back to this. The encryption module was my favorite module. 


