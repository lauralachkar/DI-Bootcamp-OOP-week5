import random

words_list = []
def get_words_from_file():
     f = open('file1.txt')
     data = f.readlines()
     for i in range(len(data)):
         words_list.append(data[i].strip('\n'))
     return words_list
print(get_words_from_file())
def get_random_sentence(length):
     length = int(input("give me a number between 2 and 20: "))
     if (length < 2):
         print("error")
     elif (length > 20):
         print("error")
     else:
         for i in range(length):
             print(random.choice(words_list).lower(), end = ' ')
get_random_sentence(6)














