import openai
openai.api_key = "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"
def generate_blog(paragraph_topic):
  response = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )

  retrieve_blog = response.choices[0].text

  return retrieve_blog
print(generate_blog('Why NYC is better than your city.'))