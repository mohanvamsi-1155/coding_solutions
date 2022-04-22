"""
    Question: Implement an algorithm to check if a string has all unique characters
"""


"""
    Notes: 
    brute_force_solution: Time Complexity: O(n^2) Space Complexity: O(1)
                            One major problem is the time.
"""
def brute_force_solution(s):
    is_unique = True
    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                continue
            if s[i] == s[j]:
                is_unique = False
                break
    return is_unique

"""
    Notes: 
    brute_force_solution_optimization_1: Time Complexity: O(n^2) Space Complexity: O(1)
    time complexity is still O(n^2) but, instead of looping over all failure cases we can return when we found one
"""

def brute_force_solution_optimization_1(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                continue
            if s[i] == s[j]:
                return False
    return True

"""
    Notes: 
    optimized_solution_1: Time Complexity: O(n log(n) + n) => O(n log(n)) Space Complexity: O(1)
"""

def optimized_solution_1(s):
    sorted_str = sorted(s)
    for i in range(len(s)-1):
        if sorted_str[i] == sorted_str[i+1]:
            return False
    return True

"""
    Notes:
    optimized_solution_2: Time Complexity: O(n) Space Complexity: O(n)

"""

def optimized_solution_2(s):
    hash_set = set()
    for ch in s:
        if ch in hash_set:
            return False
        hash_set.add(ch)
    return True


if __name__ == "__main__":
    test_1 = "bbaacdeace"
    print(brute_force_solution(test_1))
    print(brute_force_solution_optimization_1(test_1))
    print(optimized_solution_1(test_1))
    print(optimized_solution_2(test_1))
    test_2 = "abcde"
    print(brute_force_solution(test_2))
    print(brute_force_solution_optimization_1(test_2))
    print(optimized_solution_1(test_2))
    print(optimized_solution_2(test_2))