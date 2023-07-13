#Create a CLI Program that would take a sentence of at least 10 words (>= 10) and would let you translate to at least 5 different languages (10 better for fun). 
#Plus there have to be an option to get symbols/letters amount of the translation. And there should be the option to translate to 
#all languages at the same time. The whole program should be dockerized and tested. Please find, which translation have the shortest/longest variation.

# pylint: disable=all
from translate import Translator
languages = ["de", "fr", "it", "be", "pl", "sv", "uz", "zh", "lt", "so"]
translated_sentence = []
translated_sentence_length = []

def translaitor():

    while True:
        sentence = input("Please instert sentence: ")
        count_of_words_in_sentence = len(sentence.split())
    
        if count_of_words_in_sentence >= 1:
            break
        else: 
            print("please insert sentence more then 10 words")

    for language in languages:
        translator = Translator(from_lang="en", to_lang=language)
        translation = translator.translate(sentence)
        translated_sentence.append(translation)
        print(f"{language}: {translation}")

                
#     for translation in translated_sentence:
#         translated_sentence_len = len(translation)
#         translated_sentence_length.append(translated_sentence_len)
#         list_zip = zip(languages, translated_sentence_length)
#         zipped_list = list(list_zip)
#     print(zipped_list)

if __name__ == '__main__':
    translaitor()






