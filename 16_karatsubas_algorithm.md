# Karatsuba's Algorithm
Intro: Suppose we want to multiply two decimal numbers

Say (42)(81)

```
    42
*   81
------
     2
    40
   160 
+ 3200  
------
  3402 
```

Here, we digit 4 single digit multiplications (SDMs), which where: 1 x 2, 1 x 4, 8 x 2, 8 x 4,
then we did some addition

Given two N digit numbers, we would do N^2 SDMs to multiply them using our method (additions are negligible)

Can we do better?
