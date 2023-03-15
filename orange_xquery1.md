# Remington Orange - XQuery Exercise 1
## Shakespeare Data

*Most of these will be following "collection('/db/apps/shakespeare/data/')"*

1.) Find all of the main titles of each of the 42 Shakespeare plays in the collection, by stepping down the descendant axis from the collection.

- `//titleStmt/title`

2.) Modify your XPath above to return just the text of the titles, without the tags.

- `//titleStmt/title/text()`

3.) Write an XPath expression that isolates the root element TEI of each play

- N/A (confused)

4.) Write an expression using a predicate ___ on the TEI element to help you locate four plays that hold a speaker named Falstaff. Which plays are they? Record your XPath expression.

- `//TEI[.//sp[speaker="Falstaff"]]` 
- The First Part of King Henry the Fourth
- The WordHoard Shakespeare
- The Globe Shakespeare
- Cambridge Shakespeare
- Internet Shakespeare
- (I got 5 so I'm not sure if I captured the correct portion)

5.) Modify your expression to return only the main titles of those four plays, and record your expression

-  `//TEI[.//sp[speaker="Falstaff"]]//title`

6.) Describe what changes in your results if you add text() or string() to your previous statement.

- `//TEI[.//sp[speaker="Falstaff"]]//text()`    =   3 results in the 5,7, and 10 box
- `//TEI[.//sp[speaker="Falstaff"]]//string()` = 4 results but they seem to be written out parts of the plays

7.) Falstaff is one of the characters who turns up in multiple Shakespeare plays. So how often does Falstaff speak in this whole Shakespeare collection? Write a new XPath expression to return all of the speeches spoken by Falstaff. Then modify your expression to use the count() function and return only the numerical count.

- `count(collection('/db/apps/shakespeare/data/')//sp[speaker="Falstaff"])`; *473*

8.) XQuery FLWOR Statement or XPath expression?: Did you write your XQuery for finding all of Falstaff's speeches with a long XPath expression (from left to right, starting from the collection())? Or did you write it up as a FLWOR statement in multiple lines, storing information in variables and referring to them? 

- I used XPath, or the sytem that we used in class. 
