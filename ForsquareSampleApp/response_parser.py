def parse_checkin(checkin):
    try:
        return {
            'shout': checkin['shout'],
            'first_name': checkin['user']['firstName'],
            'last_name': checkin['user']['lastName']
        }
    except:
        return {}


def parse_checkins(raw_json):
    checkins_list = raw_json['response']['recent']
    parsed_checkins = []
    for checkin in checkins_list:
        parsed_checkins.append(parse_checkin(checkin))
    return parsed_checkins