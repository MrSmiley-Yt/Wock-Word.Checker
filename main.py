#import stuff
import tkinter as tk
import webbrowser

#Define Conditions
def clear_label():
    result_label.config(text="")

def describe_text(event=None):
    user_input = entry.get()
    if user_input:
        description = "Description fetched for the text: " + user_input
        result_label.config(text=description)
        search_url = f"https://www.google.com/search?q={user_input} meaning"
        webbrowser.open(search_url)
        entry.delete(0, tk.END)  # Clear the entry widget after fetching the description
        root.after(5000, clear_label)

def synonyms_text(event=None):
    user_input = entry.get()
    if user_input:
        description = "Synonyms fetched for the text: " + user_input
        result_label.config(text=description)
        search_url = f"https://www.google.com/search?q={user_input} synonyms"
        webbrowser.open(search_url)
        entry.delete(0, tk.END)  # Clear the entry widget after fetching the description
        root.after(5000, clear_label)
    else:
        result_label.config(text="Please enter text")
        root.after(2000, clear_label)

def antonyms_text(event=None):
    user_input = entry.get()
    if user_input:
        description = "Antonyms fetched for the text: " + user_input
        result_label.config(text=description)
        search_url = f"https://www.google.com/search?q={user_input} antonyms"
        webbrowser.open(search_url)
        entry.delete(0, tk.END)  # Clear the entry widget after fetching the description
        root.after(5000, clear_label)
    else:
        result_label.config(text="Please enter text")
        root.after(2000, clear_label)

def rhymes_text(event=None):
    user_input = entry.get()
    if user_input:
        description = "Rhymes fetched for the text: " + user_input
        result_label.config(text=description)
        search_url = f"https://www.google.com/search?q={user_input} rhymes"
        webbrowser.open(search_url)
        entry.delete(0, tk.END)  # Clear the entry widget after fetching the description
        root.after(5000, clear_label)
    else:
        result_label.config(text="Please enter text")
        root.after(2000, clear_label)

def youtube_text(event=None):
    user_input = entry.get()
    if user_input:
        description = "Videos fetched for the text: " + user_input
        result_label.config(text=description)
        search_url = f"https://www.youtube.com/results?search_query={user_input}"
        webbrowser.open(search_url)
        entry.delete(0, tk.END)  # Clear the entry widget after fetching the description
        root.after(5000, clear_label)
    else:
        result_label.config(text="Please enter text")
        root.after(2000, clear_label)

def photos_text(event=None):
    user_input = entry.get()
    if user_input:
        description = "Photos fetched for the text: " + user_input
        result_label.config(text=description)
        search_url = f"https://www.istockphoto.com/es/search/2/image?family=creative&phrase={user_input}"
        webbrowser.open(search_url)
        entry.delete(0, tk.END)  # Clear the entry widget after fetching the description
        root.after(5000, clear_label)
    else:
        result_label.config(text="Please enter text")
        root.after(2000, clear_label)

def Scratch_text(event=None):
    user_input = entry.get()
    if user_input:
        description = "Photos fetched for the text: " + user_input
        result_label.config(text=description)
        search_url = f"https://scratch.mit.edu/search/projects?q={user_input}"
        webbrowser.open(search_url)
        entry.delete(0, tk.END)  # Clear the entry widget after fetching the description
        root.after(5000, clear_label)
    else:
        result_label.config(text="Please enter text")
        root.after(2000, clear_label)

root = tk.Tk()
root.title("Wock")
root.geometry("600x500")
root.configure(bg='Black')

entry = tk.Entry(root, font=('Arial', 50), width=10, justify="center")
entry.pack(pady=20)
entry.bind("<Return>", describe_text)
entry.bind("<Return>", synonyms_text)
entry.bind("<Return>", antonyms_text)
entry.bind("<Return>", rhymes_text)
entry.bind("<Return>", Scratch_text)

button = tk.Button(root, text="Definition/s", command=describe_text)
button.pack()
button = tk.Button(root, text="Synonym/s", command=synonyms_text)
button.pack()
button = tk.Button(root, text="Antonym/s", command=antonyms_text)
button.pack()
button = tk.Button(root, text="Rhyme/s", command=rhymes_text)
button.pack()
button = tk.Button(root, text="Video/s", command=youtube_text)
button.pack()
button = tk.Button(root, text="Photo/s", command=photos_text)
button.pack()
button = tk.Button(root, text="Scratch Game/s", command=Scratch_text)
button.pack()

result_label = tk.Label(root, text="No descriptions fetched!", font=('Arial', 12), wraplength=380)
result_label.pack(pady=20)

root.mainloop()

