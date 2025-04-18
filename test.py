def containsDuplicate(arr):
    seen = {}
    for item in arr:
        if item in seen:
            return True
        else:
            seen[item] = item
    return False


def get_number_of_subsequence(s: str, words: list[str]):
    number_of_subsequence = 0
    for word in words:
        if is_a_substring(s, word):
            number_of_subsequence += 1
            print(word)
    return number_of_subsequence
            
                
def get_str_freq(string: str) -> dict:
    freq_count = {}

    for char in string:
        if char in freq_count:
            freq_count[char] += 1
        else:
            freq_count[char] = 1
    return freq_count

def is_a_substring(string: str, substring: str) -> bool:
    if substring > string:
        return False
    
    string_freq = get_str_freq(string)
    substring_freq = get_str_freq(substring)

    for char in substring_freq:
        if string_freq[char] is None:
            return False
        if substring_freq[char] > substring_freq[char]:
            return False
    return True

    

print(get_number_of_subsequence("master", ['ate', 'tea', 'tame', 'tim', 'eat']))
            
