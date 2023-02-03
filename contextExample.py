import openai 
from myOpenAi import MyOpenAI

apiKey = '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'

openai.api_key = apiKey

contexto = '''Somos especializados em aquecimentos de piscinas, seja através de painéis solares
            ou trocadores de calor. Estamos localizados em pinheiros (SP) na rua capote valente.
            Nosso horário de funcionamento é de segunda e sexta das 8 às 19 horas e sábado das 8 
            a meio dia. '''

response = openai.Completion.create(
    model='text-davinci-003', 
    prompt= contexto + 'Vocês colocam aquecimento em piscinas ?',
    max_tokens=1000,
    temperature=1
)

print(response.choices[0].text)