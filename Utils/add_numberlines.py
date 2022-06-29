def number_lines(file_path):

    lines = []

    with open(file_path,"r") as line:
        for i in line:
            lines.append(i.strip())
        # print(lines)

    with open(file_path,"w") as numberd:
        cnt = 1
        for str in lines:
            numberd.writelines(f"{cnt:02d}.{str}\n")
            cnt += 1
    return file_path

#  number_lines(file_path="local/sample.txt")