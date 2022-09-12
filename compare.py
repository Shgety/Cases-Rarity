import json

with open('actual.json', 'r') as file:
    actual = json.load(file)
with open('memorized.json', 'r') as file:
    memorized = json.load(file)
# if not actual['prime_drops'] == memorized['prime_drops']:
#     actual['prime_drops'] = sorted(actual['prime_drops'])
#     memorized['prime_drops'] = sorted(memorized['prime_drops'])
# else:
#     print ('no changes!')
