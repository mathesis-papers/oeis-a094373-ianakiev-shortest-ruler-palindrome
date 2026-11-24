# An alternative proof of Ianakiev's shortest-palindrome conjecture via Fici and collaborators' Zimin-word theorem

**Authors:** Haobo Ma, Wenlin Zhang

We give an alternative proof of both clauses of Ivan N. Ianakiev's August 20, 2019 conjecture in OEIS A094373 (revision 86, comment at export line 13) from the Zimin-word theorem of Fici, Gagie, Kärkkäinen and Kempa (2014, Section 5, Lemma 12 and its proof) and the factorial-plateau identity of Kullmann and Zhao (2015, Lemma 3.11): the shortest nontrivial palindrome starting at position i>=2 in the run-length sequence of A007843 has length 2^(nu_2(i-1)+1)+1. Equal endpoint valuations give the lower bound, and reflection about a multiple of a larger power of two attains it. Consequently, the complete first-occurrence list is 1,2,3,5,9,..., and P(A(m-1))=A(m) for every m>=2. We also characterize every palindromic factor, transfer the same minima to divisor-power quotients, and deduce Ianakiev's four related assertions on A296306, crediting the earlier answers of Hasler and Bala.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.24488706](https://doi.org/10.5281/zenodo.24488706)
- Concept DOI: [https://doi.org/10.5281/zenodo.24488705](https://doi.org/10.5281/zenodo.24488705)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [oeis-a094373-ianakiev-shortest-ruler-palindrome](https://mathesis-omega-research.apps.chrono-ai.fun/papers/oeis-a094373-ianakiev-shortest-ruler-palindrome?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). An alternative proof of Ianakiev's shortest-palindrome conjecture via Fici and collaborators' Zimin-word theorem. Mathesis, version 2. https://doi.org/10.5281/zenodo.24488706

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3afaecc5507038586e39d8775afe7c0df3d4fc48/D5/S1/Words/Palindromes/IanakievShortestRulerPalindrome.lean) | No public receipt |
| Lemma (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3afaecc5507038586e39d8775afe7c0df3d4fc48/D5/S1/Words/Palindromes/IanakievShortestRulerPalindrome.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3afaecc5507038586e39d8775afe7c0df3d4fc48/D5/S1/Words/Palindromes/IanakievShortestRulerPalindrome.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3afaecc5507038586e39d8775afe7c0df3d4fc48/D5/S1/Words/Palindromes/IanakievShortestRulerPalindrome.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3afaecc5507038586e39d8775afe7c0df3d4fc48/D5/S1/Words/Palindromes/IanakievShortestRulerPalindrome.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3afaecc5507038586e39d8775afe7c0df3d4fc48/D5/S1/Words/Palindromes/IanakievShortestRulerPalindrome.lean) | No public receipt |
| Corollary (s7) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3afaecc5507038586e39d8775afe7c0df3d4fc48/D5/S1/Words/Palindromes/IanakievShortestRulerPalindrome.lean) | No public receipt |
| Corollary (s8) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3afaecc5507038586e39d8775afe7c0df3d4fc48/D5/S1/Words/Palindromes/IanakievShortestRulerPalindrome.lean) | No public receipt |
| Corollary (s9) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3afaecc5507038586e39d8775afe7c0df3d4fc48/D5/S1/Words/Palindromes/IanakievShortestRulerPalindrome.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).
