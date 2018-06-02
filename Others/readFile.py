# Reading the contents of a file 

# dictionary Containing words
Unique = {'index': 'value'}

with open('test.txt', 'r') as test:
   for line in test.readlines():# reads the line in file 
        # print(line)
        # convert line to lower case 
        # strips all \n * . characters
        # separates the line into words 
        words = line.lower().strip('\n.').split(" ") 
        for word in words:
            # The if...else checks wehether the word exists already 
            if word in Unique:
                Unique[word] += 1
            else:
                Unique[word] = 1

print('*'*20 + '\nThe Word Frequency\n' + '*'*20)
print(Unique)