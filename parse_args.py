def place_parse(args):

    print(type(args))
    # Swap args[0:1] with args[2:3] for more natural directions
    args_ = [args[2], args[3], args[0], args[1]]

    args = args_

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
