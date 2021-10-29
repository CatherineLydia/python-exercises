from prettytable import PrettyTable
# hover on prettytable , right-click go to definitions

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

print(table)

# Changing Object Attribute
print(table.align)

table.align = "l"

print(table)