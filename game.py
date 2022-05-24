import random
 
fruits = [
   "apple", "apricot", "orange", "longan",
   "coconut", "fig", "lemon", "peach", "avocado",
   "banana","pear","kiwi", "kumquat", "plum", "cherry",
   "rambutan", "papaya", "mangosteen", "pomelo", "tamarind"
]
tiep = "y"
while(tiep=="y"):
   numFruits = len(fruits)
   fruitName = fruits[random.randint(0,numFruits-1)]
   fruitLen = len(fruitName)
   keyPos = random.randint(0, len(fruitName)-1)
   keyChar = fruitName[keyPos]
   hint = ""
   for i in range(fruitLen):
      if i == keyPos:
         hint += " " + keyChar
      else:
         hint += " _"
   print("gợi ý về loại quả" + hint)
   print("Mời bạn nhập tên quả đó: ")
   name = input()
   if name == fruitName:
      print("Bạn đã nhập đúng")
   else:
      print("Bạn đã nhập sai. Kết quả phải là: "+fruitName)
   print("Bạn có muốn tiếp tục chơi? (nhập y để tiếp tục)")
   tiep = input()
# hello
