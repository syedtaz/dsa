Let $w$ be an arbitrary string, and let $n = |w|$. Prove each of the following statements.

- $w$ has exactly $n + 1$ prefixes.

  Let $w = a_1a_2a_3 \dots a_n$. We can create $n-1$ pairs of the form $a_1{a_2}\cdots a_k ~\vert~ a_{k + 1}a_{k + 2} \cdots {a_n}$ where $a_1{a_2}\cdots a_k$ corresponds to the prefix. Finally, $w$ and $\epsilon$ are also valid prefixes of $w$ which brings up the count to $n+1$. $\blacksquare$

- $w$ has exactly $n$ proper suffixes.

  Let $w = a_1a_2a_3 \dots a_n$. We can create $n-1$ pairs of the form $a_1{a_2}\cdots a_k ~\vert~ a_{k + 1}a_{k + 2} \cdots {a_n}$ where $a_{k + 1}a_{k + 2} \cdots {a_n}$ corresponds to the suffix. Finally, $\epsilon$ is also a valid suffix. $\blacksquare$

- $w$ has at most $n(n + 1)/2$ distinct substrings. (Why “at most”?)

  $w$ has $n + 1$ prefixes. Each prefix is either $\epsilon$ or of the form $a_1a_2\cdots a_j$ where $1 \leq j \leq |w|$. For each prefix of the latter form, associate an $1 \leq i \leq j$.

- $w$ has at most $2n − 1$ distinct proper subsequences. (Why “at most”?)

---
