# GenAI_SummerCamp

### Overview:
The GenAI Summer Camp Assistant is a Python-based conversational agent that fetches details about a fictional GenAI Summer Camp, responds to parents' queries about the camp, and collects application details if a parent wishes to sign up their child.

### Code Organization:

1. **Initialization of the OpenAI API**:
    - The script begins by setting up the OpenAI API using the provided API key.

2. **Fetching Camp Details**:
    - **First Chunk**: The assistant requests the first portion of details about the camp.
    - **Continuation**: If more details are needed, the assistant uses a continuation prompt to request further information, appending the subsequent chunks to the initial details.

3. **Router Prompt**:
    - Based on user input, this function determines if the parent wants to ask a question or sign up their child. The decision is made based on keywords present in the user's input.

4. **Answer Questions**:
    - If the decision from the router prompt is to answer a question, this function uses the stored camp details to generate a relevant answer.

5. **Application Prompt**:
    - If the decision from the router prompt is to sign up, this function gathers essential details such as parent's name, phone number, email, and the child's age. 
    - It checks if the child's age falls within the specified range (10 to 15 years). If yes, the parent's details are stored in a global `parents_data` list. If not, a message informs the parent that the age is outside the camp's age range.

6. **Main Function**:
    - The main function orchestrates the user interaction, routing the conversation based on the parent's intent.

### Data Structures:

- **parents_data**: A global list that stores parent information. Each entry in the list is a dictionary containing:
    - `name`: Parent's full name.
    - `phone_number`: Parent's contact number.
    - `email`: Parent's email address.

### Workflow:

1. The script starts with a greeting and asks if the parent wants to query about the camp or sign up their child.
2. The `router_prompt` function determines the intent.
3. Based on the intent:
    - The script answers questions using the fetched camp details.
    - Or, it collects application details. If the child's age is within range, details are stored; otherwise, a message is displayed.
4. The interaction concludes, but the script can be easily rerun for additional queries or sign-ups.

### Pre-requisites:
 Python: Ensure you have Python installed.
   
### Steps to Run the Solution:

1. Save the code provided earlier into a file, named it genai_camp_assistant.py.
2. Open a terminal or command prompt.
3. Navigate to the directory where you saved the genai_camp_assistant.py file.
### Run the following command: 
 python genai_camp_assistant.py
 - The script will greet you and ask if you want to ask a question about the camp or sign your kid up.
 - You can type in a response like "I want to ask a question" or "I want to sign up my child". 
 - Depending on your response, the assistant will either answer your question using the details it generated about the camp, or guide you through the application process.

---

You can include this documentation with the code to help any other developer or user understand the approach and how the code functions.
