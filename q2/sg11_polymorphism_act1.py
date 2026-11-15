#Code
class Patient: #Parent Class
    def __init__ (self, name, bill_amount): #Defines and initializes the attributes name and bill_amount.
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self): #Gets name
        return self.name
    
    def get_bill_amount(self): #Gets the bill_amount
        return self.bill_amount
    
    def set_name(self, name): #Sets name
        self.name = name
    
    def set_bill_amount(self, bill_amount): #Sets bill_amount
        self.bill_amount = bill_amount
    
    def calculate_bill(self): #Calculates bill via bill_amount
        return self.bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient") #Identifies the patient as a Regular Patient


class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount) #Ensures that the child class SeniorPatient inherits the attributes without duplicating code
      
    def calculate_bill(self): #Calculates bill with a discount of 20%
        return self.get_bill_amount() * 0.80 #bill_amount is multiplied by 0.80 because the patient still has to pay the remaining 80% of the original price

    def display_patient_type(self):
        print("Patient Type: Senior Citizen") #Identifies the patient as a Senior Citizen


class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount) #Ensures that the child class PhilHealthPatient inherits the attributes without duplicating code
      
    def calculate_bill(self): #Calculates bill with a discount of 15%
        return self.get_bill_amount() * 0.85 #bill_amount is multiplied by 0.85 because the patient still has to pay the remaining 85% of the original price

    def display_patient_type(self):
        print("Patient Type: PhilHealth Patient") #Identifies the patient as a PhilHealth Patient

#Objects
patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = SeniorPatient("Maria Santos", 15000)
patient3 = PhilHealthPatient("Pedro Reyes", 15000)
patients = [patient1, patient2, patient3] #Lists the objects as patients

print("Hospital Billing System")
print("-------------------------")

for patient in patients:
  print(f"Patient Name: {patient.get_name()} ") #Prints patient's name
  
  patient.display_patient_type() #Displays patient type according to the class

  print(f"Original Bill: ₱{patient.get_bill_amount():.2f}") #Displays the patient's original bill without any discounts
  
  print(f"Final Bill: ₱{patient.calculate_bill():.2f}") #Displays the patient's final bill with discounts (regular patients retain their original bill)

  print("-------------------------")
    