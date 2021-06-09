# importing all libraries
from tkinter import *
from timeit import default_timer as timer
import random

# creating window using gui
window = Tk()

# the size of the window is defined
window.geometry("1000x500")

x = 0

# defining the function for the test
def game():
	global x

	# loop for destroying the window
	# after on test
	if x == 0:
		window.destroy()
		x = x+1

	# defining function for results of test
	def check_result():
		if entry.get() == words[word]:

			# here start time is when the window
			# is opened and end time is when
			# window is destroyed
			end = timer()

			# we deduct the start time from end
			# time and calculate results using
			# timeit function
			print(end-start)
		else:
			print("Wrong Input")
                        print(entry.get)

	words = ['programming', 'coding', 'algorithm',
			'systems', 'python', 'software']

	# Give random words for testing the speed of user
	word = random.randint(0, (len(words)-1))

	# start timer using timeit function
	start = timer()
	windows = Tk()
	windows.geometry("1000x500")

	# use lable method of tkinter for labling in window
	x2 = Label(windows, text=words[word], font="times 20")

	# place of labling in window
	x2.place(x=150, y=10)
	x3 = Label(windows, text="Start Typing", font="times 20")
	x3.place(x=10, y=50)

	entry = Entry(windows)
	entry.place(x=280, y=55)

	# buttons to submit output and check results
	b2 = Button(windows, text="Done",
				command=check_result, width=12, bg='grey')
	b2.place(x=150, y=100)

	b3 = Button(windows, text="Try Again",
				command=game, width=12, bg='grey')
	b3.place(x=300, y=100)

        close(windows)

	windows.mainloop()

def init(screen):
    screen.geometry("1000x500")

    x1 = Label(screen, text="Lets start typing test..", font="times 30")
    x1.place(x=50, y=50)

    b1 = Button(screen, text="Close", command=screen.destroy, width=12, bg='grey')
    b1.place(x=500, y=100)
    
    b1 = Button(screen, text="Go", command=game, width=12, bg='grey')
    b1.place(x=150, y=100)


def close(screen):
    b1 = Button(screen, text="Close", command=screen.destroy, width=12, bg='grey')
    b1.place(x=500, y=100)
# calling window

init(window)
window.mainloop()
