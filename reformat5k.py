with open("data_file.fasta", "r") as f:
    #lines = f.readlines()
    lines = [next(f) for x in range(10000)]

with open("newfile.txt", "w") as f:
    for line in lines:
        if not line.strip("\n").startswith(">"):
            f.write(line)