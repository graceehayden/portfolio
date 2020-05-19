# Write a function that checks whether any permutation of
# an input string is a palindrome
# patterns used:  what is required of the end result?
#     i.e. all letters are even numbered except one
#     then, how do i check for that?
#     i.e. need to get all unique letters in word and a count of each

def check_if_palindrome(word):
    unique_letters = set(word)
    even_letter_count = 0
    odd_letter_count = 0

    for letter in unique_letters:
        if (word.count(letter) % 2) == 0:
            even_letter_count = even_letter_count + 1
        else:
            odd_letter_count = odd_letter_count + 1

    if (len(word) % 2) == 0:
        word_is_even_number = True
    else:
        word_is_even_number = False

    if word == '':
        answer = "Enter a word, ya loon!"
    elif (word_is_even_number and odd_letter_count > 0) or (not word_is_even_number and odd_letter_count > 1):
        answer = "No palindrome here"
    else:
        answer = "We can make a palindrome!"

    return answer
#word = input("Enter a word: ")
#answer = check_if_palindrome(word)
#print(answer)


def merge_sort_lists(list1, list2):
    merged_list = list1 + list2
    return sorted(merged_list)

#list1 = ["animal", "trees", "television", "nature"]
#list2 = ["office", "cars", "vacation"]
#print(sort_and_merge_lists(list1, list2))
