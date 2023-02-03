import openai 

openai.api_key = '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'

response = openai.Completion.create(
    model='text-davinci-003', 
    prompt='Você pode explicar o que é um transformer no contexto de NLP?',
    max_tokens=1000
)

print(response.choices[0].text)