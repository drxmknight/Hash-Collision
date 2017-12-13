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
* combinations: word length used to create the dictionary. We recommend values smaller than 5, because it will generate 52^5 = 380,204,032 elements and could take some time.

### Run
To execute the program:

`python hash_collision.py`


## Results

This is an example output of the program with the default values (dictionary already generated).

```
Opening dictionary ...
-- Hashing started --
Collisions found: 100
Average collision found time : 0.011317360401153564 seconds.

```
This was pretty expected, since the probability of collision is very high.

If we change the `hash_size` value to 5,  the probability of collision is decreased considerably, and we could expect that the dictionary size is not enough to find the amount of collisions required (experiments) or even found one, so we need to increase the dictionary size to words of length=4. We can uncomment the following line to check that behaviour.

```python=
print("Found a collision - word: {} -> hash: {} in {} seconds.".format(msg, hashed_msg, duration))
```

```python=
Generating dictionary ...
-- Hashing started --
Found a collision - word: pumt -> hash: fccfe2b7a0 in 5.3753745555877686 seconds.
Found a collision - word: tRms -> hash: d1e48fdfc6 in 1.528867244720459 seconds.
Found a collision - word: Hccg -> hash: 0263c4c32f in 4.566152811050415 seconds.
Found a collision - word: MJja -> hash: e0703bd745 in 1.928964614868164 seconds.
Found a collision - word: UOUb -> hash: 191c10b156 in 2.788785934448242 seconds.
Collisions found: 5
Average collision found time: 3.23762903213501 seconds.
```

This mean that in a dictionary of size 52^4 = 7,311,616, and a hash size of 5 bytes, there were found only 5 collisions.