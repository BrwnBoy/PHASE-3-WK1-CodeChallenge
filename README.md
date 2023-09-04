# PHASE-3-WK1-CodeChallenge
Authour:**Brian Mwangi Maina**

## Prerequisites:

**Technologies Used**

<li>Python

**Setup/Installation Requirements**

*To run the application, in your terminal*

<li>Open the terminal and clone the repository to your local machine: git clone git@github.com:BrwnBoy/PHASE-3-WK1-CodeChallenge.git//
<li>cd into *PHASE-3-WK1-CodeChallenge*
<li>Finally, open up vs.code by typing in (code .) while in the repository.

### How Each of the Programs Run:

*Convert.Py* -*In this code, I first format the input hour, minute, and period into a time string in 12-hour format. I then use the datetime.strptime function to parse the time string into a datetime object. Finally, I format the DateTime object into a 24-hour time string using the strftime method and return the result.*

*Two_Numbers.Py* -*In this code, I use a generator expression inside the sum function to count the number of positive numbers. The generator expression iterates over the list of numbers and generates a sequence of 1s and 0s, where 1 corresponds to a positive number and 0 corresponds to a non-positive number. The sum function then sums up these 1s and 0s to give the count of positive numbers.*

*Consonant.Py* -*In this code, I initialize the maximum value and the current value to 0. I then iterate over each character in the string. If the character is a consonant, I add its alphabetic value to the current value and update the maximum value. If the character is a vowel, I reset the current value. Finally, I return the maximum value. The alphabetic value of a character can be obtained by subtracting 96 from its ASCII value, which can be obtained using the ord function.*

#### License 

Copyright (c) 2023 Brian Mwangi Maina

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
