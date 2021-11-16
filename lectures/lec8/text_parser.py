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
    pass 

# Damir
# 2. Get the number of words
# - input:  dictionary of words and counts
# - output: the number of words
def get_number_word(dict1):
    pass


# Erkebulan
# 3. Get the sum of counts of all words
# - input:  mydict - dictionary of words and counts - { word: count }
# - output: sum of all counts in dictionary
def get_sum_counts(mydict):
    pass

# Aiya
# 4. Get the average count of words
# - input:  dictionary of words and counts
# - output: average count of words
def count_average(dict1):
    pass

# Sultan
# 5. Get the word's count function
# - input: 
#     - word to query
#     - dictionary of words and counts
# - output: word count
def get_count(query, dict1):   
    pass
 
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
    pass


# Aibek
# 8. Get maximum length word
# - input: dictionary - aynimalyga at beru kerek
# - output: maximum length word   
def find_longest_word(dict1): 
    pass 


# Test all functions here
if __name__ == "__main__":
   print("Testing module ...")
   
   content = data_loader('brown_short.txt')
   print(len(content))
