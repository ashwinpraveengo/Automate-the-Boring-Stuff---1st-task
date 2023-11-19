import re

def regex_strip(s, ch=None):
    if ch is None:
        return re.sub(r'^\s+|\s+$', '', s)
    ch = re.escape(ch)
    return re.sub(rf'^[{ch}]+|[{ch}]+$', '', s)

print(regex_strip('  hello  '))     
print(regex_strip('##hello##', '#'))
