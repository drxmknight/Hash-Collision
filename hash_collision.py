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
    generate_dictionary()
    # Use set for faster search of hashes.
    hash_set = set()
    print("-- Hashing started --")
    # Set start time to measure collision.
    start_time = time.time()
    # The input message.
    collision_count = 0

    total_duration = 0

    file = open('dictionary.txt', 'r')

    for msg in file:
        # Delete \n at the end of string.
        msg = msg.rstrip()
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


# Generate a dictionary file. If it already exist, then only reads from it.
def generate_dictionary():
    try:
        # Check if the dictionary file exist.
        file = open('dictionary.txt', 'r')
        print("Opening dictionary ...")
        file.close()
        return
    except IOError:
        print("Generating dictionary ...")

    file = open('dictionary.txt', 'w')

    # All possible combinations of n=word_length letters.
    for i in product(ascii_letters, repeat=word_length):
        file.write(''.join(i) + '\n')
    file.close()


if __name__ == '__main__':
    main()
