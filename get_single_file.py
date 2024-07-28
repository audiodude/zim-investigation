from libzim.reader import Archive

june = Archive("zims/wikipedia_ab_all_maxi_2024-06.zim")
july = Archive("zims/wikipedia_ab_all_maxi_2024-07.zim")

june_article = june.get_entry_by_path('A/Ҧшьынҩажәи_жәаба')
with open('june_article.txt', 'wb') as f:
  content = bytes(june_article.get_item().content)
  print(len(content), june_article.get_item().size)
  f.write(content)


july_article = july.get_entry_by_path('A/Ҧшьынҩажәи_жәаба')
with open('july_article.txt', 'wb') as f:
  content = bytes(july_article.get_item().content)
  print(len(content), july_article.get_item().size)
  f.write(content)
