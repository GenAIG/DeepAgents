# Lesson Summary: Printing Prime Numbers from 1 to 100 in Python

## TL;DR
Finding prime numbers up to 100 is a classic coding challenge that serves as a bridge from brute-force thinking to highly optimized algorithms. This lesson takes developers from a basic nested-loop trial division approach to optimized step-skipping, and finally to the highly efficient **Sieve of Eratosthenes**, which shifts the paradigm from trial division to marking composites using multiplication.

## Key Takeaways
* **Prime Definitions & Limits**: Primes are natural numbers $> 1$ with only two distinct divisors (1 and itself). 1 is not a prime. Testing primality of any number $num$ only requires checking potential divisors up to $\lfloor\sqrt{num}\rfloor$.
* **Evolution of Algorithms**:
  - *Naive Trial Division*: Check all divisors up to $num - 1$. Time complexity is $O(N^2)$.
  - *Optimized Trial Division*: Skip even numbers and check divisors only up to $\lfloor\sqrt{num}\rfloor$. Time complexity is $O(N\sqrt{N})$.
  - *Sieve of Eratosthenes*: Mark multiples on a grid using multiplication. Time complexity is a near-linear $O(N \log \log N)$, requiring $O(N)$ space.
* **Beginner Pitfalls**: Common bugs include including 1 as prime, loop-else indentation issues, checking even divisors for odd numbers, and trying to modify lists during iteration.
* **Secret Weapon**: Python's unique `for-else` block provides a cleaner alternative to boolean flags in trial division loops, executing only if the loop completes without a `break`.
