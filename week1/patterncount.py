__author__ = 'Siddhant Srivastava'

import sys

text = sys.argv[ACTGTACGATGATGTGTGTCAAAG]
pattern = sys.argv[TGT]

def count(text,pattern):
	count = 0
	for i in range(len(text) - len(pattern) + 1):
		if text[i:i+len(pattern)] == pattern:
			count += 1
	return count

ans = count(text,pattern)

print(ans)

