from itertools import permutations
if __name__ == '__main__':
    s, k = input().split()
    l = list(s.upper())
    per = list(permutations(l, int(k)))
    l2 = sorted(per)
    for i in l2:
        print(''.join(i))