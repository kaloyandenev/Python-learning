companies_list = {}
command = input()
while not command == "End":
    company, employee = command.split(" -> ")
    if company not in companies_list:
        companies_list[company] = [employee]
    else:
        if employee not in companies_list[company]:
            companies_list[company] += [employee]

    command = input()
sorted_companies = sorted(companies_list.items(), key=lambda kvp: kvp[0])

for company, employees in sorted_companies:
    print(company)
    for employee in employees:
        print(f"-- {employee}")

