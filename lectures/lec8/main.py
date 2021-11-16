### Main program 

# Import  modules
import text_parser as tp

print('Entered main program')

# Enter file name to read
fname = input('Enter file name to read: ')
print(fname)

# Read data file
lines = tp.data_loader(fname)
print(len(lines))

# Parse file and create a dictionary
dict1 = tp.get_word_counts(lines)
print(len(dict1))

# Infinite loop for queries
while True:
  tsk = int(input('Select task:'))
  if tsk == 1:
     # 1-shi funct wakyru
     continue
  elif tsk == 2:
     # 2-shi funct wakyru
     continue
  elif tsk == 3:
     # 3-shi funct wakyru
     continue
  elif tsk == 4:
     # 4-shi funct wakyru
     continue
  elif tsk == 5:
     # 5-shi funct wakyru
     continue
  elif tsk == 6:
     # 6-shi funct wakyru
     continue
  elif tsk == 7:
     # 7-shi funct wakyru
     continue
  elif tsk == 8:
     # 8-shi funct wakyru
     continue
  else: 
     # programmadan shygu
     break
   

# Finish the program
print('Thank you for using our program')
