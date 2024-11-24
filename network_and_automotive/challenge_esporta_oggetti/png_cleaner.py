# Carica i dati grezzi
with open("./upload.html", "rb") as file:
    raw_data = file.read()

# Trova la firma PNG e il chunk finale IEND
start_index = raw_data.find(b'\x89PNG\r\n\x1a\n')
end_index = raw_data.find(b'IEND') + len(b'IEND') + 4  # Include CRC

# Estrai solo la parte PNG valida
if start_index != -1 and end_index > start_index:
    png_data = raw_data[start_index:end_index]
    # Salva il file PNG pulito
    with open("immagine_pulita.png", "wb") as png_file:
        png_file.write(png_data)
    print("File PNG estratto correttamente.")
else:
    print("Dati PNG non validi.")
