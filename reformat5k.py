# reformat data_file.fasta to have 5000 amino acids with spaces between each letter

with open("data_file.fasta", "r") as f:
    lines = [next(f) for x in range(10000)]

with open("newfile.txt", "w") as f:
    for line in lines:
        if not line.strip("\n").startswith(">"):
            for character in line[1:]:
                f.write(character + " ")

# add a single space in line 1 after
# remove single line at the end