def get_user_info(name, surname, job):
    user = {
        'name': name.upper().strip(),
        'surname': surname.upper().strip(),
        'job': job.lower().strip(),
        'fullname': name + surname,
    }

    return user

user = get_user_info('marek   ', '   marCZAk ', 'PROGRAMista   ')

print(f"{user['name']} {user['surname']} : zawód '{user['job']}'.")