# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]


def censor_one(text, phrase):
  censored_text = text.replace(phrase, len(phrase)*'X')
  return censored_text

def censor_two(text, phrases):
  for phrase in phrases:
    if phrase in text:
      text = censor_one(text, phrase)
  return text

def censor_three(text, phrases, negative_words):
  text = text.lower()
  new_text = censor_two(text, phrases)
  count = 0
  for word in negative_words:
    if word in new_text:
      count += 1
      if count > 2:
        new_text = censor_one(new_text, word)
  return new_text   

def censor_all(text, phrases, negative_words):
  text = text.lower()
  new_text = censor_two(text, phrases)
  for word in negative_words:
    if word in new_text:
      new_text = censor_one(new_text, word)
  new_text = new_text.split()
  for i in range(len(new_text)):
    if 'X' in new_text[i]:
      new_text[i-1] = len(new_text[i-1])*'Y'
      new_text[i+1] = len(new_text[i-1])*'Y'
  new_text = ' '.join(new_text)
  return new_text

print(censor_all(email_four,proprietary_terms, negative_words))


