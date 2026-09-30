"""
AlgorithmLab - Interactive Problem Solving Toolkit
Course : CSE1021 - Problem Solving / Python
Author : Neeraja Tosh (26BCE10574)

A menu-driven command-line program that demonstrates fundamental
algorithms, number algorithms, array/list techniques, Python data
structures and basic algorithm complexity.

Run with:  python main.py
Uses only the Python standard library (in fact, no imports at all).
"""

LINE = "=" * 50

def print_header(title, subtitle=""):

    print()
    print(LINE)
    print(title.center(50))
    if subtitle:
        print(subtitle.center(50))
    print(LINE)


def safe_print(text):
    try:
        print(text)
    except UnicodeEncodeError:
        print("(This character cannot be shown by your terminal.)")


def show_big(number):
    text = str(number)
    if len(text) <= 60:
        return text
    return text[:20] + "..." + text[-10:] + "  (" + str(len(text)) + " digits)"


def get_choice(count):
    while True:
        text = input("Enter your choice: ").strip()
        if text == "":
            print("Invalid input. Input cannot be empty.")
            continue
        try:
            choice = int(text)
        except ValueError:
            print("Invalid choice. Please enter a number from 1 to "
                  + str(count) + ".")
            continue
        if 1 <= choice <= count:
            return choice
        print("Invalid choice. Please enter a number from 1 to "
              + str(count) + ".")


def show_menu(title, options, back_label="Back", subtitle=""):
    print_header(title, subtitle)
    for number, name in enumerate(options, start=1):
        print(str(number) + ". " + name)
    print(str(len(options) + 1) + ". " + back_label)
    print()
    return get_choice(len(options) + 1)


def get_int(prompt, low=None, high=None):
    if low is not None and high is not None:
        hint = "Please enter an integer from " + str(low) + " to " + str(high) + "."
    elif low == 1:
        hint = "Please enter a positive integer."
    elif low == 0:
        hint = "Please enter a non-negative integer (0 or more)."
    elif low is not None:
        hint = "Please enter an integer that is at least " + str(low) + "."
    else:
        hint = "Please enter a whole number."

    while True:
        text = input(prompt).strip()
        if text == "":
            print("Invalid input. Input cannot be empty. " + hint)
            continue
        try:
            value = int(text)
        except ValueError:
            print("Invalid input. " + hint)
            continue
        if (low is not None and value < low) or (high is not None and value > high):
            print("Invalid input. " + hint)
            continue
        return value


def get_array(prompt, max_length=50):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("Invalid input. Array cannot be empty. Example: 7 2 9 1 5")
            continue
        parts = text.replace(",", " ").split()
        if len(parts) > max_length:
            print("Invalid input. Please enter at most " + str(max_length) + " numbers.")
            continue
        numbers = []
        valid = True
        for part in parts:
            try:
                numbers.append(int(part))
            except ValueError:
                valid = False
                break
        if not valid:
            print("Invalid array. Enter whole numbers separated by spaces. "
                  "Example: 7 2 9 1 5")
            continue
        return numbers


def is_sorted(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False
    return True


# Basic algorithms

def exchange_values(a, b):
    a, b = b, a
    return a, b


def count_matching(values, kind, number=0):
    count = 0
    for value in values:
        if kind == "even" and value % 2 == 0:
            count += 1
        elif kind == "odd" and value % 2 != 0:
            count += 1
        elif kind == "positive" and value > 0:
            count += 1
        elif kind == "negative" and value < 0:
            count += 1
        elif kind == "divisible" and value % number == 0:
            count += 1
        elif kind == "greater" and value > number:
            count += 1
    return count


def sum_first_n(n):
  
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def factorial(n):
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci_sequence(terms):
    sequence = []
    a, b = 0, 1
    for _ in range(terms):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def reverse_number(n):
    reversed_number = 0
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10
    return reversed_number


def to_base(n, base):
    digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n = n // base
    return result


# Number algorithms

def newton_sqrt(n):
    if n == 0:
        return 0.0, 0
    guess = float(n)
    iterations = 0
    while iterations < 200:
        better = (guess + n / guess) / 2
        iterations += 1
        if abs(better - guess) < 1e-10:
            return better, iterations
        guess = better
    return guess, iterations


def smallest_divisor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += 1
    return n


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    if n >= 1:
        is_prime[1] = False
    i = 2
    while i * i <= n:
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False
        i += 1
    primes = []
    for number in range(2, n + 1):
        if is_prime[number]:
            primes.append(number)
    return primes


def prime_factors(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors


# Values used by the simple random-number generator
LCG_A = 1103515245
LCG_C = 12345
LCG_M = 2 ** 31


def lcg_numbers(seed, count):
    numbers = []
    x = seed
    for _ in range(count):
        x = (LCG_A * x + LCG_C) % LCG_M
        numbers.append(x)
    return numbers


def fast_power(base, exponent):
    result = 1
    loops = 0
    while exponent > 0:
        if exponent % 2 == 1:
            result = result * base
        base = base * base
        exponent = exponent // 2
        loops += 1
    return result, loops


def nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Array and list algorithms

def reverse_array(numbers):
    left = 0
    right = len(numbers) - 1
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1
    return numbers


def count_occurrences(numbers, target):
    count = 0
    for value in numbers:
        if value == target:
            count += 1
    return count


def find_maximum(numbers):
    largest = numbers[0]
    for value in numbers:
        if value > largest:
            largest = value
    return largest


def remove_duplicates_sorted(numbers):
    if len(numbers) == 0:
        return 0
    write = 1
    for read in range(1, len(numbers)):
        if numbers[read] != numbers[write - 1]:
            numbers[write] = numbers[read]
            write += 1
    return write


def partition(numbers, pivot_index):
    last = len(numbers) - 1
    pivot_value = numbers[pivot_index]
    numbers[pivot_index], numbers[last] = numbers[last], numbers[pivot_index]
    boundary = 0
    for i in range(last):
        if numbers[i] < pivot_value:
            numbers[boundary], numbers[i] = numbers[i], numbers[boundary]
            boundary += 1
    numbers[boundary], numbers[last] = numbers[last], numbers[boundary]
    return boundary


def kth_smallest(numbers, k):
    copy = list(numbers)
    for i in range(1, len(copy)):
        current = copy[i]
        j = i - 1
        while j >= 0 and copy[j] > current:
            copy[j + 1] = copy[j]
            j -= 1
        copy[j + 1] = current
    return copy[k - 1]


# Module 1 menu

def run_exchange():
    a = get_int("Enter first value: ")
    b = get_int("Enter second value: ")
    new_a, new_b = exchange_values(a, b)
    print("Before: a = " + str(a) + ", b = " + str(b))
    print("After : a = " + str(new_a) + ", b = " + str(new_b))


def run_count():
    values = get_array("Enter array elements: ")
    conditions = ["Even numbers", "Odd numbers", "Positive numbers",
                  "Negative numbers", "Divisible by a number",
                  "Greater than a number"]
    print("Count which elements?")
    for number, name in enumerate(conditions, start=1):
        print("  " + str(number) + ". " + name)
    choice = get_choice(len(conditions))
    if choice == 1:
        print("Result -> Even numbers:", count_matching(values, "even"))
    elif choice == 2:
        print("Result -> Odd numbers:", count_matching(values, "odd"))
    elif choice == 3:
        print("Result -> Positive numbers:", count_matching(values, "positive"))
    elif choice == 4:
        print("Result -> Negative numbers:", count_matching(values, "negative"))
    elif choice == 5:
        while True:
            divisor = get_int("Enter the divisor: ")
            if divisor == 0:
                print("Invalid input. Cannot divide by zero. Enter a non-zero integer.")
            else:
                break
        print("Result -> Divisible by " + str(divisor) + ":",
              count_matching(values, "divisible", divisor))
    else:
        limit = get_int("Count elements greater than: ")
        print("Result -> Greater than " + str(limit) + ":",
              count_matching(values, "greater", limit))


def run_sum():
    n = get_int("Enter n (1 to 1000000): ", 1, 1000000)
    total = sum_first_n(n)
    print("Result -> Sum of 1 to " + str(n) + " = " + str(total))
    print("Check using formula n(n+1)/2 = " + str(n * (n + 1) // 2))


def run_factorial():
    n = get_int("Enter n (0 to 1000): ", 0, 1000)
    print("Result -> " + str(n) + "! = " + show_big(factorial(n)))


def run_fibonacci_sequence():
    terms = get_int("How many terms (1 to 100)? ", 1, 100)
    sequence = fibonacci_sequence(terms)
    print("Result ->", " ".join(str(x) for x in sequence))


def run_reverse_number():
    n = get_int("Enter a non-negative integer: ", 0)
    print("Result -> Reverse of " + str(n) + " = " + str(reverse_number(n)))
    print("(Trailing zeros disappear, e.g. 1200 becomes 21.)")


def run_base_conversion():
    n = get_int("Enter a non-negative decimal number: ", 0)
    base = get_int("Enter the base (2 to 16): ", 2, 16)
    print("Result -> " + str(n) + " in base " + str(base) + " = " + to_base(n, base))


def run_char_to_code():
    while True:
        text = input("Enter a single character: ")
        if len(text) == 1:
            break
        print("Invalid input. Please enter exactly ONE character.")
    code = ord(text)
    print("Result -> Unicode value: " + str(code) + " (hex " + hex(code) + ")")


def run_code_to_char():
    while True:
        code = get_int("Enter a Unicode value (0 to 1114111): ", 0, 1114111)
        if 55296 <= code <= 57343:
            print("Invalid input. Values 55296 to 57343 are reserved and "
                  "are not real characters.")
        else:
            break
    character = chr(code)
    print("Result -> Character representation: " + repr(character))
    if character.isprintable():
        safe_print("Character: " + character)
    else:
        print("(This is a non-printable / control character.)")


def fundamental_menu():
    options = ["Exchange two values", "Count elements satisfying a condition",
               "Sum of first n numbers", "Factorial (iteration)",
               "Fibonacci sequence", "Reverse a number",
               "Decimal to another base", "Character to Unicode value",
               "Unicode value to character"]
    actions = [run_exchange, run_count, run_sum, run_factorial,
               run_fibonacci_sequence, run_reverse_number,
               run_base_conversion, run_char_to_code, run_code_to_char]
    while True:
        choice = show_menu("MODULE 1: FUNDAMENTAL ALGORITHMS", options)
        if choice == len(options) + 1:
            return
        actions[choice - 1]()


# Module 2 menu

def run_sqrt():
    n = get_int("Enter a non-negative integer (up to 10**15): ", 0, 10 ** 15)
    root, steps = newton_sqrt(n)
    print("Result -> Square root of " + str(n) + " is about " + str(round(root, 6)))
    print("Newton's method took " + str(steps) + " iterations.")


def run_smallest_divisor():
    n = get_int("Enter an integer >= 2 (up to 10**12): ", 2, 10 ** 12)
    d = smallest_divisor(n)
    print("Result -> Smallest divisor of " + str(n) + " (above 1) is " + str(d))
    if d == n:
        print(str(n) + " is a prime number.")


def run_gcd():
    a = get_int("Enter first positive integer: ", 1)
    b = get_int("Enter second positive integer: ", 1)
    print("Result -> GCD(" + str(a) + ", " + str(b) + ") = " + str(gcd(a, b)))


def run_primes():
    n = get_int("Generate primes up to (2 to 1000000): ", 2, 1000000)
    primes = generate_primes(n)
    print("Found " + str(len(primes)) + " primes up to " + str(n) + ".")
    if len(primes) <= 100:
        print("Result ->", " ".join(str(p) for p in primes))
    else:
        print("First 100 primes:", " ".join(str(p) for p in primes[:100]))


def run_prime_factors():
    n = get_int("Enter an integer >= 2 (up to 10**12): ", 2, 10 ** 12)
    factors = prime_factors(n)
    print("Result -> " + str(n) + " = " + " x ".join(str(f) for f in factors))
    counts = {}
    for f in factors:
        counts[f] = counts.get(f, 0) + 1
    print("Prime : how many times ->", counts)


def run_lcg():
    seed = get_int("Enter seed (0 to 2147483647): ", 0, LCG_M - 1)
    count = get_int("How many numbers (1 to 20)? ", 1, 20)
    numbers = lcg_numbers(seed, count)
    print("Formula: next = (" + str(LCG_A) + " * x + " + str(LCG_C)
          + ") % " + str(LCG_M))
    for i, x in enumerate(numbers, start=1):
        print("  #" + str(i) + ": " + str(x) + "   (scaled to 1-100: "
              + str(1 + x % 100) + ")")
    print("(Same seed always gives the same sequence. Not for security use.)")


def run_fast_power():
    base = get_int("Enter base (-1000 to 1000): ", -1000, 1000)
    exponent = get_int("Enter exponent (0 to 1000): ", 0, 1000)
    result, loops = fast_power(base, exponent)
    print("Result -> " + str(base) + " ^ " + str(exponent) + " = " + show_big(result))
    print("Loop ran " + str(loops) + " times (normal method needs "
          + str(exponent) + " multiplications).")


def run_nth_fibonacci():
    n = get_int("Enter n (0 to 10000): ", 0, 10000)
    print("Result -> F(" + str(n) + ") = " + show_big(nth_fibonacci(n)))


def number_menu():
    options = ["Square root (Newton's method)", "Smallest divisor",
               "GCD (Euclidean algorithm)", "Generate primes up to n",
               "Prime factorization", "Pseudo-random numbers (LCG)",
               "Fast exponentiation", "nth Fibonacci number"]
    actions = [run_sqrt, run_smallest_divisor, run_gcd, run_primes,
               run_prime_factors, run_lcg, run_fast_power, run_nth_fibonacci]
    while True:
        choice = show_menu("MODULE 2: NUMBER ALGORITHMS", options)
        if choice == len(options) + 1:
            return
        actions[choice - 1]()


# Module 3 menu

def run_reverse_array():
    numbers = get_array("Enter array elements: ")
    print("Original:", numbers)
    print("Result -> Reversed:", reverse_array(numbers))


def run_count_occurrences():
    numbers = get_array("Enter array elements: ")
    target = get_int("Enter the value to count: ")
    print("Result ->", target, "appears", count_occurrences(numbers, target), "time(s).")


def run_maximum():
    numbers = get_array("Enter array elements: ")
    print("Result -> Maximum element:", find_maximum(numbers))


def run_remove_duplicates():
    while True:
        numbers = get_array("Enter a SORTED array (smallest first): ")
        if is_sorted(numbers):
            break
        print("Invalid input. The array must be sorted in increasing order, "
              "e.g. 1 1 2 3 3.")
    print("Original:", numbers)
    new_length = remove_duplicates_sorted(numbers)
    print("Result -> Without duplicates:", numbers[:new_length])
    print("New length:", new_length)


def run_partition():
    numbers = get_array("Enter array elements: ")
    last_index = len(numbers) - 1
    pivot_index = get_int("Enter pivot index (0 to " + str(last_index) + "): ",
                          0, last_index)
    pivot_value = numbers[pivot_index]
    print("Original:", numbers, "  pivot value =", pivot_value)
    position = partition(numbers, pivot_index)
    print("Result -> After partition:", numbers)
    print("Pivot " + str(pivot_value) + " is now at index " + str(position)
          + ". Items before it are smaller; items after it are not smaller.")


def run_kth_smallest():
    numbers = get_array("Enter array elements: ")
    k = get_int("Enter k (1 to " + str(len(numbers)) + "): ", 1, len(numbers))
    print("Result -> Smallest element number " + str(k) + " is "
          + str(kth_smallest(numbers, k)))


def run_structures_quick():
    numbers = get_array("Enter array elements: ")
    counts = {}
    for value in numbers:
        counts[value] = counts.get(value, 0) + 1
    print("List       :", numbers, "  (ordered, can change, allows repeats)")
    print("Tuple      :", tuple(numbers), "  (ordered, cannot change)")
    print("Set        :", set(numbers), "  (no repeats, no fixed order)")
    print("Dictionary :", counts, "  (value -> how many times)")


def array_menu():
    options = ["Reverse an array", "Count occurrences of a value",
               "Find maximum element", "Remove duplicates (sorted array)",
               "Partition around a pivot", "Find kth smallest element",
               "Demonstrate list, tuple, set and dictionary"]
    actions = [run_reverse_array, run_count_occurrences, run_maximum,
               run_remove_duplicates, run_partition, run_kth_smallest,
               run_structures_quick]
    while True:
        choice = show_menu("MODULE 3: ARRAY / LIST ALGORITHMS", options)
        if choice == len(options) + 1:
            return
        actions[choice - 1]()


# Module 4 - data structures

def demo_list():
    print("A LIST is an ordered collection that can be changed.")
    items = get_array("Enter list elements: ")
    print("Your list:", items, " length =", len(items))
    print("First element:", items[0], " Last element:", items[-1])
    extra = get_int("Enter a value to append: ")
    items.append(extra)
    print("After append:", items)
    items[0] = 0
    print("After changing first element to 0:", items)


def demo_tuple():
    print("A TUPLE is an ordered collection that CANNOT be changed.")
    items = tuple(get_array("Enter tuple elements: "))
    print("Your tuple:", items, " length =", len(items))
    try:
        items[0] = 99
    except TypeError:
        print("Trying items[0] = 99 gives an error: tuples cannot be changed.")
    if len(items) >= 2:
        first, second = items[0], items[1]
        print("Tuple unpacking: first =", first, ", second =", second)
        first, second = second, first
        print("After swapping with tuple assignment: first =", first,
              ", second =", second)


def demo_set():
    print("A SET keeps only unique items.")
    first_set = set(get_array("Enter numbers for set A: "))
    second_set = set(get_array("Enter numbers for set B: "))
    print("Set A:", sorted(first_set))
    print("Set B:", sorted(second_set))
    print("Union (in A or B)    :", sorted(first_set | second_set))
    print("Intersection (both)  :", sorted(first_set & second_set))
    print("Difference (A not B) :", sorted(first_set - second_set))


def demo_dictionary():
    print("A DICTIONARY stores key -> value pairs. Here: word frequency.")
    while True:
        text = input("Enter a sentence: ").strip()
        if text != "":
            break
        print("Invalid input. Sentence cannot be empty.")
    frequency = {}
    for word in text.lower().split():
        frequency[word] = frequency.get(word, 0) + 1
    for word in frequency:
        print("  " + word + " -> " + str(frequency[word]))
    unique = len(frequency)
    print("Unique words:", unique)


def demo_membership():
    print("Is a value present? Compare searching a list with a set.")
    n = get_int("Size of collection (1 to 100000): ", 1, 100000)
    target = get_int("Value to search for: ")
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    lookup = set(numbers)

    steps = 0
    found = False
    for value in numbers:
        steps += 1
        if value == target:
            found = True
            break
    print("List (1 to " + str(n) + "): checked " + str(steps)
          + " item(s) one by one -> " + ("found" if found else "not found"))
    print("Set : one hash lookup -> " + ("found" if target in lookup else "not found"))
    print("Lists search item by item, O(n). Sets and dictionaries use hashing,")
    print("which takes O(1) time on average.")


def data_structure_menu():
    options = ["List", "Tuple", "Set", "Dictionary",
               "Membership search: list vs set"]
    actions = [demo_list, demo_tuple, demo_set, demo_dictionary, demo_membership]
    while True:
        choice = show_menu("MODULE 4: DATA STRUCTURES", options)
        if choice == len(options) + 1:
            return
        actions[choice - 1]()


# Module 5 - complexity
# Each entry stores the algorithm, its basic idea, and its complexity.
# n = input size, d = number of digits, e = exponent, k = count.

COMPLEXITY_INFO = [
    ("Exchange two values", "Tuple assignment a, b = b, a.", "O(1)", "O(1)"),
    ("Count elements by condition", "Check every element once and add to a counter.",
     "O(n)", "O(1)"),
    ("Sum of first n numbers", "Loop from 1 to n adding to a running total.",
     "O(n)", "O(1)"),
    ("Factorial (iteration)", "Multiply a running result by 2, 3, ..., n.",
     "O(n) multiplications", "O(1) extra variables"),
    ("Fibonacci sequence", "Keep two previous terms; append each term to a list.",
     "O(n)", "O(n) for the list"),
    ("Reverse a number", "Take last digit with % 10, build reversed number.",
     "O(d), d = digits", "O(1)"),
    ("Decimal to another base", "Divide by the base repeatedly, collect remainders.",
     "O(log n) digits", "O(log n) for result text"),
    ("Character <-> Unicode value", "Direct ord() / chr() conversion.",
     "O(1)", "O(1)"),
    ("Square root (Newton)", "Repeat guess = (guess + n/guess)/2 until it stops changing.",
     "About O(log n) iterations (starts at n, then converges fast)", "O(1)"),
    ("Smallest divisor", "Try 2, 3, 4, ... while i*i <= n.",
     "O(sqrt n)", "O(1)"),
    ("GCD (Euclidean)", "Replace (a, b) by (b, a % b) until b is 0.",
     "O(log(min(a, b)))", "O(1)"),
    ("Generate primes (Sieve)", "Cross out multiples of each prime up to sqrt(n).",
     "O(n log log n)", "O(n)"),
    ("Prime factorization", "Trial division: divide out each divisor while i*i <= n.",
     "O(sqrt n) worst case", "O(log n) for the factor list"),
    ("Pseudo-random (LCG)", "Apply next = (a*x + c) % m, k times.",
     "O(k)", "O(k) for the list"),
    ("Fast exponentiation", "Square the base, halve the exponent (binary exponentiation).",
     "O(log e) multiplications", "O(1) extra variables"),
    ("nth Fibonacci number", "Loop n times keeping only the last two values.",
     "O(n)", "O(1)"),
    ("Reverse an array", "Swap elements from both ends moving inwards (in place).",
     "O(n)", "O(1)"),
    ("Count occurrences", "Compare each element with the target.", "O(n)", "O(1)"),
    ("Find maximum", "Keep the largest value seen so far.", "O(n)", "O(1)"),
    ("Remove duplicates (sorted)", "Two positions: read and write, in place.",
     "O(n)", "O(1)"),
    ("Partition around pivot", "One pass, moving smaller items before a boundary.",
     "O(n)", "O(1)"),
    ("kth smallest element", "Insertion-sort a copy, then take index k-1.",
     "O(n^2) worst case", "O(n) for the copy"),
    ("Membership search (list vs set)",
     "List: check items one by one. Set: hash lookup.",
     "List O(n); set O(1) on average", "O(n) to store the collection"),
]


def show_complexity(entry):
    name, approach, time_cost, space_cost = entry
    print()
    print(name)
    print("  Basic approach   : " + approach)
    print("  Time complexity  : " + time_cost)
    print("  Space complexity : " + space_cost)


def complexity_menu():
    options = [entry[0] for entry in COMPLEXITY_INFO]
    options.append("Show all (summary)")
    while True:
        choice = show_menu("MODULE 5: ALGORITHM COMPLEXITY", options,
                           subtitle="Choose an algorithm")
        if choice == len(options) + 1:
            return
        if choice == len(options):
            for entry in COMPLEXITY_INFO:
                show_complexity(entry)
        else:
            show_complexity(COMPLEXITY_INFO[choice - 1])


# Module 6 - examples

def example_fundamental():
    print("Example: factorial, Fibonacci and base conversion")
    print("  factorial(5)           =", factorial(5))
    print("  first 10 Fibonacci     =", fibonacci_sequence(10))
    print("  reverse_number(12345)  =", reverse_number(12345))
    print("  255 in base 2          =", to_base(255, 2))
    print("  255 in base 16         =", to_base(255, 16))
    print("  Unicode value of 'A'   =", ord("A"))


def example_number():
    print("Example: number algorithms")
    root, steps = newton_sqrt(25)
    print("  sqrt(25) by Newton     =", round(root, 6), "in", steps, "iterations")
    print("  GCD(48, 18)            =", gcd(48, 18))
    print("  smallest divisor of 91 =", smallest_divisor(91))
    print("  primes up to 30        =", generate_primes(30))
    print("  prime factors of 84    =", prime_factors(84))
    print("  2 ^ 10 (fast power)    =", fast_power(2, 10)[0])


def example_array():
    print("Example: array algorithms on [5, 3, 8, 1, 9, 2]")
    data = [5, 3, 8, 1, 9, 2]
    print("  maximum                =", find_maximum(data))
    print("  3rd smallest           =", kth_smallest(data, 3))
    print("  count of 8             =", count_occurrences(data, 8))
    print("  reversed               =", reverse_array(list(data)))
    parts = list(data)
    position = partition(parts, 0)
    print("  partition (pivot idx 0)=", parts, "pivot now at index", position)
    sorted_data = [1, 1, 2, 3, 3, 3, 4]
    length = remove_duplicates_sorted(sorted_data)
    print("  [1,1,2,3,3,3,4] without duplicates =", sorted_data[:length])


def examples_menu():
    options = ["Fundamental algorithm examples", "Number algorithm examples",
               "Array algorithm examples"]
    actions = [example_fundamental, example_number, example_array]
    while True:
        choice = show_menu("MODULE 6: EXAMPLES", options)
        if choice == len(options) + 1:
            return
        print()
        actions[choice - 1]()


# Main program

def main():
    options = ["Fundamental Algorithms", "Number Algorithms",
               "Array/List Algorithms", "Data Structure Demonstration",
               "Algorithm Complexity", "Examples"]
    actions = [fundamental_menu, number_menu, array_menu,
               data_structure_menu, complexity_menu, examples_menu]
    try:
        while True:
            choice = show_menu("ALGORITHMLAB", options, back_label="Exit",
                               subtitle="Problem Solving Toolkit")
            if choice == len(options) + 1:
                print("Thank you for using AlgorithmLab. Goodbye!")
                return
            actions[choice - 1]()
    except (KeyboardInterrupt, EOFError):
        print()
        print("Program ended by user. Goodbye!")


if __name__ == "__main__":
    main()
