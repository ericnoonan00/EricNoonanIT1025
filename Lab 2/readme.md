# 1. Hardware - Hardware drives and memory
### Hard Drives - Difference Between Latency and Transfer Rate
* Latency is measured in milliseconds and Transfer Rates are measured in MBps (Megabytes per second)
* Latency is the time the disk takes to rotate 180 degrees, while Transfer Rate is the time it takes for data to move to and from the disk
### Solid State Drives
Solid State Drives are different from Hard Disk Drives in that there are no moving parts to an SSD. There are no magnets, and dust can't collect on the unpresent disk of an SSD; both of these things make the HDD a fallible piece of hardware. The SSD is also much faster, as an HDD has to get its disk spinning to a certain speed and find the correct place on the disk where the data is stored. SSD's also are a more stable piece of hardware; because there are no moving parts, there is less that can go wrong. The one thing that HDD beats SSD in is price.
### RAM
* A computer with a high amount of RAM wont have the need for the RAM to keep going back to the HDD to load data into th CPU. It will just take it from the HDD and load it onto the CPU in one trip.
* A 32 bit system can only access 2^32 bits of RAM while a 64 bit system can access 2^64. 2^32 bits is about 4gb.
___
# 2. Hardware
### Control Unit and ALU
* First, the Control Unit gets an intruction from RAM then uses that to tell the ALU the type of operation to preform.
* Second, the ALU preforms the operation and outputs the answer.
* Sometimes the ALU will create flags, like in the case of a COMPARE command, in which case it will not need to output anything. It would simply give the Control Unit the flag which lets the Control Unit know what to do with the next command
* However, if the ALU does output something, the output goes to the Register. The Register acts almost like RAM, storing a number, except they are inside the CPU, which makes them faster for storing a number temporarily.
* The register isn't acctually turned on until the Control Unit activates it via the Set Wire. When the set wire is turned on, the Register saves whatever number is on its input wires. 
* When we are ready to use the output that is saved in the Register, the Control Unit turns on the Enable Wire. As soon as the Enable Wire is turned on, the Register will output whatever number is saved inside.
* The output then goes a series of wires that connect different parts of the CPU called a Bus. On this Bus are some other registers with their own Set/Enable wires which may have different numbers from previous instuctions.
* Finally the Control Unit will turn off the Enable Wire which will clear the Bus.
### Hardware - CPU, Input, and Output
An example of a CPU getting input and giving Output would be at the grocery store self checkout
* You, the user, input data into the self checkout kiosk by scanning your item
* The CPU of the kiosk, turns the data into binary code to store as memory
* Next, the kiosk displays the data stored as memory as output. This would be the price and name of the item, and even how much it weighs.
### Logic Gates and Circuits
A logic gate is an electric circuit with two inputs and an output that receives two incoming electric currents, compares them, and sends on a new, outgoing electric current depending on what it finds. The two inputs it can receive are a 1 or a 0. Think of a troll guarding a bridge and you have to pass a test to get through.
A Truth Table is a table that describes every output for every input a logic gate can receive (a screenshot of a few is in the folder). For example a NAND (an AND gate with the outputs reversed) gate would go as follows:
* 0 , 0  -  1
* 1 , 0  -  1
* 0 , 1  -  1
* 1 , 1  -  0
### IEEE - Ethically Aligned Design
The purpose of the IEEE (Institute of Electrical and Electronics Engineers) is to make sure that advancements in AI technology are human-centered and ethical. It is important to keep ethics in mind when working with AI, because AI is a tool to help the world community and if it isn't human-centric, there would be no point in doing it and it could potentially harm the community.
___

# 3. Data Representation
### Numeric Conversions
Decimal, Hexadecimal, and Binary are number systems in different bases.
* *Decimal* is base 10
* *Hexadecimal* is base 16 (0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f)  
* *Binary* is base 2
For example, 189 in Decimal would be 10111101 in binary (work shown using MS Paint)
### Hexadecimal Color Representation
Hexadecimal is used to represent a color on the color wheel when we program. For example, ab00ff is a magenta-like purple color.
While pleasant to the eye, this color may be problematic in constructing a webpage due to many normal colors not being contrasted enough against it. For example that color text would not be legible on a black or blue background. It would have to be a jarring, bright green in order to get enough contrast, however that would hurt the eyes.






