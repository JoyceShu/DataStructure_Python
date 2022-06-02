strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']


hashmap = {}
    
for q in queries:
    hashmap[q] = 0

for s in strings:
    for k, v in enumerate(hashmap):
        if s in v:
            hashmap[k] += 1        
print(hashmap)