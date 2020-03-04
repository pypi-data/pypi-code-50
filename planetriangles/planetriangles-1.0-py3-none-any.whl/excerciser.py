from planetriangles.plane_triangles import *

__all__ = ['run_ui']


def extract(input_str):
    # For internal use.
    if input_str == '':
        return True, None

    try:
        value = float(input_str)
        if value <= 0:
            print('values entered must be > 0')
        return value > 0, value
    except ValueError:
        print(f'{input_str} is not a valid float/integer')
        return False, None


def run_ui():
    while True:

        print("\nSession started...\n")

        # Prompt the user to enter the desired angle format and precisions to use for this session.

        angle_format_str = input('Angle format to use [r, d, dm, dms]: ')
        if angle_format_str not in ['r', 'd', 'dm', 'dms']:
            print("Invalid angle format specifier")
            break

        angle_precision_str = input('Angle precision (digits to right of decimal point) to use: ')
        try:
            angle_precision = int(angle_precision_str)
            if angle_precision < 0:
                print("Angle precision must be >= 0")
                break
        except ValueError:
            print("Angle precision must be an integer")
            break

        length_precision_str = input('Length precision (digits to right of decimal point) to use: ')
        try:
            length_precision = int(length_precision_str)
            if length_precision < 0:
                print("Length precision must be >= 0")
                break
        except ValueError:
            print("Length precision must be an integer")
            break

        # Begin the REPL for getting trianlge specs and producing solutions
        while True:
            a_str = input('\nSide a: ')
            valid, a = extract(a_str)
            if not valid:
                continue

            b_str = input('Side b: ')
            valid, b = extract(b_str)
            if not valid:
                continue

            c_str = input('Side c: ')
            valid, c = extract(c_str)
            if not valid:
                continue

            A_str = input('Angle A (degrees): ')
            valid, A = extract(A_str)
            if not valid:
                continue

            B_str = input('Angle B (degrees): ')
            valid, B = extract(B_str)
            if not valid:
                continue

            C_str = input('Angle C (degrees): ')
            valid, C = extract(C_str)
            if not valid:
                continue

            # If the user entered no values, terminate the session
            if sum(item is None for item in (a, b, c, A, B, C)) == 6:
                break

            # print(a, b, c, A, B, C)

            err_msg, aa, bb, cc, AA, BB, CC = complete_the_triangle(a, b, c, A, B, C)
            if err_msg == '':
                # Got a unique solution
                print(pretty_format_triangle(aa, bb, cc, AA, BB, CC, angle_form=angle_format_str,
                                             angle_precision=angle_precision,
                                             length_precision=length_precision))
            elif err_msg.startswith('Other'):
                # There are two possible triangles that satisfy the constraints given...
                # ... print the first one
                print(pretty_format_triangle(aa, bb, cc, AA, BB, CC, angle_form=angle_format_str,
                                             angle_precision=angle_precision,
                                             length_precision=length_precision))
                # ... and then ask for the 'other' solution
                err_msg, aa, bb, cc, AA, BB, CC = complete_the_triangle(a, b, c, A, B, C, ssa_flag='other')
                if err_msg == '':
                    print(pretty_format_triangle(aa, bb, cc, AA, BB, CC, angle_form=angle_format_str,
                                                 angle_precision=angle_precision,
                                                 length_precision=length_precision))
                else:
                    print(f'err_msg: {err_msg}  !!!! THIS INDICATES A PROGRAMMING ERROR !!!!')
            else:
                print(f'{err_msg}')

        print("\nSession completed.")
        break
