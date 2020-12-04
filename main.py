def parse_passport(passport):
    passport = passport.strip().split()
    passport = [tuple(kv.split(":")) for kv in passport]
    return dict(passport)


def validate_passport(passport, req_fields, opt_fields):
    req_fields = set(req_fields)
    opt_fields = set(opt_fields)
    pp_fields = set(passport.keys())
    return set(req_fields).issubset(set(passport.keys()))


required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
optional = ('cid')

with open("passports_d4") as f:
    chunk = ''
    n_valid = 0
    for line in f:
        if line == '\n':
            parsed = parse_passport(chunk)
            valid = validate_passport(parsed, required, optional)
            n_valid += valid
            chunk = ''
        else:
            chunk += line.strip() + ' '

print(n_valid)
