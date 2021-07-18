import googletrans as gt
import pandas as pd

# #Count of supported languages
# print(len(googletrans.LANGUAGES))

# #Supported languages list
# print(googletrans.LANGUAGES)

translator = gt.Translator()
sentence = "Merhaba, Nasılsın"
example = translator.translate(sentence, dest="es")  # dest="es" --> Destination is spanish
# print(example)
# print(example.src) # "tr" # Org. Lang
# print(example.dest) # "en" # Translated lang.
# print(example.origin) # org. text
# print(example.text) # Result
# print(example.pronunciation) #result

# words_to_translate = ["selam", "kiraz", "telefon"]
# translated_words = []

# for word in words_to_translate:
#     translated_words.append(translator.translate(word, dest="es").text)
# print(translated_words)

words_tr = ['Mandalina', "Badem", "Elma", "Kirpi",
            "Kumsal", "Şeker", "Kahve", "Dünya"]

df = pd.DataFrame(columns=["Turkish", "English", "French",
                           "German","Spanish","Arabic","Russian"])

for word in words_tr:
    df = df.append(
        {
        "Turkish" : word,
        "English" : translator.translate(word, dest="en").text,
        "French" : translator.translate(word, dest="fr").text,
        "German" : translator.translate(word, dest="de").text,
        "Spanish" : translator.translate(word, dest="fr").text,
        "Arabic" : translator.translate(word, dest="ar").text,
        "Russian" : translator.translate(word, dest="ru").text
        },
        ignore_index=True)

print(df)