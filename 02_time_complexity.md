# Time Complexity

## Asymptotic time complexity

Note: discarding/ignoring previous knowledge might help for this.

Idea: We have a algorithm which processes an object with "n" length (bit length, length of list, num vertices, etc...)
Q: How does time change with respect to "n" as $n \rightarrow \infty$?

A specific answer might be: $T(n) = 5n^2 + 6n + 1$, but this is basically impossible to have accurate, too specific

Instead, we use $O(n)$, $\Omega(n)$, and $\theta(n)$

### $O(n)$

**Definition**: $f(n) \in O(g(n))$ when $\exists n_0,C > 0 \ \forall n \ge n_0 \ f(n) \le C \times g(n)$


Prove from the definition:
Suppose we want to prove $f(n) \in O(g(n))$

General strategy
break function down into parts

$f(n) = f_0(n) + f_1(n) + ... + f_m(n)$

if $f_i(n) = D * g(n)$, then C = D, n_0 = 0

otherwise, solve for n in $f_i(n) \le g(n)$, 

note that if $f_i(n) \le 0$, C=0 n_0 free is sufficient, so you don't need to worry about this term

Then we get C = \#functions solved second way + sum of all C from first way
and we get n_0 to be the maximum n in all the parts solved.

Big O provides an **upper** bound, sometimes we want a lower bound or something else.

### $\Omega(n)$ and $\theta(n)$

1. Ω provides a lower bound $\forall n_0, B > 0 n \ge n_0 \to f(n) > B \times g(n)$
2. θ provides both bounds. $\forall n_0, B > 0, C > 0 n \ge n_0 \to B \times g(n) > f(n) > C \times g(n)$

> [!NOTE]
> To prove big theta, prove big omega and big O. Won't be asked typically

Strategy to prove $\Omega(n)$

As with O(n), we break down f(n)
$f(n) = f_0(n) + f_1(n) + ... + f_m(n)$

For $\Omega(n)$, we ignore all $f_i(n) > 0 \text{where} f_i(n) \ne C \times g(n)$

If we have a negative term, we need to replace $f_i(n)$ with $C \times g(n)$ 
such that $\forall n_0, C > 0 n \ge n_0 C \times g(n) \ge f_i(n)$.

Ex)

$\Omega(n^2 \times \lg(n)) = n^2 \times \lg(n) + 8n^2 + n + 1$

as the n^2 * lg(n) is the main term, and all other terms are '+'.

Ex)

$$ 
\text{show that:} 3n^2 - n = \Omega(n^2) \\
n^2 \ge n, n_0 = 1 \\
3n^2 - n \ge 3n^2 - n^2 \ge 2n^2 n_0 = 1 \\
B=2, n_0=1, so 3n^2 - n = \Omega(n^2)
$$

Also, you can use 0<C<1 if a coefficient of g(n) is not enough for each term.

### General

We like to use nice functions for big O and big Omega

Our nice functions are
1, lg n, n, n lgn, n^2, n^2 lgn, 2^n, 3^n, 4^n ..., n!, n^n

it can be proven that lg(n) = C * log_b(n) for any b, so O(lg n) is for ALL log bases

Intuition: given f(n), find largest term, that is probably O(n) and Omega(n)

> [!CAUTION]
> The biggest term is never going to be negative, because what kind of function gets faster with more data?
> Just take largest positive bit in this case

## Big Limit Theorems

Suppose we have functions f(x) and g(x).
1. if $\lim_{x\to\infty} f(x)/g(x) \ne \infty$ then $f(x) = O(g(x)$
2. if $\lim_{x\to\infty} f(x)/g(x) \ne 0$ then $f(x) = \Omega(g(x)$
3. if $\lim_{x\to\infty} f(x)/g(x) \ne 0, \infty$ then $f(x) = \theta(g(x)$

#### Some derivatives to remember

> [!NOTE]
> L'Hopitals rule may be useful for solving the limit defintions above, so differentiating f(x) and g(x) may be necessary

1. $\frac{d}{dx} \ln x = \frac{1}{x}$
2. $\frac{d}{dx} \log_b x = \frac{1}{x \ln b}$
3. $\frac{d}{dx} \lg x = \frac{1}{x \ln 2}$
4. $\frac{d}{dx} e^x = e^x$
5. $\frac{d}{dx} b^x = b^x \ln(b)$
6. $\frac{d}{dx} 2^x = 2^x \ln(2)$

Let's prove that $\log_b(x) = \theta(\lg(x))$

$$
\lim_{x\to\infty} \frac{\log_b(x)}{\lg(x)} = \frac{\infty}{\infty} \\
\lim_{x\to\infty} \frac{\frac{1}{x \ln b}}{\frac{1}{x \ln 2}} \\
\frac{ln(2)}{\ln(b)} \ne 0, \infty \\
\blacksquare
$$

### Time Analysis

Q: When analyzing code, if all we need is $\theta(n) \text{ or } O(n) \text{ or } \Omega(n)$, what do we need to care about?

Consider the following
```j-pseudo
sum = 0
for i = 1 to n inclusive:
    sum = sum + i
    if floor(i/2) == i/2 then:
        sum = sum + 5
    end if
end for
return (sum)
```

For the exact time T(n), we'd need every single lines runtime.
Buf if we just want one of our Big Asymptotic time complexities, we only want to focus on things that run N times.

- The code `sum = 0` and `return (sum)` are both O(1)
- The code inside the for loop, also runs at O(1), but it runs N times, so the complexity is O(n)

This leads to O(n) code
