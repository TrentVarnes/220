"""
Trent Varnes
sales_force.py
I certify this is my work
"""


from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = SalesPerson
        self.sales_people = []

    def add_data(self, file_name):
        infile = open(file_name, "r")
        content = infile.read()
        content = content.replace("\n", ", ")
        self.sales_people = content.split("\n")

    def quota_report(self, quota):
        people = []
        for person in self.sales_people:
            people.append([person.get_id(), person.get_name(), person.get_sales(), person.met_quota(quota)])
        return people

    def top_seller(self):
        top = []
        for i in range(len(self.sales_people)):
            highest = self.sales_people[i].get_sales()
            pos = i
            for x in range(i, len(self.sales_people)):
                if self.sales_people[x].get_sales() > highest:
                    highest = self.sales_people[x].get_sales()
                    pos = x
                self.sales_people[i], self.sales_people[pos] = self.sales_people[pos], self.sales_people[i]
        top.append(self.sales_people[0])
        for j in range(1, len(self.sales_people)):
            if self.sales_people[j].get_sales() == top[0].get_sales():
                top.append(self.sales_people[j])
        return top

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None
