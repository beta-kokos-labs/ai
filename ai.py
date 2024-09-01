"""
Models:
[
    "mixtral-8x7b-instruct",
    "llava-7b-chat",
    "llama-2-70b-chat",
    "codellama-34b-instruct",
    "mistral-7b-instruct",
    "pplx-7b-chat",
    "pplx-70b-chat",
    "pplx-7b-online",
    "pplx-70b-online",
]
"""
from perplexityai import Labs

prompt = input("👦: ")
for r in Labs().generate_answer(prompt, "MODEL"): 
    print(f"🤖: {r['output']}")
