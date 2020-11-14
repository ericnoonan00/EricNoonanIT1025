# Executive Summary

&Tab;In lab 6, we will explore some more of what makes the internet what it is, such as: internet architecture, internet programming, and URLs. By the end of the lab I should know how websites are structured, some resources and basics of HTML5 and CSS, and how a URL works. I am most familiar with the second module as I already know some intermidiate HTML/CSS, so I look forward to that. Also, I am interested in how URLs are organized and how they work.
___

# 1. Internet Architecture
### Internet Protocol
- An IP address is how another device identifies your network in order to send data packets. It is pretty much the same thing as an actual address. There are two types of IP addresses, IPv4 and IPv6. The difference is that IPv4 is written in decimal (base 10) IPv6 is written in hexadecimal (base 16). The IPv6 protocol allows for so many more unique IP addresses.

- ICANN - ICANN is an organization that helps to unify the internet by organizing and coordinating each IP address. Each IP address needs to be unique. In order for there to be more than one of the same IP address, there would need to be two internets, or else the sender wouldn't know what IP to send the packet to.

### TCP/IP
- The responsibility of TCP/IP is to identify devices from one another.

- TCP/IP applies to the client server model such that the client fetches packets from the server's IP address. The server then delivers said packets to the clients IP address.

- Having layers in tech is important for changing technology because you can change one layer of the technology without the other layers being affected. A real life example of this is a parcel service between two post offices:
  - At the sending end:
    - Take the package, Wrap it and address it
    - Send it to the destination
  - At the receiving end: 
    - Receive the package
    - Deliver the package to it's recipient
  - The mail man at the first office:
    - Collects the parcels from the senders and takes them to the dispath room
    - The parcels are then placed in a van and driven to the second office
  - At the second office:
    - The parcels are received by the dispatcher and placed into trays for their mail man
    - The mail man collects the parcels and drives them to their recipients
###### Any of these layers can be changed without the other ones being affected. For example, the mail can be delivered by train between the offices instead of van. The mail men wouldn't have to even care about this change.
<h6><a href="http://www.steves-internet-guide.com/internet-protocol-suite-explained/">Here</a> is a resource for this topic</h6>

- The types of applications that run on the "application" layer are network services. Network services are protocals that work with the users data - interactive. An example of this would be a webpage. 

### Internet Security
- HTTP (HyperText Transfer Protocol) applies to the client server model such that it offers the protocol that the client sends/receives data and the server sends/receives data. 

- HTTPS (Secure HyperText Transfer Protocol) does the same thing as HTTP but with addition of encrypting the data being received by HTTP. This is necessary to keep the client's data secure as it travels across the public internet to get to the server.

### Securing Your Web Browser
- You should secure your web browser because nowadays browsers aren't installed with defaultly secure settings. It is important to configure them to be secure due to the many risks found on the internet such as hackers, spyware, etc.

- Plug-ins are one example of where a browser can become vulnerable. They often are riddled with software issues such as <a href="https://www.google.com/search?q=buffer+overflow&rlz=1C1CHBF_enUS864US864&oq=buffer+overflow&aqs=chrome..69i57.3894j0j7&sourceid=chrome&ie=UTF-8">buffer overflows</a> or other design flaws.
___

# 2. Internet Programming

### World Wide Web Consortium
- Tim Berners-Lee was the inventor of the World Wide Web along with the W3C (World Wide Web Consortium). He created the W3C in order to develope high quality standards for the internet in order for it to be used to its full potential. 

- One example of the things they hold to high standards is the Web Architecture. It is important to have extremely high standards when it comes to web architecture because it deals with the transfer of data from one device to another, and some of that data can be sensitive.

### HTML5 and CSS
- I approached the design of my webpage with a barebones mindset that I only needed to write the text with minimal formating. I used an internal stylesheet, which is when the CSS is programmed in the head portion of the page. I also used an un ordered list to explain each example. I used the &amp;lt; and &amp;gt; symbols instead of < and > because HTML won't let you type < or > because it thinks you are going to write another tag. 

### XML and HTML
XML (eXtensible Markup Language) is designed to store and transport information. It is also incredibly self descriptive (I have never seen a programming language be so self descriptive before lol). However, XML and HTML differ in purpose. HTML focuses on how data *looks* while XML focuses on what data *is* and how to carry the data. Also, XML has no predefined tags, the author just invents the tags and defines them later(?). HTML, on the other hand, uses a set of predefined tags like &lt;a&gt; or &lt;p&gt;. XML simplifies pretty much everything and has become a W3C recommendation since 1998.
___

# 3. URL and File Paths

### Components of a URL 
- scheme: http or https - tells the browser what protocol to use so it can display the page correctly.
- domain: www.amazon.com - the main part of the URL. The full name of the website, basically.
- top level domain: .edu, .org, .gov - identifies what type of website you would be accessing. E.g. .gov is a government run website in the USA
- default page: no file path provided
- parameters: result of search
- anchor: specific location on the webpage.
___
# Summary
&Tab;In lab 6, we looked at some of the other things that make the internet go. Namely: internet architecture, internet programming, and URLs. We were given an in depth look at TSL/IP which is an internet protocol and a fantastic example of layered architecture. Also, we took a look at the W3C, which holds high standards for websites/web design. One thing I found particularly interesting about this module was the section about XML. Up until now, I hadn't even heard of XML. The differences between it and HTML were astonishing. XML seems so straight forward, and I will be looking more into XML on my own. Lastly, we looked at how URLs were structured.

