import g4f  

# Initialize the conversation history
conversation_history = []

# Function to simulate the conversation
def chat_with_ai():
    while True:
        # Get input from the user
        user_input = input("You: ")
        
        # Append the user message to the conversation history
        conversation_history.append({"role": "user", "content": user_input})
        
        # Generate the AI response
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=conversation_history
        )
        
        # Print the AI response
        ai_content = response.get('content')  # Assuming the response has a 'content' field
        print(f"AI: {ai_content}")
        
        # Append the AI message to the conversation history
        conversation_history.append({"role": "ai", "content": ai_content})

# Start the conversation
chat_with_ai()
