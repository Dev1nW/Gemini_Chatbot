from tkinter import *
import google.generativeai as genai
from random import random, randrange

# Create GUI 
root = Tk()
max_height = 600
max_width = 800
root.geometry('800x600')
root.maxsize(800, 600)

# Create class using Gemini API
class Gemini():
    def __init__(self):
        # Create API call
        file = open("GOOGLE_API_KEY.txt", "r")
        api_key = file.read()

        genai.configure(api_key=api_key)

        # Init to least random
        self.temperature = 0
        self.top_p = 0
        self.top_k = 1

        print('Initializing Parameters...')
        print('Initial temp: ', self.temperature)
        print('Initial TopP: ', self.top_p)
        print('Initial TopK: ', self.top_k)
        
        generation_config = genai.GenerationConfig(
            temperature = self.temperature,
            top_p = self.top_p,
            top_k = self.top_k
        )

        # Create model and history
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest', generation_config=generation_config)
        self.chat = self.model.start_chat(history=[])

    # Send message to Gemini from GUI
    def submit_message(self, event=None):
        # Get the text from GUI
        current_text = e.get()
        e.delete(0, END)

        # Send prompt to Gemini        
        response = self.chat.send_message(current_text)

        # Show Users prompt 
        myLabel = Label(frame, text=current_text, wraplength=780)
        myLabel.pack()

        # Then show response from Gemini API
        Gemini_output = 'Gemini: ' + response.text
        myLabel = Label(frame, text=Gemini_output, wraplength=780)
        myLabel.pack()
        
        # Update the scrollregion of the canvas
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Close the GUI and save history
    def End(self, event=None):
        # Save history 
        with open('Gemini_history_output.txt', 'a') as file:
            for message in self.chat.history:
                file.write((f'**{message.role}**: {message.parts[0].text}\n'))

        print('\nSaving the chat history')
        # End GUI
        root.destroy()
        

    # Reset chat and change temp
    def change_temp(self, event=None):
        print('\nrandomly changing temperature and reseting chat')
        
        file = open("GOOGLE_API_KEY.txt", "r")
        api_key = file.read()

        genai.configure(api_key=api_key)
        self.temperature = random()

        generation_config = genai.GenerationConfig(
            temperature = self.temperature,
            top_p = self.top_p,
            top_k = self.top_k
        )

        self.model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)
        self.chat = self.model.start_chat(history=[])

        # Destroy the existing frame and all its children
        global frame
        frame.destroy()
        
        # Create a new frame and add it to the canvas
        frame = Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        
        # Bind the configure event of the frame to the update function
        frame.bind("<Configure>", on_frame_configure)
        
        # Update the scrollregion of the canvas
        canvas.configure(scrollregion=canvas.bbox("all"))

        temp = 'New temp: ' + str(self.temperature)
        myLabel = Label(frame, text=temp, wraplength=780)
        myLabel.pack()

        print('New temp: ', self.temperature)

    # Reset chat and change TopK
    def change_k(self, event=None):
        print('\nrandomly changing TopK and reseting chat')

        file = open("GOOGLE_API_KEY.txt", "r")
        api_key = file.read()

        genai.configure(api_key=api_key)
        self.top_k = randrange(40)+1

        generation_config = genai.GenerationConfig(
            temperature = self.temperature,
            top_p = self.top_p,
            top_k = self.top_k
        )

        self.model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)
        self.chat = self.model.start_chat(history=[])

        # Destroy the existing frame and all its children
        global frame
        frame.destroy()
        
        # Create a new frame and add it to the canvas
        frame = Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        
        # Bind the configure event of the frame to the update function
        frame.bind("<Configure>", on_frame_configure)
        
        # Update the scrollregion of the canvas
        canvas.configure(scrollregion=canvas.bbox("all"))

        topk = 'New TopK: ' + str(self.top_k)
        myLabel = Label(frame, text=topk, wraplength=780)
        myLabel.pack()

        print('New TopK: ', self.top_k)

    # Reset chat and change TopP
    def change_p(self, event=None):
        print('\nrandomly changing TopP and reseting chat')

        file = open("GOOGLE_API_KEY.txt", "r")
        api_key = file.read()

        genai.configure(api_key=api_key)

        self.top_p = random()

        generation_config = genai.GenerationConfig(
            temperature = self.temperature,
            top_p = self.top_p,
            top_k = self.top_k
        )

        self.model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)
        self.chat = self.model.start_chat(history=[])

        # Destroy the existing frame
        global frame
        frame.destroy()
        
        # Create a new frame and add it to the canvas
        frame = Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        
        # Bind the configure event of the frame to the update function
        frame.bind("<Configure>", on_frame_configure)
        
        # Update the scrollregion of the canvas
        canvas.configure(scrollregion=canvas.bbox("all"))

        topp = 'New TopP: ' + str(self.top_p)
        myLabel = Label(frame, text=topp, wraplength=780)
        myLabel.pack()

        print('New TopP: ', self.top_p)
    
    # # Reset chat and make Gemini more random 
    def max_rand(self):

        file = open("GOOGLE_API_KEY.txt", "r")
        api_key = file.read()

        genai.configure(api_key=api_key)

        self.temperature = 1
        self.top_p = 1
        self.top_k = 40

        generation_config = genai.GenerationConfig(
            temperature = self.temperature,
            top_p = self.top_p,
            top_k = self.top_k
        )

        self.model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)
        self.chat = self.model.start_chat(history=[])

        # Destroy the existing frame
        global frame
        frame.destroy()
        
        # Create a new frame and add it to the canvas
        frame = Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        
        # Bind the configure event of the frame to the update function
        frame.bind("<Configure>", on_frame_configure)
        
        # Update the scrollregion of the canvas
        canvas.configure(scrollregion=canvas.bbox("all"))

        max_random = 'Max Random'
        myLabel = Label(frame, text=max_random, wraplength=780)
        myLabel.pack()

# Instantiate the Gemini API
gemini_api = Gemini()

# Creates an Entry where prompt is given by user
e = Entry(root, width=100)
e.pack()

# Container frame for canvas and scrollbar
container = Frame(root)
container.pack(fill='both', expand=True)

# Scrollable canvas setup
canvas = Canvas(container, height=max_height - 100)
scroll_y = Scrollbar(container, orient="vertical", command=canvas.yview)

# This frame will hold the content
frame = Frame(canvas)
canvas_frame = canvas.create_window((0, 0), window=frame, anchor="nw")

# Function to update the scrollregion
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Bind the configure event of the frame to the update function
frame.bind("<Configure>", on_frame_configure)

# Bind the Enter key to the submit_message function
e.bind('<Return>', gemini_api.submit_message)

# Configure canvas with scrollbar
canvas.configure(yscrollcommand=scroll_y.set)

# Layout canvas and scrollbar in the container
canvas.pack(side='left', fill='both', expand=True)
scroll_y.pack(side='right', fill='y')

# Frame for buttons
button_frame = Frame(root)
button_frame.pack(fill='x', pady=5)

# Place buttons next to each other in the frame
Button(button_frame, text='End', command=gemini_api.End).pack(side=LEFT)
Button(button_frame, text='Change Temp', command=gemini_api.change_temp).pack(side=LEFT)
Button(button_frame, text='Change TopK', command=gemini_api.change_k).pack(side=LEFT)
Button(button_frame, text='Change TopP', command=gemini_api.change_p).pack(side=LEFT)
Button(button_frame, text='Max Random', command=gemini_api.max_rand).pack(side=LEFT)

root.mainloop()
