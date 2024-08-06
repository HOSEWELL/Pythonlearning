def count_matching_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count


sample_list = ['abc', 'xyz', 'aba', '1221','xyyjkk']
result = count_matching_strings(sample_list)

print("Expected Result:", result)



#remove duplicate
def remove_duplicates(input_list):
    unique_items = list(set(input_list))
    return unique_items
sample_list = [1, 2, 2, 3, 4, 4, 5, 1]

result = remove_duplicates(sample_list)

print("List after removing duplicates:", result)

#words longer than n
def words_longer_than_n(words_list, n):
    longer_words = [word for word in words_list if len(word) > n]
    return longer_words
sample_words = ['hello', 'world', 'Python', 'is', 'great']

n = 4
result = words_longer_than_n(sample_words, n)

print("Original List:", sample_words)
print(f"Words longer than {n} characters:", result)

#common members

def common_member(lst1, lst2):
    return any(item in lst1 for item in lst2)

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print(common_member(list1, list2))  

#prime numbers

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_primes(lst):
    return all(is_prime(num) for num in lst)

print(all_primes([3, 5, 7, 13]))    


#difference in two lists

def list_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

list1 = [1, 2, 3, 4, 5]
list2 = [2, 4]
print(list_difference(list1, list2))  


#smallest number in the list

def second_smallest(lst):
    if len(lst) < 2:
        return None
    unique = list(set(lst))
    unique.sort()
    return unique[1]

list = [1, 2, 3, 4, 5]
print(second_smallest(list)) 


#unique values in a list

def unique_values(lst):
    return list(set(lst))

list = [1, 2, 3, 1, 2, 4, 5]
print(unique_values(list))

#frequency of an element // inbuilt counter

from collections import Counter

def elements(lst):
    return dict(Counter(lst))

sample_list = [1, 2, 3, 1, 2, 4, 5, 1]
print(elements(sample_list)) 

#common item

def common_item(lst1, lst2):
    return list(set(lst1) & set(lst2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(common_item(list1, list2))







