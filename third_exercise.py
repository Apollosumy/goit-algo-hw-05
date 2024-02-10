contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)

    return inner

@input_error
def hello_command(args):
    return "How can I help you?"

@input_error
def add_contact(args):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        raise ValueError("Invalid command format. Use: add [name] [phone]")

@input_error
def change_contact(args):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            raise KeyError("Contact not found.")
    else:
        raise ValueError("Invalid command format. Use: change [name] [new_phone]")

@input_error
def show_phone(args):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            raise KeyError("Contact not found.")
    else:
        raise ValueError("Invalid command format. Use: phone [name]")

@input_error
def show_all(args):
    if not contacts:
        return "No contacts found."
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone} \n"
        return result.strip()

@input_error
def exit_command(args):
    return "Good bye!"

commands = {
    "hello": hello_command,
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": show_all,
    "close": exit_command,
    "exit": exit_command
}

def process_command(user_input):
    command_parts = user_input.split()
    if not command_parts:
        return "Enter a command:"

    command = command_parts[0]
    args = command_parts[1:]

    if command in commands:
        return commands[command](args)
    else:
        return "Unknown command. Type 'help' for a list of commands."

def run():
    print("Contact Management Bot is running. Type 'exit' or 'close' to quit.")
    while True:
        user_input = input("Enter a command: ").lower()
        result = process_command(user_input)
        print(result)

if __name__ == "__main__":
    run()