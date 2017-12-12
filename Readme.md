# Collision resistance of hash functions.

A collision resistant hash function is one which is very hard to find the data that will generate the same hash value or digest. This is accomplished by generating a very large hash value.
This script is meant to prove that hash functions are not collision free. To prove this, we will use a hash function with a very small hash value (3 bytes) and a dictionary with words of 3 letter length combinations, so the probability of getting a collision is increased.

## Strategy used

* First, it generate a simple dictionary with words of length=4.
* Creates a set data structure (faster search) to store the hash values.
* It begin to hash the words:
    * If the hash digest is not in the set, then adds it to the set.
    * If it's already in the set, then a collision was found and the set is emptied, so we can begin a new experiment over the remaining dictionary words.


## Usage

Inside the program we have these global variables:

```python=
# Hash size in bytes.
hash_size = 3

# Number of experiments.
experiments = 100

# Number of combinations
combinations = 3
```

* hash_size: number of the hash value, in bytes.
* experiments: number of collisions needed to finish the program.
* combinations: word length used to create the dictionary. We recommend values smaller than 5, because it will generate 52^5 = 380,204,032 elements and could throw memoryError, and there is no need of more for this purpose

### Run
To execute the program:

`python hash_collision.py`


## Results

This is an example output of the program with the default values.

```
Generating dictionary ...
-- Hashing started --
Collisions found: 100
Average time between every collision: 0.03781072616577148 seconds.
```
This was pretty expected, since the probability of collision is very high.

If we change the `hash_size` value to 5,  the probability of collision is increased considerably, and we could expect that the dictionary size is not enough to find the amount of collisions required (experiments). We can uncomment the line to check that behaviour.

```python=
print("Found a collision - word: {} -> hash: {} in {} seconds.".format(msg, hashed_msg, duration))
```

```python=
Generating dictionary ...
-- Hashing started --
Found a collision - word: pumt -> hash: fccfe2b7a0 in 14.750139474868774 seconds.
Found a collision - word: tRms -> hash: d1e48fdfc6 in 6.060598611831665 seconds.
Found a collision - word: Hccg -> hash: 0263c4c32f in 15.190600633621216 seconds.
Found a collision - word: MJja -> hash: e0703bd745 in 6.33185601234436 seconds.
Found a collision - word: UOUb -> hash: 191c10b156 in 8.128683090209961 seconds.
Collisions found: 5
Average collision found time: 10.092375564575196 seconds.
```



