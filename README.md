# NestedPRNG

A high-precision nested Pseudo-Random Number Generator (PRNG) implemented in Python.

## Features

- Generates 64-bit integers, big integers, and high-precision floats.
- Supports multiple layers of nesting for enhanced randomness.
- Configurable precision for floating-point numbers.

## Usage

```python
from nested_prng import NestedPRNG
prng = NestedPRNG(seed=12345)
print(prng.next_int_in_range(1, 100))
