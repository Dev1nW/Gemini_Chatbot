import google.generativeai as genai
from random import random, randrange
import gradio as gr

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
        self.model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)
        self.chat = self.model.start_chat(history=[])

        self.demo = gr.Interface(fn=self.submit_message, inputs=["text", "checkbox", "checkbox", "checkbox", "checkbox"], outputs=["text", "text"])

        self.flag = False
        self.seen = [False, False, False]

    # Send message to Gemini from GUI
    def submit_message(self, prompt,  change_temp, change_topp, change_topk, save_and_end_code):
        if change_temp or change_topp or change_topk:
            if self.seen != [change_temp, change_topp, change_topk]:
                file = open("GOOGLE_API_KEY.txt", "r")
                api_key = file.read()

                genai.configure(api_key=api_key)

                if change_temp:
                    self.temperature = random()
                    print('\nChanging Temperature to: ', self.temperature)
                if change_topp:
                    self.top_p = random()
                    print('\nChanging TopP to: ', self.top_p)
                if change_topk:
                    self.top_k = randrange(40)+1
                    print('\nChanging TopK to: ', self.top_k)

                generation_config = genai.GenerationConfig(
                    temperature = self.temperature,
                    top_p = self.top_p,
                    top_k = self.top_k
                )

                self.model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)
                self.chat = self.model.start_chat(history=[])

                self.seen = [change_temp, change_topp, change_topk]
            else:
                pass

        if save_and_end_code and not self.flag:
            history = []
            with open('Gemini_history_output.txt', 'a') as file:
                for message in self.chat.history:
                    file.write((f'**{message.role}**: {message.parts[0].text}\n'))
                    history.append((f'**{message.role}**: {message.parts[0].text}\n'))
            
            print('\nSaving the chat history')  
            self.flag = True

            return "", history
        
        elif not save_and_end_code and self.flag:
            self.flag = False

        response = self.chat.send_message(prompt)

        history = []
        for message in self.chat.history:
                history.append((f'**{message.role}**: {message.parts[0].text}\n'))
        
        return response.text, history


if __name__ == "__main__":
    gemini_chatbot = Gemini()
    gemini_chatbot.demo.launch()