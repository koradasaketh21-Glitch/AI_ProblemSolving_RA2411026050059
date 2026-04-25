from itertools import permutations

puzzle = input("Enter puzzle (e.g., SEND+MORE=MONEY): ").replace(" ", "")
left, result = puzzle.split('=')
word1, word2 = left.split('+')

letters = list(set(word1 + word2 + result))
digits = range(10)

for perm in permutations(digits, len(letters)):
    mapping = dict(zip(letters, perm))

    if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[result[0]] == 0:
        continue

    num1 = int("".join(str(mapping[c]) for c in word1))
    num2 = int("".join(str(mapping[c]) for c in word2))
    res = int("".join(str(mapping[c]) for c in result))

    if num1 + num2 == res:
        print("\nSolution Found:")
        print(mapping)
        print(f"{num1} + {num2} = {res}")
        break
