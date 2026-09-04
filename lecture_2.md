# Lecture 2 - CMSC351

## Asymptotic time complexity

Note: discarding/ignoring previous knowledge might help for this.

Idea: We have a algorithm which processes an object with "n" length (bit length, length of list, num vertices, etc...)
Q: How does time change with respect to "n" as $n \rightarrow \infty$?

A specific answer might be: $T(n) = 5n^2 + 6n + 1$, but this is basically impossible to have accurate, too specific

Instead, we use $O(n)$, $\Omega(n)$, and $\theta(n)$


**Definition**: $f(n) \in O(g(n))$ when $\exists n_0,C \ \forall n >= n_0 \ f(n) <= C \times g(n)$


Prove from the definition:
Suppose we want to prove $f(n) \in O(g(n))$

General strategy
break function down into parts

$f(n) = f_0(n) + f_1(n) + ... + f_m(n)$

if $f_i(n) = D * g(n)$, then C = D, n_0 = 0

otherwise, solve for n in $f_i(n) <= g(n)$

Then we get C = \#functions solved second way + sum of all C from first way
and we get n_0 to be the maximum n in all the parts solved.
