# Python demonstration - Assignment

## Description

I've been asked to perform the following tasks:

### Array Comparison

Compare the contents of two lists of numbers (integers). One list is a target
list and the other list can be thought of as the list to operate on. This has
been called the current list in the assignment.

The goal is to output a list of additions and a list of deletions that need to
be made to the current list in order to make it identical to the target list.

The assignment's examples are ordered, but it is likely safe to assume this
should work for un-ordered lists.

### Social Media Analysis

Given a csv file that represents relationships between posts and reposts on a
social media network, analyze the total number of followers a given post has. We
are told it is safe to assume that now two posts share common followers
(including reposts.)

The csv file contains data for postId, repostId, and followrs (count of
followers) and unique posts will have a repostId of '-1'.

*Note:* I only paraphrase the assignment in this readme to ensure that I do not
attempt to apply the license of this repository to the original assigment
document, which I did not author.

## Usage and Discussion

Run Tests:

```
make check
```

Run Demo:

```
make
```

I've tried to follow some standard best practices as far codebase structure and
testing go. The testing is not particularly robust, but it helped me maintain
confidence as I implemented and altered functions.

I've got a main.py file that serves as a rudimentary demonstration, providing
the output requested in the assignment as well in a human readable format.

The Makefile currently onle does two things. It defaults to 'demo' which runs
the main.py demonstration script, and can be used to run the tests with the
'check' target.

For the social media analysis portion of the exercise I ran both an altered and
unaltered version of the sample input, just to test the robustness of my
solution, which involves building a tree.

In my research I learned that my current solution may not necessarily be the most
up-to-date, as I used the UserDict object instead of inheriting from dict
directly. The tree implementation used here can likely be improved upon.

The first portion of the exercise also uses altered sample data, however, the
original sample data is shown. Several batches of sample data were used, and I
considered creating a function to randomly generate short-to-medium lists for
use in testing, but this was deemed out of scope.
