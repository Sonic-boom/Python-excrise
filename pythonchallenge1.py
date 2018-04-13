strs = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''


def change(strs):
    res = []
    for x in strs:
        if x != ' ' and x != '.':
            res += chr((ord(x)-97+2) % 26 + 97)
        else:
            res += ' '
    print("".join(res))


change(strs)
'''
i hope you didnt translate it by handd thats what computers are ford doing it in by hand is inefficient and thatws why this text is so longd using stringdmaketransxy is recommendedd now apply on the urld
'''
change("map")
