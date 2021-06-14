# importing all libraries
from tkinter import *
from timeit import default_timer as timer
import random
from paragraph import *
from login import *

# creating window using gui
window = Tk()

# the size of the window is defined
window.geometry("1000x500")

window_count = 0
windows_count = 0
user_credentials = []

# defining the function for the test
def trial_test():
	global window_count
        global windows_count
        print("window value "+str(window_count))
        print("windows value "+str(windows_count))

	# loop for destroying the window
	# after on test
	#if window_count == 0:
	#	window.destroy()
	#        window_count = window_count + 1

        # defining function for results of test
        def check_result():
                result.delete(0, 'end')
        	if entry.get() == lines[line]:
        		end = timer()
                        word_count = len(entry.get())
                        #result.insert(0, round(end-start,2))
                        #wpm = (word_count/5)/(((int)(end-start))/60.0)
                        wpm = (int)((word_count/5)/((end-start)/60))
                        current_idx = len(user_credentials) - 1
                        if user_credentials[current_idx] < wpm:
                            user_credentials.pop(current_idx)
                            user_credentials.insert(current_idx, wpm)
                        result.insert(0, wpm)
        	elif entry.get() == "":
                        result.insert(0, "")
                else:
                        result.insert(0, "Wrong Input")

	# Give random words for testing the speed of user
        line = random.randint(0, (len(lines)-1)) 

	# start timer using timeit function
	start = timer()
	windows = Tk()
	windows.geometry("1000x500")
        windows_count = windows_count + 1

	# use lable method of tkinter for labling in window
	x2 = Label(windows, text=lines[line], font="times 20")
	x2.place(x=100, y=10)

	# place of labling in window
	x3 = Label(windows, text="Start Typing", font="times 20")
	x3.place(x=10, y=50)

	entry = Entry(windows, width = 100)
	entry.place(x=280, y=55)

        results = Label(windows, text="Time taken", font="times 20")
        results.place(x=600, y=170)

        result = Entry(windows)
        result.place(x=600, y=200)

        b4 = Button(windows, text="Close", command=windows.destroy, width=12, bg='grey')
        b4.place(x=500, y=100)

	# buttons to submit output and check results
	b2 = Button(windows, text="Done",
			    command=check_result, width=12, bg='grey')
	b2.place(x=150, y=100)

	#b3 = Button(windows, text="Try Again",
        #		command=windows.destroy, width=12, bg='grey')
	#b3.place(x=300, y=100)
	#windows.mainloop()

def actual_test():
	global window_count
        global windows_count
        print("window value "+str(window_count))
        print("windows value "+str(windows_count))

	# loop for destroying the window
	# after on test
	#if window_count == 0:
	#	window.destroy()
	#        window_count = window_count + 1

        # defining function for results of test
        def check_result():
                result.delete(0, 'end')
                print("output here "+str(entry.get())+" actual one "+str(paragraphs[paragraph]))
        	if entry.get() == paragraphs[paragraph]:
        		end = timer()
                        #result.insert(0, round(end-start,2))
                        word_count = len(entry.get())
                        wpm = (int)((word_count/5)/((end-start)/60))
                        current_idx = len(user_credentials)
                        user_credentials.insert(current_idx+1, wpm)
                        result.insert(0, wpm)
        	elif entry.get() == "":
                        result.insert(0, "")
                else:
                        result.insert(0, "Wrong Input")

	# Give random words for testing the speed of user
        paragraph = random.randint(0, (len(paragraphs)-1)) 

	# start timer using timeit function
	start = timer()
	windows = Tk()
	windows.geometry("1000x500")
        windows_count = windows_count + 1

	# use lable method of tkinter for labling in window
	x2 = Label(windows, text=paragraphs[paragraph], font="times 20")
	x2.place(x=100, y=10)

	# place of labling in window
	x3 = Label(windows, text="Start Typing", font="times 20")
	x3.place(x=10, y=50)

	entry = Entry(windows, width = 100)
	entry.place(x=280, y=55)

        results = Label(windows, text="Time taken", font="times 20")
        results.place(x=600, y=170)

        result = Entry(windows)
        result.place(x=600, y=200)


	# buttons to submit output and check results
	b2 = Button(windows, text="Done",
		    command=check_result, width=12, bg='grey')
	b2.place(x=150, y=100)

	#b3 = Button(windows, text="Try Again",
        #		command=windows.destroy, width=12, bg='grey')
	#b3.place(x=300, y=100)


        #close(windows)
        b4 = Button(windows, text="Close", command=windows.destroy, width=12, bg='grey')
        b4.place(x=500, y=100)

def test_option():
    test_window = Tk()
    test_window.geometry("1000x500")

    x1 = Label(test_window, text="Choose test", font="times 20")
    x1.place(x=10, y=50)

    b1 = Button(test_window, text="Trial test", command=trial_test, width=12, bg='grey')
    b1.place(x=200, y=200)

    b2 = Button(test_window, text="Actual test", command=actual_test, width=12, bg='grey')
    b2.place(x=200, y=400)

    b3 = Button(test_window, text="Close", command=test_window.destroy, width=12, bg='grey')
    b3.place(x=600, y=200)

def user_login():
    def check_credentials():
        if (user_name.get(), user_password.get()) in user_database.items():
            test_option()
            user_credentials.append(user_name.get())
            user_credentials.append(0)
        else:
            user_login.destroy()
    user_login = Tk()
    user_login.geometry("1000x500")
    x1 = Label(user_login, text="Enter user name", font="times 20")
    x1.place(x=10, y=50)
    user_name = Entry(user_login, width = 50)
    user_name.place(x=10, y=100)
    
    x2 = Label(user_login, text="Enter user password", font="times 20")
    x2.place(x=10, y=150)
    user_password = Entry(user_login, width = 50)
    user_password.place(x=10, y=200)

    b1 = Button(user_login, text="Login", command=check_credentials, width=12, bg='grey')
    b1.place(x=10, y=300)

    b2 = Button(user_login, text="Close", command=user_login.destroy, width=12, bg='grey')
    b2.place(x=600, y=300)

    
def admin_login():
    def check_credentials():
        if (admin_name.get(), admin_password.get()) in admin_database.items():
            print("Admin login successful")
            print(user_credentials)
            # print user heighest data
        else:
            admin_login.destroy()
    admin_login = Tk()
    admin_login.geometry("1000x500")
    x1 = Label(admin_login, text="Enter Admin name", font="times 20")
    x1.place(x=10, y=50)
    admin_name = Entry(admin_login, width = 50)
    admin_name.place(x=10, y=100)
    
    x2 = Label(admin_login, text="Enter admin password", font="times 20")
    x2.place(x=10, y=150)

    admin_password = Entry(admin_login, width = 50)
    admin_password.place(x=10, y=200)

    b1 = Button(admin_login, text="Login", command=check_credentials, width=12, bg='grey')
    b1.place(x=10, y=300)

    b2 = Button(admin_login, text="Close", command=admin_login.destroy, width=12, bg='grey')
    b2.place(x=600, y=300)

def init(screen):
    screen.geometry("1000x500")

    x1 = Label(screen, text="Welcome", font="times 30")
    x1.place(x=400, y=50)

    x2 = Label(screen, text="Login as Admin", font="times 20")
    x2.place(x=200, y=150)

    x3 = Label(screen, text="Login as User", font="times 20")
    x3.place(x=200, y=300)

    b1 = Button(screen, text="Close", command=screen.destroy, width=12, bg='grey')
    b1.place(x=600, y=200)
    
    #b2 = Button(screen, text="Start", command=test_option, width=12, bg='grey')
    #b2.place(x=250, y=200)

    b3 = Button(screen, text="Admin Login", command=admin_login, width=12, bg='grey')
    b3.place(x=200, y=200)

    b4 = Button(screen, text="User Login", command=user_login, width=12, bg='grey')
    b4.place(x=200, y=350)

def close(screen):
    b1 = Button(screen, text="Close", command=screen.destroy, width=12, bg='grey')
    b1.place(x=500, y=100)
    print("close function called")

# calling window

init(window)
window.mainloop()
