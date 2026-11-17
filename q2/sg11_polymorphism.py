#patient class
class Patient:
  def __init__(self, name : str, bill_amount: float):
    self.__name = name
    self.__bill_amount = bill_amount

  def get_name(self):
    print(f"Patient Name: {self.__name}")

  def set_name(self, name):
    self.__name = name

  def get_bill_amount(self):
    print(f"Original Bill: P{(self.__bill_amount):,.2f}")

  def set_bill_amount(self, bill_amount):
    self.__bill_amount = bill_amount

  def calculate_bill(self):
    print(f"Final Bill: P{(self.__bill_amount):,.2f}")

  def display_patient_type(self):
    print("Patient Type: Regular Patient")
#senior patient class
class senior_patient(Patient):
  def __init__(self, name, bill_amount):
    super().__init__(name,bill_amount)
    self.__bill_amount = bill_amount
  def calculate_bill(self):
    print(f"Final Bill: P{(self.__bill_amount*0.8):,.2f}")
    
  def display_patient_type(self):
    print("Patient Type: Senior Citizen")
#philhealth member class
class philhealth_patient(Patient):
  def __init__(self, name, bill_amount):
    super().__init__(name,bill_amount)
    self.__bill_amount = bill_amount
  def calculate_bill(self):
    print(f"Final Bill: P{(self.__bill_amount*0.85):,.2f}")

  def display_patient_type(self):
    print("Patient Type: PhilHealth Member")
#output
patients = [Patient("Juan",15000.00),senior_patient("Jose",15000.00),philhealth_patient("John",15000.00)]
print("Hospital Billing System\n----------------------------")
for patient in patients:
  patient.get_name()
  patient.display_patient_type()
  patient.get_bill_amount()
  patient.calculate_bill()
  print("")
