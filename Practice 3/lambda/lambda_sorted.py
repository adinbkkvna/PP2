students=[("Adina",90),("Aruzhan",85),("Alina",80),("Asiya",70)]
sorted_students=sorted(students,key=lambda x:x[1])
print(sorted_students)

words=["apple","fruit","elephant","cup"]
sorted_words=sorted(words, key=lambda x:len(x))
print(sorted_words)