from common.openai import openai


def generate_text(text: str):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=text,
    temperature=0.7,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response["choices"][0]["text"]