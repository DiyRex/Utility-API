def duplicate(file_path):
    with open(file_path) as result:
        uniqlines = set(result.readlines())
        with open(file_path, 'w') as rmdup:
            rmdup.writelines(set(uniqlines))

    return file_path