import random
import string

def make_ordered_password(length, name_part='', number_part='', include_symbols=True):
    if not name_part and not number_part:
        print("Nothing entered. Using suggested base: yukti@2809")
        name_part = "yukti"
        number_part = "2809"

    symbol_segment = '@' if include_symbols else ''
    core = name_part + symbol_segment + number_part
    padding_length = length - len(core)

    filler = ''
    if padding_length > 0:
        filler_chars = string.ascii_letters + string.digits
        if include_symbols:
            filler_chars += "!#$%^&*"

        filler = ''.join(random.choice(filler_chars) for _ in range(padding_length))

    final_password = core + filler
    return final_password


if __name__ == "__main__":
    print("=== Structured Password Creator ===\n")

    try:
        length_input = input("Desired total password length: ")
        pw_length = int(length_input)

        user_name = input("Enter name/letters you'd like (leave blank for default): ").strip()
        user_numbers = input("Enter numbers you'd like to include (leave blank for default): ").strip()
        symbol_pref = input("Do you want a symbol between them? (yes/no): ").strip().lower()

        add_symbol = symbol_pref == 'yes'

        generated_pw = make_ordered_password(pw_length, user_name, user_numbers, add_symbol)
        print("\nHere’s your generated password:\n" + generated_pw)

    except ValueError:
        print("Please enter a valid number for length.")


