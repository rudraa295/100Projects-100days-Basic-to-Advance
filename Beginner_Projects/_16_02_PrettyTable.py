import prettytable as pt

table = pt.PrettyTable()

table.add_column("Student's Name",["Rudra Chaudhary","Utkarsh Thakur","Sachin","Dhruv"])
table.align["Student's Name"] = "l"

table.add_column("Marks",[90,68,60,70])

print(table)

