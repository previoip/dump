a = [
    ["eat","tea","tan","ate","nat","bat"]
]

import time

def solve(strs):
    def assert_anagram(s1, s2):
        return sorted(s1) == sorted(s2)

    res = [[strs.pop(0)]]

    for i in strs:
        for j in res:
            if assert_anagram(i, j[0]) and i not in j:
                j.append(i)
                break
        else:
            res.append([i])

        print(res)
        time.sleep(.2)
    return res

if __name__ == '__main__':
    for i in a:
        print(solve(i))