import ollama
from langchain_core.prompts import PromptTemplate

# Base template for legal case analysis
base_template = """
You are an AI Legal Advisor tasked with analyzing legal cases and providing judgments based on the Indian Penal Code (IPC). 

**Case Description**: {description}

### Instructions for Case Analysis:
1. **Understand the Case**: Analyze the provided case description to identify key details.
2. **Determine Suspect(s)**: Identify the potential suspect(s) based on the information given.
3. **Define Crime**: Clearly state the nature of the crime involved.
4. **Recommend Punishment**: Suggest an appropriate punishment by referencing the relevant IPC article(s) and explain briefly.

### Output Format:
Suspect: [List of suspect(s)]
Crime: [Nature of the crime]
IPC Article(s): [Relevant article(s) of the IPC]
Punishment: [Recommended punishment]
"""

def ai_judge(prompt):
    """
    Function to interact with the AI Judge model for legal case analysis.
    
    Args:
        prompt (str): The case description to analyze.

    Returns:
        str: The structured judgment from the model.
    """
    # Prepare the message payload for the API call
    messages = [
        {
            'role': 'user',
            'content': create_case_prompt_template(prompt)
        },
    ]
    
    try:
        # Call the AI model
        response = ollama.chat(model='llama3.2:1b', messages=messages)

        if 'message' in response and 'content' in response['message']:
            return response['message']['content']
        else:
            raise ValueError("Unexpected response structure.")

    except Exception as e:
        raise RuntimeError(f"An error occurred: {str(e)}")

def create_case_prompt_template(description):
    """
    Create a prompt template for legal case analysis based on the IPC.

    Args:
        description (str): The user's case description.

    Returns:
        str: A formatted prompt string ready for the legal AI system.
    """
    prompt_template = PromptTemplate(
        input_variables=["description"],
        template=base_template
    )
    return prompt_template.format(description=description)
