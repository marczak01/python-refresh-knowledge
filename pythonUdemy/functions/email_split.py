import time
t_start = time.perf_counter()

def email_split(email):
    monkey_index = email.find('@')
    dot_index = email.rfind(".")
    user_info = {
        'user': email[:monkey_index],
        'domain': email[monkey_index+1:dot_index],
        'domain_ext': email[dot_index+1:],
    }
    return f"User : {user_info['user']} at domain '{user_info['domain']}' with domain ext: '{user_info['domain_ext']}'"


print(email_split('marczak3.ds.42lol@icloud.com'))


t_end = time.perf_counter()
print(t_end - t_start)