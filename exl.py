#print "Hello World!"
#print "Hello Again"
#print "I like typing this."
#print "This is fun."
#print "Yay! Printing."
#print "I'd much rather you 'not' ."
#print 'I "said" do not touch this.'

#print "I will now count my chickens:"

#print "Hens", 25 + 30 / 6
#print "Roosters", 100 - 25 * 3 % 4

#print "Now I will count the eggs:"

#print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

#print "Is it true that 3 + 2 < 5 - 7?"

#print 3 + 2 < 5 - 7

#print "What is 3 + 2?", 3 + 2
#print "what is 5 - 7?", 5 - 7

#print "Oh, that's why it's False."

#print "How about some more."

#print "Is it greater?", 5 < -2
#print "Is it greater or equal?", 5 >= -2
#print "Is it less or equal?", 5<= -2

#print 7.0 / 4.0
#print 7 / 4


#cars = 100
#space_in_a_car = 4
#drivers = 30
#passengers = 90
#cars_not_driven = cars - drivers
#cars_driven = drivers
#carpool_capacity = cars_driven * space_in_a_car
#average_passengers_per_car = passengers / cars_driven

#Make sure to recall variables in print scripts as they are defined above
#print "There are", cars, "cars available."
#print "There are only", drivers, "drivers available."
#print "There will be", cars_not_driven, "empty cars today."
#print "We can transport", carpool_capacity, "people today."
#print "We have", passengers, "to carpool today."
#print "We need to put about", average_passengers_per_car, "in each car."


# name = 'Jonathan Bingman'
# age = 25 #not a lie
# height = 77.0 #inches
# cm_height = height / 0.39370
# weight = 210.0 #pounds
# eyes = "Blue"
# teeth = "White"
# hair = "Brown"


#print "Let's talk about %s." % name
#print "He's %d inches tall." % height
#print "He's %d pounds heavy." % weight
#print "Actually that is pretty heavy."
#print "He's got %s eyes and %s hair." % (eyes, hair)
#print "His teeth are usually %s depending on the tea." % teeth

#this line is tricky, try to get it exactly right
# print "If I add {}, {}, and {}  I get {}.".format(age, height, weight, age + height + weight)

#print "The height in centimeters of %s is %rcm" % (name, round(cm_height, 2))


#x = "There are %d types of people." % 10
#binary = "binary"
#do_not = "don't"
#y = "Those who know %s and those who %s." % (binary, do_not)

#print x
#print y

#print "I said: %r." % x
#print "I also said: '%s'." % y

#hilarious = False
#joke_evaluation = "Isn't that joke so funny?! %r"

#print joke_evaluation % hilarious

#w = "This is the left side of..."
#e = "a string with a right side."

#print w + e


#print "Mary had a little lamb."
#print "Its fleece was white as %s." % 'snow'
#print "And everywhere that Mary went."
#print "." * 10 #it added a period to the end of the previous sentence 10 times

#end1 = "C"
#end2 = "h"
#end3 = "e"
#end4 = "e"
#end5 = "s"
#end6 = "e"
#end7 = "B"
#end8 = "u"
#end9 = "r"
#end10 = "g"
#end11 = "e"
#end12 = "r"

#comma at the end. try removing it
#removing the comma after the first print triggers a newline
#print end1 + end2 + end3 + end4 + end5 + end6,
#print end7 + end8 + end9 + end10 + end11 + end12
#print end1 * 100

#%r = raw format which seems to add parentheses around concantinated strings, provides literal print out of line including included variable names, formatters, and \n new line commands
#formatter = "%s %s %s %s"

# print formatter % (1, 2, 3, 4)
# print formatter % ('one', 'two', 'three', 'four')
# print formatter % (True, False, False, True)
# print formatter % (formatter, formatter, formatter, formatter)
# print formatter % (
#     "I had this thing.",
#     "That you could type up right.",
#     "But it didn't sing.",
#     "So I said goodnight."
# )


# days = "Mon Tues Wed Thu Fri Sat Sun"
# months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#
# print "Here are the days: ", days
# print "Here are the months: %r" % months
#
# print """
# There's something going on here.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.
# """


# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\ a \\ cat."
#
# fat_cat = '''
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# '''
#
# print tabby_cat
# print persian_cat
# print backslash_cat
# print fat_cat

# while True:
#     for i in ["|", "/", "-", "\\", "|"]:
#         print "%s\r" % i,

# age = int(raw_input("How old are you? "))
# height = raw_input("How tall are you? ")
# weight = raw_input("How much do you weigh? ")
#
# print "So, you're %r old, %s tall and %r heavy." % (age, height, weight)


# from sys import argv
#
# script, user_name = argv
# prompt = '> '
#
# print "Hi %s, I'm the %s script." % (user_name, script)
# print "I'd like to ask you a few questions."
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)
#
# print "where do you live %s?" % user_name
# lives = raw_input(prompt)
#
# print "What kind of computer do you have?"
# computer = raw_input(prompt)
#
# print """
# Alright, so you said %r about liking me.
# You live in %r. Not sure where that is.
# And you have a %r computer. Nice.
# """ % (likes, lives, computer)

# from sys import argv
#
# script, filename = argv
#
# txt = open(filename)
#
# print "Here's your file %r:" % filename
# print txt.read()
# print "Edit the file: "
# txt = open(filename, 'a+')
# txt_new = raw_input("Enter New Text>> ")
#
# txt.write('\n')
# txt.write(txt_new)
#
# print txt.read()

#We import the arg variables from the sys directory and grab preassigned assets "script" and "filename" and during the terminal command "python exl.py(executing file) foo.txt(editing file)".

#We then open the text file for editing, we truncate to clear the file for new content(with permission from the user). You can also a+ modifier (append a file with content already existant) or rw+ modifier to read the file and write(overwrite). Once the file is open and cleared, we get input from the use for new .txt file data. Then we close the file to finalize. According to stack overflow, you may not need to close a file, as that is the default action after a write() in the new python language syntax.


# from sys import argv
# #grab assets from argv module
# script, filename = argv
#
# #get input whether or not to erase (truncate) test textfile
# raw_input("Would you like to erase the file and begin again?\n Press ENTER for YES\n Press CTRL+C for NO")
#
# #open file to be erased, set in variable named "target"
# target = open(filename, 'w')
#
# #erase (truncate) textfile function
# print "Erasing text file, Success!"
# target.truncate()
#
# #grab new content from user for .txt file
# print "Enter new text to place into file!"
# line1 = raw_input("> ")
#
# #write the input from the user (saved in line1 variable) and write it to the file.
# #Inputted text only works in single line, non formatable way via Terminal. Must specifcy new lines via python code program.
# print "Thanks! Check the file, your updates were made!"
# target.write(line1)
#
# #close the .txt file for finalization
# target.close()
#
# #TERMINAL COMMANDS '$ cat (filename.txt) works to simply read file from text
# #while $ echo "This is a test file." > test.txt will create a new text file in the current directory and enter the text "This is a test file." into said .txt file

# from sys import argv
# from os.path import exists
#
# script, from_file, to_file = argv
#
# print "Copying from %s to %s" % (from_file, to_file)
#
# # we could do these two on one line, how?
# indata = open(from_file).read()
#
# print len(indata), exists(to_file), raw_input("copy file?>>")
#
# out_file = open(to_file, 'w').write(indata)


# def print_two(*args):
#     arg1, arg2 = args
#     print "arg1: %r, arg2: %r" % (arg1, arg2)
#
# def print_two_again(arg1, arg2):
#     print "arg1: %r, arg2: %r" % (arg1, arg2)
#
# def print_one(arg1):
#     print "arg1: %r" % arg1
#
# def print_none():
#     print "I got nothin'."
#
# print_two ("Zed", "Shaw")
# print_two_again("Zedagain", "Shawagain")
# print_one("First!")
# print_none()

#defines (creates) a function called cheese_and_crackers and then adds arguments (definable variables) for cheese and cracker numbers
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     #variables defined in functions not global
#     amount_of_cheese = 300
#     amount_of_crackers = 2
#     print amount_of_crackers, amount_of_cheese
#     print "You have %d cheeses!" % cheese_count
#     print "You have %d boxes of crackers!" % boxes_of_crackers
#     print "Man that's enough for a party!"
#     print "Get a blanket. \n"
#
# #runs the function cheese_and_crackers and changes the count and boxes numbers to the ones given in the argument values assigning 20 to cheese_count and 30 to boxes_of_crackers
# print "We can just give the function numbers directly:"
# cheese_and_crackers(20, 30)
#
# #assigns number values to variables and then runs the function cheese_and_crackers with the arguments using the variable names
# print "OR, we can use variables from our script:"
# amount_of_cheese = 10
# amount_of_crackers = 50
#
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
# #simply runs the function cheese_and_crackers and then first does math automatically, and then sets the final solution to arguments
# print "We can even do math inside too:"
# cheese_and_crackers(10 + 20, 5 + 6)
#
# #runs the cheese_and_crackers function and assigns arguments from the previously defined variables and runs the mathematic equations, then displays them as the arguments inside the function
# print "And we can combine the two, variables and math:"
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#
# print "LAST ONE, WE GET INPUT FROM THE USER AND THEN PLACE THOSE NUMBERS INTO THE FUNCTION"
#
# cheese_and_crackers(int(raw_input("How many cheese you want?")), int(raw_input("How many crackers you like?")))

# from sys import argv
# script, input_file = argv
#
# #set 'f' as argument for current_file = input_file
# def print_all(f):
#     print f.read()
#
# def rewind(f):
#     f.seek(0)
#
# def print_a_line(line_count, f):
#     print line_count, f.readline()
#
# current_file = open(input_file)
#
# print "First let's print the whole file: \n"
# print_all(current_file)
#
# print "Now let's rewind, kind of like a tape."
# rewind(current_file)

# print "Let's print three lines:"
#
# current_line = 1
# print_a_line(current_line, current_file)
#
# current_line = current_line + 1
# print_a_line(current_line, current_file)
#
# current_line = current_line + 1
# print_a_line(current_line, current_file)
#
# rewind(current_file)

#####simply previous code into a while loop (using a FOR loop is supposed to be more efficient memory and time wise)
# print "Create a while loop to replace iteration of code\n"
# current_line = 1
# while current_line <= 3:
#     print_a_line(current_line, current_file) ##do not need to print function, will add "none" to the end of each line
#     current_line += 1


# def add(a, b):
#     print "ADDING %d + %d" % (a, b)
#     return a + b
#
# def subtract(a, b):
#     print "SUBTRACTING %d - %d" % (a, b)
#     return a - b
#
# def multiply(a, b):
#     print "MULTIPLYING %d x %d" % (a, b)
#     return a * b
# def divide(a, b):
#     print "DIVIDING %d / %d" % (a, b)
#     return a / b
#
# print "Let's do some math with just functions!"
#
# age = add(30, 5)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide (100, 2)
#
# print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
#
# print "Here is a puzzle."
#
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#
# print "That becomes: ", what, "Can you do it by hand?"
