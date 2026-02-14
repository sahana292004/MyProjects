# Import necessary modules from langchain_core
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

**Note**: Provide only the analysis results (suspect, crime, IPC article(s), and punishment) in a structured format.

### Output Format:
Suspect: [List of suspect(s)]
Crime: [Nature of the crime]
IPC Article(s): [Relevant article(s) of the IPC]
Punishment: [Recommended punishment]
"""

def create_case_prompt_template(description):
    """
    Create a prompt template for legal case analysis based on the IPC.

    Args:
        description (str): The user's case description.

    Returns:
        str: A formatted prompt string ready for the legal AI system.
    """

    # Log the creation of the prompt template
    print("Creating case analysis prompt template...")

    # Create the final prompt template using the PromptTemplate class
    prompt_template = PromptTemplate(
        input_variables=["description"],
        template=base_template
    )

    # Log the prompt creation with the provided case description
    print(f"Prompt created with case description: {description}")

    # Format the prompt with the case description
    formatted_prompt = prompt_template.format(description=description)

    # Log the final formatted prompt for debugging
    print("Final formatted prompt:", formatted_prompt)

    return formatted_prompt


# Example usage of the function to demonstrate its functionality
if __name__ == "__main__":
    # User input for legal case analysis
    user_case_description = (
        "Mack and Ana were seen arguing at the bungee jumping site before Mack's death. "
        "Mackenzie was also present with nunchaku and has a history of violence."
    )

    # Call the function to create the case prompt template
    case_prompt = create_case_prompt_template(description=user_case_description)

    # Print the generated case analysis prompt for the user
    print("\nGenerated Case Analysis Prompt Template:\n")
    print(case_prompt)

    # Additional comments or explanations can be added here if needed
    print("\n**Note**: Use the generated case analysis prompt to interact with the AI Legal Advisor.")
