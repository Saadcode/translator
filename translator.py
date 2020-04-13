from googletrans import Translator

text = input('')

#language dict
language_dict = {
  'Arabic' : 'ar', 
  'Chinese' : 'zh-CN', 
  'Danish' : 'da', 
  'Dutch' : 'nl', 
  'English' : 'en', 
  'French' : 'fr', 
  'German' : 'de', 
  'Greek' : 'el', 
  'Hindi' : 'hi', 
  'Indonesian' : 'id', 
  'Italian' : 'it', 
  'Japanese' : 'ja', 
  'Korean' : 'ko', 
  'Latin' : 'la', 
  'Mongolian' : 'mn', 
  'Norwegian' : 'no', 
  'Russian' : 'ru', 
  'Spanish' : 'es', 
  'Vietnamese' : 'vi'
  } 

translator = Translator()

if __name__ == '__main__':
  for key, value in language_dict.items() :
    if key in text :
      split_text = text.split(' ')
      list_remove = []
      list_remove.append(split_text[0])
      list_remove.append(split_text[-1])
      list_remove.append(split_text[-2])
      for word in list_remove :
        text = text.replace(word, '')

      print(translator.translate(text, dest=value).text)

