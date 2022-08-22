import json
f = open('../cities.json',) 
data = json.load(f)

def all_CountryNames():
	all_country = list()
	for dct in data:
		all_country.append(dct['country'])
	return list(dict.fromkeys(all_country))

def all_Country_StateNames():
	all_country = list()
	states = []
	state_names = []
	for dct in data:
		all_country.append(dct['country'])
	all_country = list(dict.fromkeys(all_country))
	state_list = list()
	for country in all_country:
		all_state = list()
		for dct in data:
			if dct['country'] == country:
				all_state.append(dct['subcountry'])
		all_state = list(dict.fromkeys(all_state))
		states.append(all_state)
		state_list.append({country:all_state})
		for i in states:
			for j in i:
				state_names.append(j)
# 	return state_names  if you want the name of the states alone in a list
	return json.dumps(state_list)

def all_State_CityNames(flag='all'):
	all_subcountry = list()
	all_city_list = list()
	cities = []
	city_names = []
	for dct in data:
		all_subcountry.append(dct['subcountry'])
	all_subcountry = list(dict.fromkeys(all_subcountry))
	if flag == 'all':
		for subcountry in all_subcountry:
			city_list = list()
			for dct in data:
				if dct['subcountry'] == subcountry:
					city_list.append(dct['name'])
			city_list = list(dict.fromkeys(city_list))
			all_city_list.append({subcountry:city_list})
			cities.append(city_list)
			for i in cities:
				for j in i:
					city_names.append(j)
	else:
		city_list = list()
		subcountry = flag
		for dct in data:
			if dct['subcountry'] == subcountry:
				city_list.append(dct['name'])
		city_list = list(dict.fromkeys(city_list))
		all_city_list.append({subcountry:city_list})

# 	return city_names  if you want the name of the cities alone in a list
	return json.dumps(all_city_list)





#print(all_State_CityNames())
