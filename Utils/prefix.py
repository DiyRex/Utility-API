def make_prefix(file_path,prefix):

    lines = []

    with open(file_path,"r") as line:
        for i in line:
            lines.append(i.strip())
        # print(lines)

    with open(file_path,"w") as numberd:
        cnt = 1
        for str in lines:
            numberd.writelines(f"{prefix}{str}\n")
            cnt += 1
    return file_path


# prefix(file_path="local/sample.txt",prefix="d-soft")