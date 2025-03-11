import os

def spacing(text):
    new_text = text
    for c in ('X', 'Y', 'Z', 'F'):
        index = new_text.find(c)
        if index != -1:
            new_text = new_text[:index] + ' ' + new_text[index:]
    return new_text

while True:
    path = input("Enter file path: ")
    output_path = "C:\\Users\\nguye\\Desktop"
    try:
        input_file = open(path, 'r')
        break
    except OSError:
        print("Invalid path")

with open(os.path.join(output_path, 'output.gcode'), 'w') as output_file:

    # add header
    #output_file.write("G28;\n")

    # transfer and modify code from original .nc file
    line = input_file.readline()
    while line:
        text = line.splitlines()[0].upper()

        if text[0].upper() == 'X' \
            or text[0].upper() == 'Y' \
                or text[0].upper() == 'Z':

            output_file.write("G0{};\n".format(spacing(text)))

        elif text[0].upper() == 'G':
            output_file.write(spacing(text) + ';\n')

        line = input_file.readline()

    # add footer
    output_file.write("G28 X0 Y0;\n"
                      "M18")

input_file.close()
print("gcode file successfully generated!\n"
      "(file: output.gcode)\n"
      "(location: Desktop)")