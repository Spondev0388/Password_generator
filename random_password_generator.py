import random
password_length = int(input("Enter the length of your desired password"))
password_divide = int(password_length/2)
possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
possible_signs = "~@!#$%^&*()-_+={[}]\|;:,><?/"
random_character_list = [random.choice(possible_characters) + random.choice(possible_signs) for n in range(password_divide)]
odd_number_issue_resolved = "("
rand_password = "".join(random_character_list)
if int(password_length)% 2 == 1:
    print(str(rand_password + odd_number_issue_resolved))
else:
    print(rand_password)

#I was not willing to add comments still I am adding(for telling my experience and some mistakes)(and also to gain marks) (lol)
#The only problem which made me stuck in this program was the odd number issue(You might have also noticed it if you remove the odd_number_issue_resolved function don't mess with that
#But now its all fine
#I hope you will like it :)






