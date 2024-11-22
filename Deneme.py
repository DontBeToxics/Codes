meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "bir şakaya karşılık cevap",
    "SHEESH": "onaylamamak",
    "CREEPY": "Korkunç",
    
            }
while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print(meme.dict[word])
        break
