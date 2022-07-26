with open("newfile.txt", "r") as f:
    lines = f.readlines()

with open("pfam_all.json", "w") as f:
    for line in lines:
        new_string = ('{"text": "' + line[1:-1] + '"}\n')
        f.write(new_string)
# remove single line at the end