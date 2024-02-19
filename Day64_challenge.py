class jobs():
  name = None
  salary = None
  hours = None

  def __init__(self, name, salary, hours):
    self.name = name
    self.salary = salary
    self.hours = hours

  def details(self):
    print(f"name:{self.name}\nsalary:{self.salary}\nhours:{self.hours}")


class doctor(jobs):
  specilization = None
  experience = None

  def __init__(self, salary, hours, specilization, experience):
    self.name = "doctor"
    self.salary = salary
    self.hours = hours
    self.specilization = specilization
    self.experience = experience

  def details(self):
    print(
      f"name:{self.name}\nsalary:{self.salary}\nhours:{self.hours}\nSpeciality:{self.specilization}\nYears:{self.experience}"
    )


class teacher(jobs):
  subject = None
  position = None

  def __init__(self, salary, hours, subject, position):
    self.name = "Teacher"
    self.salary = salary
    self.hours = hours
    self.subject = subject
    self.position = position

  def details(self):
    print(
      f"name:{self.name:<10}\nsalary:{self.salary}\nhours:{self.hours}\nSubject:{self.subject}\nPosition:{self.position}"
    )


print("🌟Jobs Jobs Jobs!🌟")
print()
job = jobs("Lawyer", "Squillions", "60")
print(job.details())
print()

doctor = doctor("2000", 8, "Dnetis", "12")
print(doctor.details())
print()

teacher = teacher("2000", "60", "Computer Science", "Classroom Teacher")
print(teacher.details())
print()

print()
