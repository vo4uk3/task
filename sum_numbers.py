def sum_numbers_in_file(file):
    with open(file, 'r') as data:
        numbers = [line.split('\n') for line in data.readlines()]
        res = 0
        for  number in numbers:
            for v in number:
                if v.startswith('#') or v.startswith(' '):
                    continue
                try:
                    res += float(v)
                except Exception:
                    pass
        print(res)
