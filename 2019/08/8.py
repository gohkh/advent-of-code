with open("8.txt", 'r') as f:
    image = f.readlines()[0].strip()

layers = [image[i:25*6+i] for i in range(0, len(image), 25*6)]
sorted_layers = sorted(layers, key=lambda x: x.count("0"))
print(sorted_layers[0].count("1") * sorted_layers[0].count("2"))

final_image = ""
for i, pixel in enumerate(layers[0]):
    if pixel == "2":
        z = 1
        while layers[z][i] == "2":
            z += 1
        pixel = layers[z][i]

    if pixel == "0": # readability
        pixel = " "
    else:
        pixel = "0"

    final_image += pixel

rows = [final_image[i:25+i] for i in range(0, len(final_image), 25)]
for row in rows:
    print(row)
