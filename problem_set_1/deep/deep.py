input_string = input("What is the Answer to the Great Question of Life, " \
"the Universe, and Everything? ").lower().strip()
match input_string:
    case '42':
        print('Yes')
    case 'forty two' | 'forty-two':
        print('Yes')
    case _ :
        print('No')

