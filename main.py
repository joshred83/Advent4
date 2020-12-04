def parse_passport(passport):
  passport = passport.strip().split()
  passport = [tuple(kv.split(":")) for kv in passport]
  return dict(passport)

def validate_passport(passport, req_fields):
  s1 = set(req_fields)
  s2 = set(passport.keys())
  return s1.issubset(s2)


required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
optional =('cid')


with  open("passports_t1") as f:
  chunk = ''
  n_valid = 0
  for line in f:
    if line == '\n':
      parsed = parse_passport(chunk)
      valid = validate_passport(parsed, required)
      print(parsed, valid)
      n_valid += valid
      chunk = ''
    else:
      chunk += line.strip() + ' '
    
print(n_valid)

       
        

  
  




