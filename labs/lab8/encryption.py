def encode(message, key):
    acc = ""
    for c in message:
        i = ord(c)
        added = key + i
        c = chr(added)
        acc += c
    return acc


def encode_better(message, key):
    acc = ""
    for i in range(len(message)):
        c = message[i]
        key1 = key[i % len(key)]
        c = ord(c)
        key2 = ord(key1) - 97
        add = key2 + c
        c = chr(add)
        acc += c
    return acc