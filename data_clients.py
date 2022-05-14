import itertools


def clients_dict(d):
    for name, number in d.items():
        number = int(number)
        res = list(map(int, str(number)))
        if len(res) == 10:
            number = f'+7{number}'
            d[name] = number
        elif len(res) == 11:
            if res[0] == 8:
                res[0] = 7
                number = ''.join(str(e) for e in res)
                number = f'+{number}'
                d[name] = number
            elif res[0] == 7:
                number = f'+{number}'
                d[name] = number
    return d



def split_dict_equally(input_dict, chunks=40):
    return_list = [dict() for idx in range(chunks)]
    idx = 0
    for k,v in input_dict.items():
        return_list[idx][k] = v
        if idx < chunks-1:  # indexes start at 0
            idx += 1
        else:
            idx = 0
    return return_list


