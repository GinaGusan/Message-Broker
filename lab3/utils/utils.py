class Employee(object):
    def __init__(self, name, surname, salary, department):
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary

    def __repr__(self):
        return self.name + self.surname + self.department + self.salary

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.department + ' ' + self.salary


class Location(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __repr__(self):
        return self.ip + self.port

    def __str__(self):
        return self.ip + ' ' + str(self.port)
