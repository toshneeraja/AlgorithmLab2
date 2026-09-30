# AlgorithmLab - Interactive Problem Solving Toolkit

**Course:** CSE1021 - Problem Solving / Python
**Student:** Neeraja Tosh
**Registration Number:** 26BCE10574
**GitHub:** toshneeraja

## 1. Project Overview

AlgorithmLab is a menu-driven **command-line** program written in Python.
It lets a user run fundamental algorithms, number algorithms, array/list
techniques and Python data-structure demonstrations, and see the time and
space complexity of each algorithm. All algorithm logic is written by hand
inside a single file, `main.py`. The purpose is educational (algorithmic
problem solving).

## 2. Problem Statement

Students learn many small algorithms (factorial, GCD, primes,
array partitioning, etc.) one at a time, but seldom get one place to run
them with their own inputs and to compare how efficient they are.
AlgorithmLab provides that place: one interactive terminal program with
input validation, worked examples and a complexity reference.

## 3. Objectives

- Implement the basic CSE1021 algorithms manually using loops,   conditions,functions, and tuple assignment.
- Demonstrate lists, tuples, sets and dictionaries.
- Show the basic approach, time complexity and space complexity of each algorithm.
- Build a program that does not crash on invalid input.

## 4. Features

- Six modules reached from one main menu, each with a Back option.
- 9 fundamental algorithms, 8 number algorithms, 7 array/list options.
- Interactive data-structure demonstrations plus a list-vs-set membership comparison.
- Complexity information for 23 implemented algorithms.
- Built-in examples that need no input and no external file.
- Input validation for: empty input, letters instead of numbers, negative
  values, zero where a positive number is needed, invalid menu choices,
  invalid arrays, invalid `k`, invalid base, invalid character, invalid
  Unicode value, pivot index out of range, division by zero, and
  Ctrl+C / Ctrl+D.

## 5. Course Concepts Demonstrated

| Concept | Where it appears in `main.py` |
|---|---|
| Problem solving, algorithm analysis, efficiency | Module 5 (Complexity), Module 4 list-vs-set comparison |
| Variables, expressions | Throughout |
| Functions, parameters, return values | Every algorithm is a function, e.g. `gcd(a, b)` |
| Tuple assignment | `exchange_values`, `gcd`, `fibonacci_sequence`, `reverse_array` |
| Conditional statements and loops | All algorithms (`if`, `while`, `for`) |
| Fundamental algorithms | Exchange, counting, summation, factorial, Fibonacci, reverse, base conversion, character/Unicode |
| Number algorithms | Newton's square root, smallest divisor, GCD, Sieve of Eratosthenes, prime factors, LCG, fast power, nth Fibonacci |
| Array/list techniques | Reverse, count, maximum, remove duplicates (sorted), partition, kth smallest |
| Lists, tuples, sets, dictionaries | Module 4 and Module 3 option 7 |
| Exception handling | `try/except` for invalid numbers, Ctrl+C and Ctrl+D |

## 6. Functional Modules

1. **Fundamental Algorithms** - exchange two values; count elements by a
   condition; sum of first n numbers; factorial (iteration); Fibonacci
   sequence; reverse a number; decimal to another base (2-16); character to
   Unicode value; Unicode value to character.
2. **Number Algorithms** - square root (Newton's method); smallest divisor;
   GCD (Euclidean); primes up to n (Sieve of Eratosthenes); prime
   factorization; pseudo-random numbers (Linear Congruential Generator);
   fast exponentiation; nth Fibonacci number.
3. **Array/List Algorithms** - reverse an array; count occurrences; find
   maximum; remove duplicates from a sorted array; partition around a
   pivot; kth smallest element; list/tuple/set/dictionary demonstration.
4. **Data Structure Demonstration** - list, tuple, set, dictionary, and
   membership search (list vs set).
5. **Algorithm Complexity** - choose an algorithm to see its approach, time
   complexity and space complexity, or show all.
6. **Examples** - built-in sample runs of fundamental, number and array algorithms.

## 7. Technologies Used

- Language: Python 3
- **Python standard library only** 
- **No external dependencies**
- **Command-line interface** (terminal)
- **Educational / problem-solving purpose**

## 8. Project Structure

```
AlgorithmLab/
├── main.py
└── README.md
```

## 9. Installation / Setup

No installation is needed. Python 3 (3.8 or newer) must be installed.

```bash
git clone <your-repository-url>
cd AlgorithmLab
python --version
```

There is nothing to install with `pip`.

## 10. How to Run

From the folder containing `main.py`:

```bash
python main.py
```

(On some systems the command is `python3 main.py`.)

The main menu appears immediately:

```
==================================================
                   ALGORITHMLAB
             Problem Solving Toolkit
==================================================
1. Fundamental Algorithms
2. Number Algorithms
3. Array/List Algorithms
4. Data Structure Demonstration
5. Algorithm Complexity
6. Examples
7. Exit

Enter your choice:
```

Type a number and press Enter. In every submenu the last number is **Back**;
in the main menu the last number is **Exit**.

## 11. Example Usage

Main menu -> `1` (Fundamental) -> `4` (Factorial):

```
Enter your choice: 4
Enter n (0 to 1000): 5
Result -> 5! = 120
```

Main menu -> `2` (Number) -> `5` (Prime factorization):

```
Enter your choice: 5
Enter an integer >= 2 (up to 10**12): 84
Result -> 84 = 2 x 2 x 3 x 7
Prime : how many times -> {2: 2, 3: 1, 7: 1}
```

Main menu -> `1` -> `7` (Base conversion):

```
Enter a non-negative decimal number: 255
Enter the base (2 to 16): 16
Result -> 255 in base 16 = FF
```

## 12. Input/Output Examples

**Invalid input is rejected and the user can try again:**

```
Enter n (0 to 1000): abc
Invalid input. Please enter an integer from 0 to 1000.
Enter n (0 to 1000): -3
Invalid input. Please enter an integer from 0 to 1000.
Enter n (0 to 1000): 5
Result -> 5! = 120
```

**Invalid menu choice:**

```
Enter your choice: 99
Invalid choice. Please enter a number from 1 to 7.
```

**Invalid pivot index (array of 5 elements):**

```
Enter array elements: 5 3 8 1 9
Enter pivot index (0 to 4): 7
Invalid input. Please enter an integer from 0 to 4.
Enter pivot index (0 to 4): 2
Original: [5, 3, 8, 1, 9]   pivot value = 8
Result -> After partition: [5, 3, 1, 8, 9]
Pivot 8 is now at index 3. Items before it are smaller; items after it are not smaller.
```

**kth smallest (Module 3, option 6):**

```
Enter array elements: 7 2 9 1 5
Enter k (1 to 5): 3
Result -> Smallest element number 3 is 5
```

**Fast exponentiation (Module 2, option 7):**

```
Enter base (-1000 to 1000): 2
Enter exponent (0 to 1000): 10
Result -> 2 ^ 10 = 1024
Loop ran 4 times (normal method needs 10 multiplications).
```

**Built-in example (Module 6, option 2):**

```
  sqrt(25) by Newton     = 5.0 in 7 iterations
  GCD(48, 18)            = 6
  smallest divisor of 91 = 7
  primes up to 30        = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  prime factors of 84    = [2, 2, 3, 7]
  2 ^ 10 (fast power)    = 1024
```

## 13. Complexity Analysis

`n` = input value or list length, `d` = number of digits, `e` = exponent,
`k` = how many numbers are generated. This table matches the Module 5 screen.

| Algorithm | Approach | Time | Space |
|---|---|---|---|
| Exchange two values | Tuple assignment | O(1) | O(1) |
| Count elements by condition | Check each element once | O(n) | O(1) |
| Sum of first n numbers | Loop adding 1..n | O(n) | O(1) |
| Factorial (iteration) | Multiply running result by 2..n | O(n) multiplications | O(1) extra variables |
| Fibonacci sequence | Two previous terms, list of results | O(n) | O(n) |
| Reverse a number | `% 10` and `// 10` per digit | O(d) | O(1) |
| Decimal to another base | Repeated division, collect remainders | O(log n) digits | O(log n) |
| Character <-> Unicode | `ord()` / `chr()` | O(1) | O(1) |
| Square root (Newton) | Repeat `(guess + n/guess)/2` | About O(log n) iterations | O(1) |
| Smallest divisor | Try 2, 3, ... while `i*i <= n` | O(sqrt n) | O(1) |
| GCD (Euclidean) | Replace `(a, b)` by `(b, a % b)` | O(log(min(a, b))) | O(1) |
| Generate primes (Sieve) | Cross out multiples | O(n log log n) | O(n) |
| Prime factorization | Trial division | O(sqrt n) worst case | O(log n) |
| Pseudo-random (LCG) | `(a*x + c) % m`, k times | O(k) | O(k) |
| Fast exponentiation | Square base, halve exponent | O(log e) multiplications | O(1) extra variables |
| nth Fibonacci | Loop keeping last two values | O(n) | O(1) |
| Reverse an array | Swap from both ends (in place) | O(n) | O(1) |
| Count occurrences | Compare each element | O(n) | O(1) |
| Find maximum | Track largest so far | O(n) | O(1) |
| Remove duplicates (sorted) | Read/write positions, in place | O(n) | O(1) |
| Partition around pivot | One pass with a boundary | O(n) | O(1) |
| kth smallest | Insertion-sort a copy, take index k-1 | O(n^2) worst case | O(n) |
| Membership search | List: one by one; set: hashing | List O(n); set O(1) average | O(n) to store |

Notes: Factorial, Fibonacci, and power work with very large integers, so
the cost of each multiplication or addition also grows with the number of
digits; the table counts operations. kth smallest deliberately uses a
simple insertion sort so it is easy to understand, which is slower than
more advanced methods.

## 14. Limitations

- Teaching tool for small inputs, not a production library. Limits are
  placed on some inputs (for example n up to 1000 for factorial, up to
  1,000,000 for the sieve) to keep the program fast.
- The LCG pseudo-random generator is for demonstration only and is not secure.
- Newton's square root uses floating-point numbers and a fixed tolerance
  (1e-10), so results are approximate.
- Only whole numbers (integers) are accepted as numeric input.
- No data is saved between runs; the program is single-user.
- Some terminals cannot display every Unicode character; the program then shows a message instead of crashing.

## 15. Future Enhancements

- Add a faster kth-smallest method (quickselect) and compare it with the current one.
- Add more algorithms such as binary search and simple sorting comparisons.
- Allow decimal (floating-point) input for the square root.
- Save a session's results to a text file.

## 16. Author

**Neeraja Tosh**
Reg. No. 26BCE10574
VIT Bhopal, CSE1021 - Problem Solving / Python
GitHub: [toshneeraja](https://github.com/toshneeraja)

