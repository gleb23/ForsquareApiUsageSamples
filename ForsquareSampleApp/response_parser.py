def parse_checkin(checkin):
    try:
        return {
            'shout': checkin.get('shout'),
            'first_name': checkin['user'].get('firstName'),
            'last_name': checkin['user'].get('lastName'),
            'place': checkin['venue'].get('name'),
            'address': checkin['venue'].get('location').get('formattedAddress')[0]
        }
    except:
        return {}


def parse_checkins(raw_json):
    checkins_list = raw_json['response']['recent']
    parsed_checkins = []
    for checkin in checkins_list:
        parsed_checkins.append(parse_checkin(checkin))
    return parsed_checkins


def parse_place(place):
    try:
        return {
            'name': place.get('name'),
            'address': place.get('location').get('formattedAddress')
        }
    except:
        return {}


def parse_places(raw_json):
    checkins_list = raw_json['response']['venues']
    parsed_places = []
    for place in parsed_places:
        parsed_places.append(parse_place(place))
    return parsed_places