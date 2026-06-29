from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key=("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")
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)