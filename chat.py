from openai import OpenAI
client = OpenAI()

def chat(user_message):
    completion = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[{"role": "user", "content": user_message}])

    print(completion)

chat("hello")