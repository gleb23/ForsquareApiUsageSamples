import logging


def parse_checkin(checkin):
    logging.log(2, "Parsing checkin " + str(checkin))
    try:
        return {
            'shout': checkin.get('shout'),
            'first_name': checkin['user'].get('firstName'),
            'last_name': checkin['user'].get('lastName'),
            'place': checkin['venue'].get('name'),
            'address': get_formatted_address(checkin['venue'])
        }
    except:
        return None

def get_formatted_address(venue):
    formatted_address = venue.get('location').get('formattedAddress')
    if formatted_address is not None and len(formatted_address) > 0:
        return formatted_address[0]

def parse_checkins(raw_json):
    checkins_list = raw_json['response']['recent']
    parsed_checkins = []
    for checkin in checkins_list:
        parsed_checkin = parse_checkin(checkin);
        if parsed_checkin is not None:
            parsed_checkins.append(parsed_checkin)
    return parsed_checkins


def parse_place(place):
    try:
        return {
            'name': place.get('name'),
            'address': get_formatted_address(place)
        }
    except:
        return {}


def parse_places(raw_json):
    places = raw_json['response']['venues']
    parsed_places = []
    for place in places:
        parsed_places.append(parse_place(place))
    return parsed_places