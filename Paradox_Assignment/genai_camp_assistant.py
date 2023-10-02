import openai

# =======================
# Initialize the OpenAI API
# =======================
openai.api_key = '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'

# =======================
# Fetching Camp Details using Chat Model
# =======================
def get_camp_details():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Describe a fictional GenAI Summer Camp, detailing its offerings, values, policies, location, dates, pricing, and age range."}
        ]
    )
    return response.choices[0].message['content']

camp_details = get_camp_details()

# =======================
# Router Prompt
# =======================
def router_prompt(parent_input):
    if "sign" in parent_input.lower() or "apply" in parent_input.lower() or "register" in parent_input.lower():
        return "sign_up"
    else: 
        return "question"

# =======================
# Answer Questions using Chat Model
# =======================
def answer_question(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Based on the following details about GenAI Summer Camp, answer the question:\n\n{camp_details}\n\nQuestion: {question}"}
        ]
    )
    return response.choices[0].message['content']

# =======================
# Application Prompt
# =======================
parents_data = []

def application_prompt():
    parent = {}
    parent['name'] = input("Please provide your full name: ")
    parent['phone_number'] = input("Your phone number: ")
    parent['email'] = input("Your email: ")
    kid_age = int(input("Your kid's age: "))
    
    if 10 <= kid_age <= 15:
        parents_data.append(parent)
        return f"Thank you, {parent['name']}. We have received the details. We'll send an email to {parent['email']} with further instructions."
    else:
        return f"I'm sorry, {parent['name']}. The age range for our camp is 10-15 years old. Unfortunately, we cannot accept your kid's application."

# =======================
# Main Function
# =======================
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
