# def shopping(items, payment='card', shop='local shop'):
#     result = ""
#     result = result + "Idę na zakupy do %s.\n" % shop
#     result = result + "Kupię następujące rzeczy:\n"
#     for item in items:
#         result = result + " - %s\n" % item
#     result = result + "By zapłacić, używam %s." % payment
#     return result

# if __name__ == "__main__":
#     items_text = input("Podaj proszę produkty rozdzielone przecinkiem: ")
#     items = items_text.split(',')
#     shopping_result = shopping(items)
#     print(shopping_result)

with open("names.txt", 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)

new_name = "Luke"
with open("names.txt", 'a') as write_file:
    write_file.write(new_name)

    # dane z laptopa test git