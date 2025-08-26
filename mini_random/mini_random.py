from decimal import Decimal, getcontext

# -----------------------
# High precision support
# -----------------------
# Set the precision for Decimal calculations to 200 digits
getcontext().prec = 200  

class NestedPRNG:
    """
    Nested Pseudo-Random Number Generator (PRNG) using a layered Linear Congruential Generator (LCG)
    """

    def __init__(self, seed: int = 123456789):
        # Initialize the PRNG with a seed value
        self.state = seed

    def _lcg(self, state: int) -> int:
        """
        Single-step Linear Congruential Generator (LCG)
        Formula: state = (a * state + c) % m
        Returns the next state as a 64-bit integer
        """
        a = 6364136223846793005
        c = 1442695040888963407
        m = 2**64
        return (a * state + c) % m

    def next(self, layers: int = 8) -> int:
        """
        Generate a 64-bit integer by applying the LCG multiple times (nested layers)
        Updates the internal state and returns the generated value
        """
        s = self.state
        for _ in range(layers):
            s = self._lcg(s)
        self.state = s
        return s

    # -----------------------
    # Generate 64-bit integer within a given range
    # -----------------------
    def next_int_in_range(self, low: int, high: int, layers: int = 8) -> int:
        """
        Returns a pseudo-random 64-bit integer between low and high (inclusive)
        """
        val = self.next(layers)
        span = high - low + 1
        return low + (val % span)

    # -----------------------
    # Generate big integer within a given range
    # -----------------------
    def next_bigint_in_range(self, low: int, high: int, blocks: int = 4, layers: int = 8) -> int:
        """
        Returns a pseudo-random big integer with multiple 64-bit blocks,
        then maps it to the specified range [low, high]
        """
        val = 0
        for _ in range(blocks):
            val = (val << 64) | self.next(layers)
        span = high - low + 1
        return low + (val % span)

    # -----------------------
    # Generate high precision float within a given range
    # -----------------------
    def next_float_in_range(self, min_val: Decimal, max_val: Decimal, blocks: int = 4, layers: int = 8) -> Decimal:
        """
        Returns a pseudo-random Decimal number between min_val and max_val
        Uses multiple 64-bit blocks to achieve high precision
        """
        val = 0
        for _ in range(blocks):
            val = (val << 64) | self.next(layers)
        denom = 1 << (64 * blocks)  # maximum possible value for normalization
        frac = Decimal(val) / Decimal(denom)
        return min_val + (max_val - min_val) * frac


# ===============================
# Example: generate random numbers 100 times
# ===============================
if __name__ == "__main__":
    # Initialize PRNG with a custom seed
    gen = NestedPRNG(seed=92345432345698767761)

    # Sets to keep track of unique values
    int_set = set()
    bigint_set = set()
    float_set = set()

    for i in range(10):
        # Generate random numbers of different types
        int_val = gen.next_int_in_range(-10**5, 10**5)
        bigint_val = gen.next_bigint_in_range(-10**50, 10**50)
        float_val = gen.next_float_in_range(Decimal("-1e50"), Decimal("1e50"))

        # Store in sets to count unique values
        int_set.add(int_val)
        bigint_set.add(bigint_val)
        float_set.add(float_val)

        # Print generated values
        print(f"===== Iteration {i+1} =====")
        print("64-bit int [-120,120]:", int_val)
        print("256-bit bigint [-1050,1050]:", bigint_val)
        print("High precision float [-1e50,1e50]:", float_val)

    # Output summary of unique values
    print("\n===== Unique Values Summary =====")
    print("Unique 64-bit ints:", len(int_set))
    print("Unique 256-bit bigints:", len(bigint_set))
    print("Unique high-precision floats:", len(float_set))
