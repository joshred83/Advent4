
import re
import json
required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')

def get_next_passport(file_stream):
  passport = ''
  line = ''
  while line != '\n':
    line = f.readline()
    passport += ' ' + line.strip()
  passport.strip().split()

f = open("passports_t1")
    passport = get_next_passport(f)
print(passport)
with  open("passports_t1") as f
    passport = get_next_passport(f)

  
  
  




