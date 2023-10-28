import random

# Define a dictionary of responses for the chatbot
responses = {
    "hello": ["Hello! How can I help you today?", "Hi there!", "Greetings!"],
    "how are you": ["I'm just a computer program, but I'm functioning well.", "I'm doing fine, thanks for asking!"],
    "good morning": ["Good morning!", "Morning! How can I assist you today?", "Top of the morning to you!"],
    "good afternoon": ["Good afternoon!", "Had your lunch?", "Working?? Have a break, Have a chocolate"],
    "good evening": ["Good evening!", "Hope you had your evening Chai!"],
    "good night": ["Good Night!", "Have a great Sleep"],
    "motivation": [
        "Here's a motivational quote for you: 'The only way to do great work is to love what you do.' - Steve Jobs",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any "
        "obstacle.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    ],
    "bye": ["Goodbye! Have a great day.", "See you later!", "Farewell!"],
    "calculate": [],  # We'll add responses for calculations dynamically.
    "default": ["I'm not sure I understand. Can you please rephrase your question.",
                "Could you provide more information?"]
}


# Function to generate a response
def get_response(input_text):
    input_text = input_text.lower()
    if input_text.startswith("calculate "):
        try:
            result = eval(input_text[len("calculate "):])  # Evaluate the expression
            return f"The result is: {result}"
        except Exception as e:
            return "Sorry, I couldn't calculate that. Please check your input."

    response = responses.get(input_text, responses["default"])
    return random.choice(response)


# Main chat loop
print("~~Welcome to my AI Chat Bot.~~~~ \n  Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    else:
        response = get_response(user_input)
        print("Chatbot:", response)
