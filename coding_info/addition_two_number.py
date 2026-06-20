def two_sum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in lookup:
            return [lookup[diff], i]

        lookup[num] = i

nums = [3, 5, 6, 7]
print(two_sum(nums, 11))


# Reverse a String
def reverse_string(s):
    return s[::-1]

print(reverse_string("neha"))

##palindrome check
def palindrome(word):
    return word == word[::-1]

print(palindrome("madam"))


#Remove Duplicates from List
nums = [1,2,2,3,4,4]
unique = list(set(nums))
print(unique)


# binary addition
a = "1010"
b = "110"
print(int(a,2))
result = bin(int(a,2) + int(b,2))
print(result)
print(result[2:])

# missing number in array
nums = [1,2,3,5,6,7,8,9,10]

n = 10

expected = n*(n+1)//2
print(expected)
actual = sum(nums)

print(expected-actual)