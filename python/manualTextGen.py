from openai import OpenAI

role = "You are an expert programmer making a program that plots a list of points in python."
n = 10

class WordPredictor:
    def __init__(self):
        self.client = OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama',  # required, but unused
        )

    def getResponse(self, text):
        system_message = {"role": "system", "content": role}
        user_message = {"role": "user", "content": text}
        response = self.client.chat.completions.create(
            model="dolphin-phi",
            messages=[system_message, user_message],
            max_tokens=1
        )
        return response.choices[0].message.content

    def get_next_word_probabilities(self, text):
        """system_message = {"role": "system", "content": role}
        user_message = {"role": "user", "content": text}
        response = self.client.chat.completions.create(
            model="dolphin-phi",
            messages=[system_message, user_message],
            logprobs=True, # not implemented but does exactly what i want
            top_logprobs=5,
            max_tokens=1,
            #n=1000
        )"""
        messages = [self.getResponse(text) for i in range(n)]
        probabilities = [(message, messages.count(message)/n) for message in set(messages)]
        probabilities.sort(key=lambda x: x[1], reverse=True)
#        next_word = response.choices[0].message['content']
        return probabilities

# Example usage:
predictor = WordPredictor()
text = "import matplotlib.pyplot as plt\n"
while True:
    next_word = predictor.get_next_word_probabilities(text)
    print(text)
    print(next_word[:5])
    choice = input("1-5 or annother word: ")
    match choice:
        case "1":
            text += next_word[0][0]
        case "2":
            text += next_word[1][0]
        case "3":
            text += next_word[2][0]
        case "4":
            text += next_word[3][0]
        case "5":
            text += next_word[4][0]
        case _:
            text += choice
