import re

def parse_passport(passport):
    passport = passport.strip().split()
    passport = [tuple(kv.split(":")) for kv in passport]
    return dict(passport)


def validate_passport(passport, req_fields, opt_fields):
    req_fields = set(req_fields)
    opt_fields = set(opt_fields)
    pp_fields = set(passport.keys())
    if not(req_fields.issubset(pp_fields)):
      print(pp_fields - req_fields)
      return False
    else:
      print("\nreqd fields present")
    
    return all((validate_byr(passport['byr']),
               validate_iyr(passport['iyr']),
               validate_eyr(passport['eyr']),
               validate_hgt(passport['hgt']),
               validate_hcl(passport['hcl']),
               validate_ecl(passport['ecl']),
               validate_pid(passport['pid'])))
        
def validate_byr(byr):
  try:
    print("byr", byr, 1920 <= int(byr) <= 2002)
    return 1920 <= int(byr) <= 2002
  except ValueError:
    print("Not Valid")
    return False
  
def validate_iyr(iyr):
  try:
    print("iyr", iyr, 2010 <= int(iyr) <= 2020)
    return 2010 <= int(iyr) <= 2020
  except ValueError:
    print("Not Valid")
    return False
  
def validate_eyr(eyr):
  try:
    print("eyr", eyr, 2020 <= int(eyr) <= 2030)
    return 2020 <= int(eyr) <= 2030
  except ValueError:
    print("Not Valid")
    return False
  
def validate_hgt(hgt):

  if re.match(r'\d{3}cm', hgt):
    hgt_cm = int(hgt[:3])
    print("hgt", hgt, 150<= hgt_cm <= 193)
    return 150 <= hgt_cm <= 193

  elif re.match(r'\d{2}in', hgt):
    hgt_inches = int(hgt[:2])
    print("hgt", hgt, 59 <= hgt_inches <= 76)
    return 59 <= hgt_inches <= 76
  else:
    print("hgt", hgt, False)
    return False

  """hgt (Height) - a number followed by either cm or in:
     If cm, the number must be at least 150 and at most 193.
     If in, the number must be at least 59 and at most 76."""

  pass
  
def validate_hcl(hcl):
  return bool(re.match(r'#[0-9a-f]', hcl))
  
def validate_ecl(ecl):
  if len(ecl)==3:
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' )

def validate_pid(pid):
  if len(pid) == 9:
    return bool(re.match(r'[0-9]{9}',pid))
 




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

    parsed = parse_passport(chunk)
    valid = validate_passport(parsed, required, optional)
    n_valid += valid
    chunk = ''

print(n_valid)
