# Pands Problem Sheet 2023


This repository is used for the problem sets given during the Programming and Scripting module on Higher Diploma in Data Analytics course from GMIT.\
Here I will explain how I came to the solution of given tasks, reference the sources I researched for solving the problems and list the technologies I used for creating and testing the code.\
I have no previous experience of coding.  In creating this README file I used the following resources as well as consulting with fellow students.

[MarkdownGuide](https://www.markdownguide.org/cheat-sheet/)\
[GistGithub](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)

## Table of contents
* [Weekly tasks](#weekly-tasks)
    * [Bank](#bank)
    * [Accounts](#accounts)
    * [Collatz](#collatz)
    * [Weekday](#weekday)
    * [Square root](#python-squareroot)
    * [Es](#es)
    * [Plotting](#plottask)
* [Technologies](#technologies)


Weekly tasks
======
### ***Bank***

    Write a program that prompts the user to read in two money amounts (in cent).  
    Both amounts are added together and the answer is printed out in a human readable 
    format with a euro sign and decimal point between the euro and cent amount.

This program is a basic calculation of based on the users input.

User inputs the two amounts in cent. The amounts are added together and converted to Euro and Cent by dividing the total by 100 and is returned as a floating point number rounded to two decimal places.

The [rounding](https://pythonguides.com/python-print-2-decimal-places/) of the result to 2 points was added for a nicer touch although not strictly necessary.


### ***Accounts***

    Write a program that that reads in a 10 character account number
    and outputs the account number with only the last 4 digits showing
    (and the first 6 digits replaced with Xs).

Although not specified I've added a validation rule that prompts the user to enter the account number again if it is less than ten digits.  This is done by using a *while* loop.

The *rjust()* method returns a new string of given length after substituting a given character (in this case X) in the left side of the original string. [rjust method](https://www.geeksforgeeks.org/python-string-rjust-method/).

Slicing in Python gets a sub-string from a string and negatove indexing is used to begin slicing from the end of the string.  In order to get the last 4 digits only I used -4 in my code.

This code can easily be modified to deal with account numbers of any size by simply removing the validation code contained withinbg the *while* loop.