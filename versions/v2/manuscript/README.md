# An alternative proof of Ianakiev's shortest-palindrome conjecture

Haobo Ma (ChronoAI Pte Ltd, Singapore), then Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore).

## Build

Build the main source with Tectonic 0.17.0, then run the exact-integer checker:

```sh
tectonic note.tex
python3 verify.py
```

Alternatively, run `pdflatex note.tex` twice. The bibliography is included in the main source; no BibTeX step or external figure is needed. The checker uses Python 3's standard library and writes `verification.json` next to itself. Its output matches the included JSON. Assertions must remain enabled.

## Mathematical coverage

The note proves both clauses of Ivan N. Ianakiev's August 20, 2019 comment in OEIS A094373: the entire first-occurrence list and the position identity. It preserves the exceptional value P(1)=1 and proves P(i)=2^(nu_2(i-1)+1)+1 for every i>=2.

The proof is presented as a deduction from Fici, Gagie, Kärkkäinen and Kempa's earlier Zimin-word suffix theorem (2014, Section 5, Lemma 12 and its proof) and Kullmann and Zhao's factorial-plateau identity (2015, Lemma 3.11), with a self-contained endpoint-spacing proof. No priority claim is made.

Written corollaries give the exact radius criterion for every ruler-word palindrome; suffix lengths; occurrence counts and densities; divisor-power quotients with identical palindromic factors; all four A296306 assertions; ruler sums, coincidence and square-free descriptions; elementary transforms and array identities; elephant walks; and the A007843 generating function, recursion and jump condition. Hasler's 2020 equivalent divisor-power answer precedes Fried's independent 2025 proof. Fried's separate permanent correction is cited rather than presented as new.

## Declaration scope

The declaration `D5.S1.Words.Palindromes.IanakievShortestRulerPalindrome.result` contains the factorial and boundary minima, the stipulated first value, palindrome minima, strict increase of A, the complete first-occurrence equivalence and the position identity. The private helper declarations `b_succ` and `p_formula` contain the ruler bridge and shortest-length formula. Exact source:

https://github.com/the-omega-institute/trureturing/blob/3afaecc5507038586e39d8775afe7c0df3d4fc48/D5/S1/Words/Palindromes/IanakievShortestRulerPalindrome.lean

The additional corollaries have written proofs in the note; they are not additional statements of `result`. The Python checker supplies finite consistency checks, with all ranges and counts in `verification.json`. Its finite computations do not replace the unbounded proofs.

License: CC BY 4.0 (`cc-by-4.0`), https://creativecommons.org/licenses/by/4.0/.
