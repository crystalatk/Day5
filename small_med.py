# Be Santa!

# Write a program that simulates a visit to Santa,

# Ask the user what they want for Christmas (can be any number of items)
# Ask if they've been bad or good this year.
# Based on their response, return the appropriate statement:
# If they've been good, list the presents they'll receive.
# If they've been bad, tell them they can expect a lump of coal.
# Hints

# Start with just a single item and make the script work. Then add more.
# Use input to ask the user what they want, and assign the values to variables.
# Use input to ask if they've been bad or good.
# Use a conditional statement, if ... else, to determine the response.
# Bonus

# Involve Krampus!!
# Add functions!


present_list = []
present_list.append(input("What would you like for Christmas?\n"))


def present_function(list):
    want_present = True
    while want_present == True:
        want_more = input("Would you like to add more gifts? y or n\n")
        if want_more.lower() == "y":
            list.append(input("What else would you like for Christmas?\n"))
        else:
            want_present = False


present_function(present_list)

error = True
while error == True:

    naughty_nice = input("Have you been Naughty or Nice this year?\n")
    naughty_nice = naughty_nice.lower()

    if naughty_nice == "nice":
        print("""\n\nLooks like you deserve some presents! 
              .__.      .==========.
            .(\\//).  .-[ for you! ]
           .(\\()//)./  '=========='
       .----(\)\/(/)----.
       |     ///\\\     |
       |    ///||\\\    |
       |   //`||||`\\   |
       |      ||||      |
       |      ||||      |
       |      ||||      |
       |      ||||      |
       |      ||||      |
       |      ||||      |
       '------====------'
You get:""")
        for idx, present in enumerate(present_list):
            print(f"{idx + 1}: {present}")
        error = False

    elif naughty_nice == "naughty":
        print("""
    No presents for you, Naughty Child!\n  Look out for KRAMPUS!!! 
       .----.      __) `
       | == |     < __=- |
    ___| :: |___   \\ `)/
    \  `----'  /\  (\) (
     \   `.   /( \/ /\\
     |    :   | \  /  \\
     \   _._  /  `"   <_>
      xxx(o)xx
""")

    else:
        print("Not off to a great start! You need to listen to the question!")
