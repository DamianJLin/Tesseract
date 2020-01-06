def place_parse(args):

    # Check correct number of arguments
    if len(args) == 4:

        # Check arguments are digits
        args_are_digits_flag = True
        try:
            args = list(map(int, args))
        except ValueError:
            args_are_digits_flag = False

        if args_are_digits_flag:

            # Check all digits are in correct range
            if all(0 <= args[j] < 5 for j in range(len(args))):

                return args

            else:

                print('All coordinates must be in the range [0, 4]')
                return None

        else:

            print('Arguments must be integers. Type help for details.')
            return None

    else:

        print('Wrong number of arguments. Type help for details.')
        return None
