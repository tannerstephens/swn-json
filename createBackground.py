import json

with open('backgrounds.json') as f:
  data = json.load(f)

name = input('Name: ').lower()

desc = input('Description: ')
nextline = input()

while nextline:
  desc += f' {nextline}'
  nextline = input()

free_skill = [input('Free Skill:').lower()]

quick_skills = []
print('Quick Skills')
for i in range(3):
  quick_skills.append([input(f'{i+1}: ').lower()])

growth = []
print('Growth')
for i in range(6):
  g = input(f'{i+1}: ').lower()

  if '+' in g:
    growth.append({
      'type': 'stat',
      'change': 1,
      'stat': ["str","dex","con","int","wis","cha"],
      "text": g
    })
  else:
    growth.append({
      'type': 'skill',
      'skill': ["administer","connect","exert","fix","heal","know","lead","notice","perform","pilot","program","punch","shoot","sneak","stab","survive","talk","trade","work"],
      "text": g
    })


learning = []
print('Learning')
for i in range(8):
  learning.append([input(f'{i+1}: ').lower()])

data[name] = {
  "description": desc,
  "freeSkill": free_skill,
  "quickSkills": quick_skills,
  "growth": growth,
  "learning": learning
}

with open('backgrounds.json', 'w') as f:
  json.dump(data, f, indent=2)
