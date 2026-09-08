1. What is the question?

You are given an array like:

[1, 3, 20, 4, 1, 0, 2]

You need to find the index of any peak element.

A peak element is an element that is greater than its neighbors.

For example:

[1, 3, 20, 4, 1, 0, 2]
       ↑
      20

20 is greater than:

left neighbor → 3
right neighbor → 4

So 20 is a peak.

Its index is:

0  1   2  3  4  5  6
1  3  20  4  1  0  2
      ↑

Therefore:

answer = 2