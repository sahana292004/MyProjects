import json
import re
from textwrap import shorten


# Load IPC Data
with open("ipc.json", "r", encoding="utf-8") as f:
    ipc_data = json.load(f)

ipc_dict = {str(i["Section"]): i["section_desc"].lower()
            for i in ipc_data if i.get("Section") and i.get("section_desc")}

# Keyword lists for role extraction
suspect_words = ["man", "person", "husband", "thief", "attacker", "driver", "accused"]
victim_words = ["woman", "wife", "victim", "child", "shopkeeper", "passenger", "girl"]

def extract_role(text, keywords):
    for word in keywords:
        if word in text.lower():
            return word.capitalize()
    return "Not identified"

def similarity(case, section):
    case_words = set(re.findall(r'\w+', case.lower()))
    sec_words = set(re.findall(r'\w+', section.lower()))
    if not sec_words:
        return 0.0
    common = len(case_words.intersection(sec_words))
    score = common / max(len(case_words), len(sec_words))
    return min(score, 1.0)

def find_ipc_sections(case, top_n=3):
    results = []
    for sec, desc in ipc_dict.items():
        score = similarity(case, desc)
        if score > 0:
            results.append((sec, score))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_n]

def main():
    case = input("\nEnter case description: \n> ")

    suspect = extract_role(case, suspect_words)
    victim = extract_role(case, victim_words)

    print("\n=========== REPORT ===========")
    print("Suspect Identified: ", suspect)
    print("Victim Identified: ", victim)
     

    matches = find_ipc_sections(case)

    if matches:
        for sec, score in matches:
            print(f"\nIPC Section: {sec}")
            print(f"Match Accuracy: {score*100:.2f}%")
    else:
        print("\nNo IPC match found.")

    print("\nCase Summary:")
    print("→", shorten(case, width=120))
    print("=============================")
      

if __name__ == "__main__":
    main()
    
