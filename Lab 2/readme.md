# 1. Hardware
#### Hardware drives and memory
___
## Hard Drives - Difference Between Latency and Transfer Rate
* Latency is measured in milliseconds and Transfer Rates are measured in MBps (Megabytes per second)
* Latency is the time the disk takes to rotate 180 degrees, while Transfer Rate is the time it takes for data to move to and from the disk
___
## Solid State Drives
Solid State Drives are different from Hard Disk Drives in that there are no moving parts to an SSD. There are no magnets, and dust can't collect on the unpresent disk of an SSD; both of these things make the HDD a fallible piece of hardware. The SSD is also much faster, as an HDD has to get its disk spinning to a certain speed and find the correct place on the disk where the data is stored. SSD's also are a more stable piece of hardware; because there are no moving parts, there is less that can go wrong. The one thing that HDD beats SSD in is price.
___
## RAM
* A computer with a high amount of RAM wont have the need for the RAM to keep going back to the HDD to load data into th CPU. It will just take it from the HDD and load it onto the CPU in one trip.
* A 32 bit system can only access 2^32 bits of RAM while a 64 bit system can access 2^64. 2^32 bits is about 4gb.
___
# 2. 
### Control Unit and ALU
* First, the Control Unit gets an intruction from RAM then uses that to tell the ALU the type of operation to preform.
* Second, the ALU preforms the operation and outputs the answer.
* Sometimes the ALU will create flags, like in the case of a COMPARE command, in which case it will not need to output anything. It would simply give the Control Unit the flag which lets the Control Unit know what to do with the next command
* However, if the ALU does output something, the output goes to the Register. The Register acts almost like RAM, storing a number, except they are inside the CPU, which makes them faster for storing a number temporarily.
* The register isn't acctually turned on until the Control Unit activates it via the Set Wire. When the set wire is turned on, the Register saves whatever number is on its input wires. 
* When we are ready to use the output that is saved in the Register, the Control Unit turns on the Enable Wire. As soon as the Enable Wire is turned on, the Register will output whatever number is saved inside.
* The output then goes a series of wires that connect different parts of the CPU called a Bus. On this Bus are some other registers with their own Set/Enable wires which may have different numbers from previous instuctions.
* Finally the Control Unit will turn off the Enable Wire which will clear the Bus.




# 3. Data Representation
Decimal, Hexidecimal, and Binary are number systems in different bases.
* *Decimal* is base 10
* *Hexidecimal* is base 6
* *Binary* is base 2
For example:
* 189 in Decimal would be 10111101 in binary
* 







