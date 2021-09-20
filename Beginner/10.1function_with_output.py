# Functions with Outputs

def format_name(f_name,l_name):
    """ Take a first and last and format it to return
    the title case version of the name"""    #Docstrings
    if f_name=="" or l_name=="":
        return "Invalid input"
    else:
        formatted_f_name=f_name.title()
        formatted_l_name=l_name.title()     #title case => My First And Last Name
        return f"{formatted_f_name} {formatted_l_name}"

title_case=format_name(input("What is your first name?"),input("What is your last name?"))
print("Formatted Name:",title_case)

