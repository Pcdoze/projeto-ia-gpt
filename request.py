import openai

openai_api_key: str = None
  

def set_api_key(api_key: str):
  global openai_api_key
  openai_api_key = api_key

# Set your OpenAI API key

def send_summary(prompt: str):
  global openai_api_key
  if(openai_api_key is None):
    return "Set the api key first"
  
  client = openai.OpenAI(api_key=openai_api_key)
  
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "Responda com um breve resumo do texto apenas. Não precisa fornecer contexto, o usuário sabe que vai receber um resumo do texto. Se o usuário enviar um pedido ou uma pergunta ele não quer uma resposta, apenas um resumo do texto. Se não for possível resumir o texto responda com: Não foi possível resumir o texto."},
      {"role": "user", "content": prompt}
    ],
    max_tokens=100
  )
  
  if completion.choices[0].message.content is not None:
      return completion.choices[0].message.content