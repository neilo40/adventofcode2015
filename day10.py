current_password = "hepxcrrq"
alphabet = "abcdefghijklmnopqrstuvwxyz"
doubles = ["{}{}".format(x, x) for x in alphabet]
straights = ["{}{}{}".format(alphabet[x], alphabet[x + 1], alphabet[x + 2]) for x in range(len(alphabet) - 2)]

def increment_password(old_password):
    new_password = ""
    inc_next = True
    for letter in reversed(old_password):
        if inc_next:
            if letter == 'z':
                new_password += 'a'
            else:
                new_password += alphabet[alphabet.index(letter) + 1]
                inc_next = False
        else:
            new_password += letter
    return "".join(reversed(new_password))


def is_valid(password):
    return has_no_forbidden_letters(password) and has_a_straight(password) and has_two_doubles(password)


def has_no_forbidden_letters(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    else:
        return True


def has_a_straight(password):
    for straight in straights:
        if straight in password:
            return True 
    return False


def has_two_doubles(password):
    double_count = 0
    for double in doubles:
        if double in password:
            double_count += 1
    return double_count >= 2    


def get_new_password(password):
    new_password_is_valid = False
    while not new_password_is_valid:
        password = increment_password(password)
        new_password_is_valid = is_valid(password)
    print(password)
    return password


new_password = get_new_password(current_password)
get_new_password(new_password)
        
