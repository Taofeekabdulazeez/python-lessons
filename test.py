def containsDuplicate(arr):
    seen = {}
    for item in arr:
        if item in seen:
            return True
        else:
            seen[item] = item
    return False


def number_of_subsequence(s: str, words: list[str]):
    # count 's' letter frequence
    str_char_freq = {}
    for char in s:
        if char in str_char_freq:
            str_char_freq[char] = str_char_freq[char] + 1
        else:
            str_char_freq[char] = 1
    
    # loop words arr and get frequency of letter in each word
    for word in words:
        word_freq_count = {}
        for char in word:
            if char in word_freq_count:
                word_freq_count[char] = word_freq_count[char] + 1
            else:
                word_freq_count[char] = 1
        for c in word_freq_count.keys():
            if str_char_freq[c] is None:
                return
            if str_char_freq[c] < word_freq_count[c]:
                return
            
                
        
    

print(number_of_subsequence("aeiouu", []))
            
