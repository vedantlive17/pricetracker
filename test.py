try:
    if '2' != 2:
        raise ValueError
    else:
        print('same')
except ValueError:
    print('ValueError')
except NameError:
    print('NameError')