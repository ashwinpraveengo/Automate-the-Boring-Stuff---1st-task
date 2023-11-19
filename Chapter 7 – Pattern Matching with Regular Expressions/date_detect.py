import re

def is_valid_date(d):
    mth_30 = {'04', '06', '09', '11'}
    mth_31 = {'01', '03', '05', '07', '08', '10', '12'}
    mth , dy , yr = d['month'], d['day'], d['year']
    if mth in mth_31 and 1 <= int(dy) <= 31: return True
    if mth in mth_30 and 1 <= int(dy) <= 30: return True
    if mth == '02':
        if 1 <= int(dy) <= 29 and (int(yr) % 4 == 0 and (int(yr) % 100 != 0 or int(yr) % 400 == 0)): return True
        if 1 <= int(dy) <= 28: return True
    return False

date_regex = re.compile(r'(?P<day>0[1-9]|[12]\d|3[01])/(?P<month>0[1-9]|1[0-2])/(?P<year>[12]\d{3})')
matches = date_regex.search('Your date: 31/04/2021')
if matches and is_valid_date(matches.groupdict()):
    print(matches.groupdict()) 
