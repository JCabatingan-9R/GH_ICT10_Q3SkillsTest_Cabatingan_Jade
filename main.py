from pyscript import display, document


def check(e):
    document.getElementById('output').innerHTML = '' # clear output

    # get username and password values with their id
    user = document.getElementById('user').value
    pw = document.getElementById('pw').value

    # turn variables into lists and get the number of characters using list() and len()
    lu = list(user)
    lp = list(pw)

    username = len(lu)
    password = len(lp)

    # finding out if characters are all letters or all numbers for future conditional statements
    pwlist = [pw.isdigit(), pw.isalpha()]

    # conditional statements
    if username >= 7: # username must contain 7 characters or more
        if password >= 10: # password must contain 10 characters or more
            if pw.isdigit() == True: # if all characters are digits
                display(f'There must be at least one letter in your password.', target="output")
            
            elif  pw.isalpha() == True: # if all characters are letters
                display(f'There must be at least one number in your password.', target="output")
            
            elif any(pwlist) == False: # if there are no True values in pwlist, meaning the password ins't all letters nor all numbers
                display(f'Congratulations! You have successfully signed up!', target="output")
        else:
            display(f'Your password must contain 10 characters.', target="output")
    else: 
        display(f'Your username must contain at least 7 characters.', target="output")