text = input()
accumulated_text = ""

while text != 'Stop':
    accumulated_text += text + "\n"
    text = input()

print(accumulated_text)


#
# accumulated_text = ""
#
# while True:
#     text = input()
#     if text == 'Stop':
#         break
#     accumulated_text += text + "\n"
#
# print(accumulated_text)
