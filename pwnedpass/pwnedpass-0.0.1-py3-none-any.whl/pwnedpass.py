#!/usr/bin/env python3

# SPDX-License-Identifier: BlueOak-1.0.0

import io
import typing

INDEX_PREFIX_SIZE = 3
INDEX_POINTER_SIZE = 8  # 64 bit file pointer
INDEX_SEGMENT_SIZE = INDEX_POINTER_SIZE * 256 ** INDEX_PREFIX_SIZE

SHA1_SIZE = 20
ENTRY_HASH_SIZE = SHA1_SIZE - INDEX_PREFIX_SIZE
COUNT_SIZE = 4  # 32 bit int
ENTRY_SIZE = ENTRY_HASH_SIZE + COUNT_SIZE

def search(f: typing.BinaryIO, target_hash: bytes) -> int:
	if len(target_hash) != SHA1_SIZE:
		raise ValueError(f'target_hash must be a valid sha1 hash, got {target_hash!r}')

	index_prefix = target_hash[:INDEX_PREFIX_SIZE]
	hash_rest = target_hash[INDEX_PREFIX_SIZE:]
	entries_loc, entries_size = _entries_location(f, index_prefix)

	f.seek(entries_loc)
	entries = memoryview(f.read(entries_size))

	for i in range(0, len(entries), ENTRY_SIZE):
		if hash_rest == entries[i:i+ENTRY_HASH_SIZE]:
			return int.from_bytes(entries[i+ENTRY_HASH_SIZE:i+ENTRY_HASH_SIZE+COUNT_SIZE], byteorder='big')
	return 0

def _entries_location(f, index_prefix: bytes) -> typing.Tuple[int, int]:
	"""returns the location and size of a block of entries, given a hash prefix"""
	index_loc = int.from_bytes(index_prefix, byteorder='big') * INDEX_POINTER_SIZE
	f.seek(index_loc)

	if index_prefix == b'\xff\xff\xff':
		# this is the last prefix, so the entries go until EOF
		first_loc = int.from_bytes(f.read(INDEX_POINTER_SIZE), byteorder='big') + INDEX_SEGMENT_SIZE
		size = -1  # when passed to read(), reads until EOF
	else:
		buf = f.read(INDEX_POINTER_SIZE * 2)
		first_loc = int.from_bytes(buf[:INDEX_POINTER_SIZE], byteorder='big') + INDEX_SEGMENT_SIZE
		second_loc = int.from_bytes(buf[INDEX_POINTER_SIZE:], byteorder='big') + INDEX_SEGMENT_SIZE
		size = second_loc - first_loc

	return first_loc, size

def main():
	import sys

	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<pwned passwords database file>', '[sha1 hash as hex]', file=sys.stderr)
		print('If the hash is omitted, read a password from stdin.', file=sys.stderr)
		sys.exit(1)

	if len(sys.argv) < 3:
		from hashlib import sha1
		from getpass import getpass

		target_hash = sha1(getpass().encode()).digest()
	else:
		target_hash = bytes.fromhex(sys.argv[2])

	with open(sys.argv[1], 'rb') as f:
		count = search(f, target_hash)
		if count is None:
			sys.exit(0)
		else:
			print(count)
			sys.exit(2)  # a hash being found is a BAD THING

if __name__ == '__main__':
	main()
