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

user_credentials = []

# defining the function for the test
def trial_test():
        # defining function for results of test
        def check_result():
                result.delete(0, 'end')
        	if entry.get("1.0", 'end-1c') == lines[line]:
        		end = timer()
                        word_count = len(entry.get("1.0", 'end-1c'))
                        wpm = (int)((word_count/5)/((end-start)/60))
                        current_idx = len(user_credentials) - 1
                        if user_credentials[current_idx][1] < wpm:
                            user = user_credentials[current_idx]
                            user[1] = wpm
                            user_credentials.pop(current_idx)
                            user_credentials.insert(current_idx, user)
                        result.insert(0, wpm)
        	elif entry.get("1.0", 'end-1c') == "":
                        result.insert(0, "")
                else:
                        result.insert(0, "Wrong Input")
        def try_again():
            windows.destroy()
            trial_test()
        
	# Give random words for testing the speed of user
        line = random.randint(0, (len(lines)-1)) 

	# start timer using timeit function
	start = timer()
	windows = Tk()
	windows.geometry("1000x500")

	# use lable method of tkinter for labling in window
	x2 = Label(windows, text=lines[line], font="times 20")
	x2.place(x=200, y=100)

	# place of labling in window
	x3 = Label(windows, text="Start Typing:", font="times 18 bold")
	x3.place(x=50, y=100)

        entry = Text(windows, font="times 18", height="5", width="50", bg="white", fg="black")
	entry.place(x=200, y=200)
        ### Adjust its placing
        results = Label(windows, text="Result in WPM", font="times 18 bold")
        results.place(x=800, y=100)

        result = Entry(windows)
        result.place(x=800, y=150)

	# buttons to submit output and check results
	b2 = Button(windows, text="Done",
			    command=check_result, width=12, bg='grey')
	b2.place(x=150, y=400)

	b3 = Button(windows, text="Try Again",
        		command=try_again, width=12, bg='grey')
	b3.place(x=430, y=400)

        b4 = Button(windows, text="Close", command=windows.destroy, width=12, bg='grey')
        b4.place(x=700, y=400)


def actual_test():
        # defining function for results of test
        def check_result():
                result.delete(0, 'end')
        	if entry.get("1.0", 'end-1c') == paragraphs[paragraph]:
        		end = timer()
                        word_count = len(entry.get("1.0", 'end-1c'))
                        wpm = (int)((word_count/5)/((end-start)/60))
                        current_idx = len(user_credentials) - 1
                        if user_credentials[current_idx][1] < wpm:
                            user = user_credentials[current_idx]
                            user[1] = wpm
                            user_credentials.pop(current_idx)
                            user_credentials.insert(current_idx, user)
                        result.insert(0, wpm)
        	elif entry.get("1.0", 'end-1c') == "":
                        result.insert(0, "")
                else:
                        result.insert(0, "Wrong Input")

        def try_again():
            windows.destroy()
            actual_test()

	# Give random words for testing the speed of user
        paragraph = random.randint(0, (len(paragraphs)-1)) 

	# start timer using timeit function
	start = timer()
	windows = Tk()
	windows.geometry("1000x500")

	# use lable method of tkinter for labling in window
	x2 = Label(windows, text=paragraphs[paragraph], font="times 18", wraplength=700)
	x2.place(x=200, y=100)

	# place of labling in window
	x3 = Label(windows, text="Start Typing:", font="times 18 bold")
	x3.place(x=50, y=20)

        entry = Text(windows, font="times 18", height="5", width="55", bg="white", fg="black")
	entry.place(x=200, y=300)

        results = Label(windows, text="Results in WPM", font="times 18 bold")
        results.place(x=800, y=20)

        result = Entry(windows)
        result.place(x=800, y=50)

	# buttons to submit output and check results
	b2 = Button(windows, text="Done",
		    command=check_result, width=12, bg='grey')
	b2.place(x=150, y=450)

	b3 = Button(windows, text="Try Again",
        		command=try_again, width=12, bg='grey')
	b3.place(x=430, y=450)

        b4 = Button(windows, text="Close", command=windows.destroy, width=12, bg='grey')
        b4.place(x=700, y=450)

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
            user = [user_name.get(), 0]
            user_credentials.append(user)
        else:
            invalid_input = Tk()
            invalid_input.geometry("500x300")
            x1 = Label(invalid_input, text="Invalid login credentials", font=("Arial",20))
            x1.place(x=120, y=100)
            b1 = Button(invalid_input, text="OK", width=15, command=invalid_input.destroy, bg='grey')
            b1.place(x=180, y=200)
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

def display_record():
        display_record = Tk()     
        display_record.geometry("1000x500")
        total_rows = len(user_credentials)
        if total_rows == 0:
            # display no data available
            no_record = Tk()
            no_record.geometry("500x300")
            x1 = Label(no_record, text="No record available", font=("Arial",20))
            x1.place(x=140, y=100)
            b1 = Button(no_record, text="OK", width=15, command=no_record.destroy, bg='grey')
            b1.place(x=180, y=200)
            display_record.destroy()
            return
        total_columns = len(user_credentials[0])
        for i in range(total_rows):
            for j in range(total_columns): 
                e = Entry(display_record, width=20, fg='black',
                        font=('Arial', 16, 'bold'))
                e.place(x=(j+1)*150, y=(i+1)*50)
                e.insert(0, user_credentials[i][j])
        x1 = Label(display_record, text="High Scores", font=("Arial",30))
        x1.place(x=600, y=200)
        b2 = Button(display_record, text="Close", width=15, command=display_record.destroy, bg='grey')
        b2.place(x=400, y=400)
 
def admin_login():
    def check_credentials():
        if (admin_name.get(), admin_password.get()) in admin_database.items():
            display_record()
        else:
            invalid_input = Tk()
            invalid_input.geometry("500x300")
            x1 = Label(invalid_input, text="Invalid login credentials", font=("Arial",20))
            x1.place(x=120, y=100)
            b1 = Button(invalid_input, text="OK", width=15, command=invalid_input.destroy, bg='grey')
            b1.place(x=180, y=200)
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
    
    b3 = Button(screen, text="Admin Login", command=admin_login, width=12, bg='grey')
    b3.place(x=200, y=200)

    b4 = Button(screen, text="User Login", command=user_login, width=12, bg='grey')
    b4.place(x=200, y=350)

# calling window

init(window)
window.mainloop()
