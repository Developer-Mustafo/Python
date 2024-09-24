name = "Mustafo"
print(name.upper())
text = " Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. "
print(text)
print(text.strip())
print(text.split())
text2 = "Aslomu aleykum"
print(text2)
print(text2.replace("Aslomu", "Assalomu"))
age = 15
print(f'Hello my name is {name}, I am {age} years old')
print(name.lower())
print(name.upper())
list = list()
list.append("Hello")
list.append("World")
print(list)
print(type(list))
print(list[0])

class  Student:
	def __init__(self):
		return 'Hello Student'
s = Student()
print(s)