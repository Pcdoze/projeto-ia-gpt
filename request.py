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
      {"role": "system", "content": "Responda ao usuário com um breve resumo do texto"},
      {"role": "user", "content": prompt}
    ],
    max_tokens=50
  )
  
  if completion.choices[0].message.content is not None:
      return completion.choices[0].message.content