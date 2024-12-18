import zlib, base64

# Učitaj podatke iz datoteke
data = open("demo.txt", "r").read()

# Pretvori podatke u bajtove
data_bytes = bytes(data, "utf-8")

# Komprimiraj podatke i kodiraj ih u base64 format
compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))

# Dekodiraj u string format za spremanje
decoded_data = compressed_data.decode("utf-8")

# Spremi komprimirane podatke u datoteku
compressed_file = open("compressed.txt", "w")
compressed_file.write(decoded_data)
compressed_data.close()

# Dekomprimiraj podatke za provjeru
decompressed_data = zlib.decompress(base64.b64decode(decoded_data))
print(decompressed_data)
