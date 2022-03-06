# Import tkinter library for api
import tkinter as tk
import tkinter.scrolledtext as tksc

# Define a test function to test the button
def test_my_button():
    # Raise the authentication frame
    frame_auth.tkraise()

    # Get the user's password they entered and store it in a variable
    usr_password = ent_password.get()

    # Update the authentication frame to display the user's password
    lbl_auth.config(text='Your Password: '+usr_password)


# Create a 600x300 window for the gui
root = tk.Tk()
root.wm_geometry("400x300")

# Set the title
root.title('Authorization')

# Create empty frame with a grid
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky='news')

# Create an authentication frame
frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky='news')

# Create a Username widget
lbl_username = tk.Label(frame_login, text='Username:', font='Courier')
lbl_username.pack()

# Create a Password widget
lbl_password = tk.Label(frame_login, text='Password:', font='Courier')
lbl_password.pack()

# Add a label to the authentication frame
lbl_auth = tk.Label(frame_auth, font='Courier')
lbl_auth.pack()

# Add username input field for the user
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

# Add a password input field for the user
ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(pady=5)

# Add a button that a user can click to enter their details and login
bt_image = tk.PhotoImage(file="button.gif") # Set the button image
bt_image = bt_image.subsample(40,40)
button_login = tk.Button(frame_login, text='Log In', command=test_my_button, image=bt_image)
button_login.pack()

# Bring login frame to the front
frame_login.tkraise()

# Add a scrolling text widget
test_textbox = tksc.ScrolledText(frame_auth)
test_textbox.configure(height=10, width=50, font='Times',background='Blue',foreground='white') # Configure the widget
test_textbox.pack()

# Keep the window persistent
root.mainloop()
