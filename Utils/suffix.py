def make_suffix(file_path,suffix):

    lines = []

    with open(file_path,"r") as line:
        for i in line:
            lines.append(i.strip())
        # print(lines)

    with open(file_path,"w") as numberd:
        cnt = 1
        for str in lines:
            numberd.writelines(f"{str}{suffix}\n")
            cnt += 1
    return file_path


# suffix(file_path="local/sample.txt",suffix="d-soft")