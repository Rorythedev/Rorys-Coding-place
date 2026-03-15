import openai

class Chatbot:
    def __init__(self):
        openai.api_key = 'your-api-key'

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        return response['choices'][0]['message']['content']

if __name__ == '__main__':
    bot = Chatbot()
    while True:
        user_input = input('You: ')
        if user_input.lower() in ['exit', 'quit']:
            break
        response = bot.get_response(user_input)
        print('Bot:', response)