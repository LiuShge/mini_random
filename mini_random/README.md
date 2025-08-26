# mini_random

High-Precision Nested Pseudo-Random Number Generator (PRNG) implemented in Python  
Author: LiuShge

---

## Overview

`mini_random` is a **high-precision nested pseudo-random number generator (PRNG)** written in Python.  
It can generate multiple types of random numbers, including integers, big integers, and high-precision floating-point numbers.  
The generator supports multiple layers of nesting to improve randomness and allows configurable precision for floating-point numbers.  

Ideal for scientific computing, simulations, randomized testing, or any scenario where reproducible random sequences are needed.

---

## Features

- Generates:
  - 64-bit integers  
  - Arbitrary-precision big integers  
  - High-precision floating-point numbers (configurable precision)  
- Multi-layer nesting for enhanced randomness  
- Seed-based initialization for reproducible sequences  
- Uses Python's built-in `decimal` module for precise floating-point control  

---

## Installation

Simply download the `mini_random.py` file to use—no additional dependencies required.  

Or clone the repository:

```bash
git clone https://github.com/LiuShge/python_toolkit.git
```
## Usage
```python
from mini_random import NestedPRNG

# Initialize PRNG with a seed
prng = NestedPRNG(seed=12345)

# Generate a random integer between 1 and 100
print(prng.next_int_in_range(1, 100))

# Generate a high-precision floating-point number between 0 and 1
print(prng.next_float_in_range(0, 1))

# Generate a big integer in a specified range
print(prng.next_bigint_in_range(-10**50, 10**50))
```
Example Output: 

42 

0.734829182374982734 

-9708196413034723149118309935275652529732012143283 


  Note: Results vary depending on the seed. Using the same seed ensures reproducible sequences.

## Use Cases

 Scientific simulations and calculations

 Big integer operations and testing

 Debugging random algorithms

 Experiments requiring reproducible and controlled randomness

## Contributing

Feel free to fork, submit pull requests, or open issues and suggestions.

## License

MIT License
