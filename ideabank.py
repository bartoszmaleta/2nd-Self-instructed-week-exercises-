# ideabank = open('bank_of_ideas.txt', 'a')
# idea = input('What is your new idea: ')

# ideabank.write(idea)
# ideabank.close()

# ideabank = open('bank_of_ideas.txt', 'r')
# for line in ideabank:
#     print(line)

# print(ideabank.read())

with open("bank_of_ideas.txt", "a") as ideabank:
    idea = input("what is your new idea? ")
    ideabank.write(idea + "\n") 
   

with open("bank_of_ideast.txt", "r") as ideabank:
    for i, line in enumerate(ideabank):
        
        print(f'{format(i+1)} {line.strip()}')
        
        #  print('{} {}'.format(i+1, line.strip()))
        # print (ideabank.read())