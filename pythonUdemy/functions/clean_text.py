words = ['java', 'css', 'html', 'python']
text = "To jest bardzo dlugi tekst, ktory zawiera java oraz html css ale ma tez w sobie python."

def clean_text(text):
    for word in words:
        text = text.replace(word, '****')
    return text

result = clean_text(text)
print(result)