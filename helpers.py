def find_user_by_id(user_list, user_id):
    return next((user for user in user_list if user['id'] == user_id), None)


def filter_users_by_status(user_list, status):
    return [user for user in user_list if user['status'] == status]


def format_user_data(user):
    return {
        'id': user['id'],
        'name': user['name'],
        'status': user['status']
    }


def sort_users_by_name(user_list):
    return sorted(user_list, key=lambda user: user['name'])


def group_users_by_status(user_list):
    grouped = {}
    for user in user_list:
        status = user['status']
        if status not in grouped:
            grouped[status] = []
        grouped[status].append(user)
    return grouped


def validate_user_data(data):
    required_keys = ['id', 'name', 'status']
    return all(key in data for key in required_keys)