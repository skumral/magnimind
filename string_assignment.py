# string assignment

"""
1. Ask the user to enter their first name and surname in lower case. 
Change the case to title case and join them together. Display the finished result.
"""

first_name = input("Enter your first name in lower case: ")
last_name = input("Enter your last name in lower case: ")
print(first_name.capitalize()+last_name.capitalize())


"""
2. Ask the user to type in the first line of a poem Raven by E
dgar Allen Poe and display the length of the string. 
Ask for a starting number and an ending number and then 
display just that section of the text 
(remember Python starts counting from 0 and not 1). 
Here is the poem Raven:

Deep into that darkness peering,
Long I stood there, wondering, fearing,
Doubting, dreaming dreams no mortals
Ever dared to dream before;
But the silence was unbroken,
And the stillness gave no token,
And the only word there spoken
Was the whispered word, "Lenore!"
This I whispered, and an echo
Murmured back the word, "Lenore!"
Merely this, and nothing more.
"""

first_line = input("Type in the first line of poem 'Raven': ")
print(len(first_line))
s_number = int(input("Enter a starting number: "))
e_number = int(input("Enter an ending number: "))
print(first_line[s_number: e_number+1])


"""
3. Removes extra characters from the start and end of a string 
and explain why you need to remove white spaces while exploring text.
"""
# strip function returns a copy of the string with leading and
# trailing whitespace removed.
