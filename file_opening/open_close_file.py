
"""
file = open('simple.txt')
print(type(file))

"""


"""
with open('simple.txt', 'r') as reader:
    print(reader)



file = open('dog_breeds.txt', 'rb')
type(file)

file = open('dog_breeds.txt', 'wb')
type(file)

with open('simple.txt', 'r') as reader:
    print(reader.read())

with open('simple.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')"""
'''
f = open("simple.txt", 'a')
f.write("Now the file has more content")'''

f = open("simple.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f= open("simple.txt", 'r')
print(f.read())