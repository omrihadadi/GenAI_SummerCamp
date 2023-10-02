import openai
import re

min_age = None
max_age = None

# Initialize the OpenAI API
openai.api_key = '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'

# Fetching Camp Details using Chat Model

def get_camp_details():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Describe a fictional GenAI Summer Camp, detailing its offerings, values, policies, location, dates, pricing, min age and max age in numbers."}
        ]
    )
    return response.choices[0].message['content']

camp_details = get_camp_details()

def extract_age_from_response(response_text):
    """Extract age from the OpenAI's response text."""
    age_matches = re.findall(r'(\d+)', response_text)
    if age_matches:
        return int(age_matches[0])
    else:
        raise ValueError("Couldn't extract age from the response.")


def initialize_age_range():
    global min_age, max_age

    # Ask OpenAI for the minimum age
    response_min_age = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "What is the youngest age allowed for the GenAI Summer Camp? Please answer with just a number."}
        ]
    )
    temp_min_age = extract_age_from_response(response_min_age['choices'][0]['message']['content'])

    # Ask OpenAI for the maximum age
    response_max_age = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "What is the oldest age allowed for the GenAI Summer Camp? Please answer with just a number."}
        ]
    )
    temp_max_age = extract_age_from_response(response_max_age['choices'][0]['message']['content'])

    # Ensure the age range is logical
    min_age = min(temp_min_age, temp_max_age)
    max_age = max(temp_min_age, temp_max_age)



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
        parent_data = {}  # This ensures parent_data is always defined

    

# Main Function

def main():
    print("Hello! Welcome to GenAI Summer Camp's assistant. Do you want to ask a question about the camp or sign your kid up?")
    while True: 
        parent_input = input()
        route = router_prompt(parent_input)
        if route == "question":
          parent_question = parent_input
          print(answer_question(parent_question))
        elif route == "sign_up":
          print(application_prompt())
        else:
          print("Sorry, I didn't understand that. Please type your intent clearly.")

if __name__ == "__main__":
    main()
