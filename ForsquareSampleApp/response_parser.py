def parse_checkin(checkin):
    parsed_checkin = {}
    try:
        parsed_checkin['shout'] = checkin['shout']
        parsed_checkin['first_name'] = checkin['user']['firstName']
        parsed_checkin['last_name'] = checkin['user']['lastName']
    except:
        pass
    return parsed_checkin


def parse_checkins(raw_json):
    checkins_list = raw_json['response']['recent']
    parsed_checkins = []
    for checkin in checkins_list:
        parsed_checkins.append(parse_checkin(checkin))
    return parsed_checkins