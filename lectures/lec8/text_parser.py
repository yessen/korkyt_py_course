####################################
### This modules works with file ###
####################################

# Obshiy
# Data loader function
# - input:  filename
# - output: list of lines
def data_loader(filename):
    print('data_loader function')
    try:
       fin = open(filename)
       lines = fin.readlines()
       fin.close()
    except:   
       print('File ashylmadi')
       return []

    return lines

# Galymzhan
# 1. Word count function
# - input:  list of lines
# - output: dictionary of words and counts
def get_word_counts(lines):
    print('get_word_counts function')
    counts = dict()
    for line in lines:
        words = line.split()
        for word in words:
            if word not in counts:
               counts[word] = 1
            else:
               counts[word] += 1 
    return counts

# Damir
# 2. Get the number of words
# - input:  dictionary of words and counts
# - output: the number of words
def get_number_word(dict1):
    print('get_number_word function')
    lendict1 = len(dict1)
    return lendict1 

# Erkebulan + Aibek K.
# 3. Get the sum of counts of all words
# - input:  mydict - dictionary of words and counts - { word: count }
# - output: sum of all counts in dictionary
def get_sum_counts(mydict):
    print('get_sum_counts function')

# Aiya
# 4. Get the average count of words
# - input:  dictionary of words and counts
# - output: average count of words
def count_average(dict1):
    print('count_average function')
    sum=0
    for item in dict1:
        sum+=dict1[item]
    average=sum/(len(dict1))
    return average

# Sultan
# 5. Get the word's count function
# - input: 
#     - word to query
#     - dictionary of words and counts
# - output: word count
def get_count(word, dict1):   
    print('get_count function')
    b = word in dict1
    return b 
 
# Sunkar + Olzhas
# 6. Check if a word is in the dictionary
# - input: 
#     - word to check
#     - dictionary of words and counts      
# - output: True if word is in dictionary, False - otherwise


# Timur
# 7. Save dictionary to the file
# - input:  
#     - filename
#     - dictionary of words and counts      
# - output: message if the file is saved or not
def save_dic_to_file(dic, filename):
    print('save_dic_to_file function') 


# Aibek
# 8. Get maximum length word
# - input: dictionary - aynimalyga at beru kerek
# - output: maximum length word   
def find_longest_word(dict1): 
    print('find_longest_word function') 


# Test all functions here
if __name__ == "__main__":
   print("Testing module ...")
   
   content = data_loader('brown_short.txt')
   dict1 = get_word_counts(content)
   print()  # dictionary uzyndygyn wigaru kerek
   print(count_average(dict1))

  
