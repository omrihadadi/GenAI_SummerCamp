import openai

min_age = None
max_age = None

# Initialize the OpenAI API
openai.api_key = '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'

# Fetching Camp Details using Chat Model

def get_camp_details():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Describe a fictional GenAI Summer Camp, detailing its offerings, values, policies, location, dates, pricing, and age range."}
        ]
    )
    return response.choices[0].message['content']

camp_details = get_camp_details()

def initialize_age_range():
    global min_age, max_age

    # Ask OpenAI for the minimum age
    response_min_age = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "What's the minimum age for the GenAI Summer Camp?"}
        ]
    )
    min_age = int(response_min_age['choices'][0]['message']['content'])

    # Ask OpenAI for the maximum age
    response_max_age = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "What's the maximum age for the GenAI Summer Camp?"}
        ]
    )
    max_age = int(response_max_age['choices'][0]['message']['content'])

# Router Prompt

def router_prompt(parent_input):
    if "sign" in parent_input.lower() or "apply" in parent_input.lower() or "register" in parent_input.lower():
        return "sign_up"
    else: 
        return "question"

# Answer Questions using Chat Model

def answer_question(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Based on the following details about GenAI Summer Camp, answer the question:\n\n{camp_details}\n\nQuestion: {question}"}
        ]
    )
    return response.choices[0].message['content']

# Application Prompt

parents_data = []

def application_prompt():
    global min_age, max_age

    # If age range hasn't been initialized yet, do so
    if min_age is None or max_age is None:
        initialize_age_range()

    parent_name = input("Please enter your full name: ")
    phone_number = input("Please enter your phone number: ")
    email = input("Please enter your email: ")
    kid_age = int(input("Please enter your kid's age: "))

    # Check if kid's age is within the range
    if min_age <= kid_age <= max_age:
        parent_data = {
            "parent_name": parent_name,
            "phone_number": phone_number,
            "email": email,
            "kid_age": kid_age
        }
        print("Application successfully received! We'll be in touch.")
    else:
        print(f"Sorry, this camp is for kids aged between {min_age} and {max_age}.")

    return parent_data

# Main Function

def main():
    print("Hello! Welcome to GenAI Summer Camp's assistant. Do you want to ask a question about the camp or sign your kid up?")
    parent_input = input()

    route = router_prompt(parent_input)
    if route == "question":
        parent_question = input("Please ask your question: ")
        print(answer_question(parent_question))
    elif route == "sign_up":
        print(application_prompt())
    else:
        print("Sorry, I didn't understand that. Please type your intent clearly.")

if __name__ == "__main__":
    main()
