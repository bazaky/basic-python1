import base64

text = input("Masukkan teks :\n")
text_bytes = text.encode('ascii')
base64_bytes = base64.b64encode(text_bytes)
base64_text = bas64_bytes.decode('ascii')

print (base64_text)
