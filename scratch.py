from passages import Bbuttonlogic, is_beginner_sentence
from sudachipy import Dictionary

tokenizer = Dictionary().create()

beginner_words = {
    "猫",
    "犬",
    "学校",
    "行く",
    "食べる",
    "見る",
    "好き",
}

text = "死刑囚は黙秘した。"

words = tokenizer.tokenize(text)

#for word in words:
#    dic = word.surface()
 #   doc = word.dictionary_form()
  #  print(dic)
   # print(doc)
    #print(
     #   word.dictionary_form(),
      #  word.part_of_speech()[0]
    #)
#for word in words:
   # if beginner_words:
        #print(
           # word.dictionary_form(),
            #word.part_of_speech()[0]
       # )
