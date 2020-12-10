# Executive Summary
In Lab 8, we will talk about various database models, practice querying a database with SQL (structured query language), and go over ethical and legal implications of IT. To say databases are an important part of our everyday life would be an understatement. Also, to know the ethical standards expected to be followed would be vastly important in obtaining and maintaining an IT career that makes you proud of yourself.   
___
# Database
&tab;The diference between *data*,*information*, and *knowledge* can be looked at in tiers. Teir 1, *data* is pure quantitative and qualitative, devoid of context or intent. Tier 2, *information* is contextualized data. For example, monthly sales, calculated from daily sales, used to calculate yearly sales, are information. Tier 3 would be *knowledge*, which is human beliefs or perceptions about concepts local to the area of said human. There are two types of knowledge: *explicit* and *tacit* knowledge. *Explicit* knowledge refers to qualitative and quantitative knowledge - it can be expressed with words and numbers. *Tacit* knowledge refers to insights and institutions which are difficult to transfer into words.

**Making tables** - example: Small Company
- the Customer table and the Order table would have the primary key of *CustomerID* and *Order Number* respectively.
- The two tables are related by their primary keys. I made it this way because there would be no other unique way to keep track of the customers.
- CustomerID would be the foreign key to the Order table.

### Big Data
**The Four V's of Big Data**$NewLine;
- Volume: the amount of data that makes data *big*. It describes the entriety of the data that organizations have been trying to harness to improve decision making across the enterprise.
- Velocity: This represents the movement of data. Data movement is now almost real time and the update window has reduced to the fraction of a second. Because of this real-time nature of data creation, enterprises could incorporate streaming data into decision making.
- Variety: It defines different types of *data* and *resources*. New categories have been added to the list of data types.
- Veracity: The trustworthiness of the data and certain types of data.

**What types of technology have driven the increased need for big data?**
___
# Structured Query Language(SQL)
- RDBMS stands for Relational Database Management System. If SQL is how you access, organize and update the database, RDBMS is how you make the database
- The two tables I picked were the product table and cataegory table. Their primary keys are ProductID and CategoryID. CategoryID is the foreign key to the product table. The category table is what holds a description of what type of product it is.

### SQL Injections 
SQL Injections are a common and serious database security threat. They are done by web input when there is nothing stopping the user from entering incorrect information. This can be prevented by adding *parameters* to your SQL file.
___
# Ethical and Legal Implications of Information Systems
A *code of ethics* is a document that outlines a set of acceptable behaviors for a professional and it is generally, agreed to by all members of the group. The code of ethics that IT professionals follow is the Association for Computing Machinery (ACM). They created this as a standarized code of ethics for IT professionals.

- An Acceptable Use Policy (AUP)(commonly: Terms of Use) is different from a code of ethics in that it outlines the rules for someone using an enterprise's software, while a code of ethics outlines the company's acceptable behaviors.
- For example I'll look at Netflix's AUP/Terms of Use (https://help.netflix.com/legal/termsofuse). They outline 9 Sections: Membership, Free Trials, Billing and Cancellation, Netflix Service, Passwords and Account Access, Disclaimers of Warranties and Limitations on Liability, Arbitration Agreement, DVD Plans, and Miscellaneous. The rules I find are quite predictable and can be summed up by saying, "if you are doing anything blatantly sketchy using Netflix, you are breaking the AUP"

### Intellectual Property
**WIPO** - the global forum for intellectual property (IP) services. They basically make sure that if you created it you get the credit for it. 

- It would be mean a great deal of importance to obtain a copyright on something you create because:
  - it will protect you from people stealing your ideas
  - if someone steals your idea, they can copyright it before you and take legal action against you
- In the case of the SVG image I created earlier in the course, it would be important to copyright it because it is the logo for my company and it holds the idea of the whole company within it. If someone stole that, they could profit off of my intellect and leave me with nothing.
- A Trademark would be expecially useful in the case of the SVG logo I created because it protects the actual image itself, whereas the copyright protects the intellectual property. 

### Information Collection
- COPPA - gives parents control over what information websites can collect from their kids
- FERPA - protects the privacy of student education databases
- HIPPA - publicizes standards for the electronic exchange, privacy and security of health information
___
# Conclusion
In lab 8 we discussed some basic database concepts and basic SQL (as an aspiring programmer I will be diving headfirst into SQL during winter break). The SQL module was interesting to me as it showed me how databases were programmed - something I always wondered about. Also we looked at the ethical standards that are expected out of each and every IT professional. It was interesting to see that they were pretty predictable. I found myself saying, "yeah, that makes sense" a lot during this module.
