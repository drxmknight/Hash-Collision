from hashlib import blake2b
from itertools import product
from string import ascii_letters
import time

# Hash size in bytes.
hash_size = 3

# Number of experiments.
experiments = 100

# Number of letters by word
word_length = 3


def main():
    print("Generating dictionary ...")
    # Al possible combinations of 3 letters.
    words = [''.join(i) for i in product(ascii_letters, repeat=word_length)]
    # Use set for faster search of hashes.
    hash_set = set()
    print("-- Hashing started --")
    # Set start time to measure collision.
    start_time = time.time()
    # The input message.
    collision_count = 0

    total_duration = 0

    for msg in words:
        # Message in bytes.
        byte_str = msg.encode()
        # Hash object constructor, with hash length=3 bytes (24 bits).
        digest = blake2b(byte_str, digest_size=hash_size)
        # Generate the message digest.
        hashed_msg = digest.hexdigest()

        if hashed_msg in hash_set:
            # Get collision time duration.
            duration = time.time() - start_time
            # print("Found a collision - word: {} -> hash: {} in {} seconds.".format(msg, hashed_msg, duration))
            # Empty the hash in every collision.
            hash_set = set()
            # Restart timer.
            start_time = time.time()
            collision_count += 1
            total_duration += duration

        if collision_count == experiments:
            total_duration = total_duration / experiments
            print("Collisions found: {}".format(experiments))
            print("Average collision found time : {} seconds.".format(total_duration))
            return

        # Adds a new hash value to the set.
        hash_set.add(hashed_msg)

    if collision_count != 0:
        total_duration = total_duration / collision_count
        print("Collisions found: {}".format(collision_count))
        print("Average collision found time: {} seconds.".format(total_duration))

    else:
        print("No collisions found!")


if __name__ == '__main__':
    main()
