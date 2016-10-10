import json
from pprint import pprint

gear = {}
skills = {}
skillpoints = {}
jewels = {}
with open('gear_data.json', encoding='utf8') as data:
    mhdata = json.load(data)
    for item in mhdata:
        name = item['name']
        name = name.replace('.', '')
        gear[name] = {}
        gear[name]['resist'] = {str(key): value for (key, value) in enumerate(item['resist'])}
        gear[name]['maxdef'] = item['maxdef']
        gear[name]['part'] = item['part']
        gear[name]['mindef'] = item['mindef']
        gear[name]['skills'] = {(str(key)).replace('.', ''): value for (key, value) in item['skills'].items()}
        gear[name]['slots'] = item['slots']
        gear[name]['type'] = item['type']
        gear[name]['period'] = item['period']
        gear[name]['sex'] = item['sex']

with open('skills.json', encoding='utf8') as data:
    mhdata = json.load(data)
    #pprint(mhdata)
    for skill in mhdata.keys():
        points = mhdata[skill]
        name = skill.replace(".", "")
        skills[name] = points

with open('skillpoints.json', encoding='utf8') as data:
    mhdata = json.load(data)
    for skill in mhdata['skills']:
        name = skill['name']
        name = name.replace('/', ' ')
        skillpoints[name] = {"points": skill["points"], "type": skill["type"], "skill": skill["skill"]}

with open('jewels.json', encoding='utf8') as data:
    mhdata = json.load(data)
    for jewel in mhdata:
        name = jewel['name']
        name = name.replace(". ", " ")
        name = name.replace('.', ' ')
        jewel_skill = {}
        for key in jewel['skills'].keys():
            name = key.replace('.', ' ')
            jewel_skill[name] = jewel['skills'][key]
        jewels[name] = {"skills": jewel_skill, "slots": jewel['slots'], 'period': jewel['period']}

with open('mhdb_fixed.json', 'w') as outfile:
    json.dump({'gear': gear, 'skills': skills, 'skillpoints': skillpoints, 'jewels': jewels}, outfile)
