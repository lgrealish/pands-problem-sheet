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

    Write a program that reads in a 10 character account number and
    outputs the account number with only the last 4 digits showing
    (and the first 6 digits replaced with Xs).

Although not specified I've added a validation rule that prompts the user to enter the account number again if it is less than ten digits.  This is done by using a *while* loop.

The *rjust()* method returns a new string of given length after substituting a given character (in this case X) in the left side of the original string. [rjust method](https://www.geeksforgeeks.org/python-string-rjust-method/).

Slicing in Python gets a sub-string from a string and negatove indexing is used to begin slicing from the end of the string.  In order to get the last 4 digits only I used -4 in my code. [Negative Indexing](https://www.tutorialspoint.com/what-is-a-negative-indexing-in-python)

Because the rjust() function removes the last 4 numbers in a string, this code can easily be modified to deal with account numbers of any size by simply removing the validation code contained within the *while* loop in line 12, 13, 18.

### ***Collatz***

    Write a program that asks the user to input any positive integer
    and outputs the successive values of the following calculation.
    At each step calculate the next value by taking the current value 
    and, if it is even, divide it by two, but if it is odd, multiply 
    it by three and add one.

Although not specified I've added a validation rule that prompts the user to 'Try again' if a negative number is input.  This is done by using a *while* loop.

The next step was to define the collatz() function that I wanted to run.  Again this is done with a *while* loop which runs until we achieve a value of 1.  This *while* loop contains conditional statements *if* and *else* that signify what action should happen depending on whether the number is odd or even.

All of the results at each iteration are appended to a list.

### ***Weekday***

    Write a program that outputs whether or not today is a weekday.

In order to manipulate the date and time I imported the *datetime* module.  Using the *datetime* module and the function *today()* the code determines todays date.  The *weekday()* function returns the day of the week as an integer where Monday is 0 and Sunday is 6. [weekday](https://pythontic.com/datetime/date/weekday)

An *if* and *else* statement return the corresponding strings if today() is a weekday or not.

### ***Python-squareroot***

    Write a program that outputs whether or not today is a weekday.

In order to manipulate the date and time I imported the *datetime* module.  Using the *datetime* module and the function *today()* the code d
