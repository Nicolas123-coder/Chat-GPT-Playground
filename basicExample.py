import openai 
from myOpenAi import MyOpenAI

apiKey = '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'

openai.api_key = apiKey

chat = MyOpenAI(
    'Aonde fica o rio de janeiro?', 
    'text-davinci-003', 
    3,
    1000,
    1,
    apiKey
)
resposta = chat.callGpt()

for x in resposta: 
    print(x)