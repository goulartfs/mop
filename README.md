# :pill: M.O.P - My own pharmacy :pill:

With this project I hope to easily manage the medications that my family and I need.

This project is also an object-oriented programming exercise seeking to follow Domain Driven Development, Test Driven
Development, Clean Architecture and Clean Code concepts.

## :pill: Running

*To run tests*

```
python3 -m pytest -v
```

*To run tests on VSCode*

add to your `.vscode/settings.json` this configs:

```
{
    "python.testing.pytestPath": "pytest",
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "python.testing.autoTestDiscoverOnSaveEnabled": true
}
```

## :pill: Project Structure

- **app** - Application main directory. Concrete implementations.

- **domain** - Domain layer, with entities and business rules. Abstract implementations.

- **infrastructure** - Technical implementations and infrastructure details.

- **tests** - testing module, here we concentrate unit and functional tests, etc.

### _Questions_

> #1: Should I use a service layer or make my
> application depend directly on the use case?
> It makes a difference?
>
> Answer: I have started with a service layer, then I realize
> using use cases layer makes things easier to understand,
> to read, to maintain, to extends, etc.

## :pill: Mapped Entities

- **Medicine** - represents a medicine

- **Patient** - represents a patient. A patient can have one or more medical prescriptions

- **Pharmacy** - represents a pharmacy. In our case, a personal stock of medicines that we have in our house, work, etc.
  A pharmacy may have none or many drugs in stock.

## :pill: User's Stories

**Pharmacy**

- As an administrator, I would like to add new pharmacy
    - :white_check_mark: domain.use_cases.pharmacy.insert_pharmacy
- As an administrator, I would like to update a pharmacy
    - :white_check_mark: domain.use_cases.pharmacy.update_pharmacy
- As an administrator, I would like to update a pharmacy
    - :white_check_mark: domain.use_cases.pharmacy.delete_pharmacy

**Medicine**

- As an administrator, I would like to list all medicines in my pharmacy
    - :white_check_mark: domain.use_cases.medicine.list_medicines
- As an administrator, I would like to add a new medicine to my pharmacy
    - :white_check_mark: domain.use_cases.medicine.insert_medicine
- As an administrator, I would like to remove a medicine in my pharmacy
    - :white_check_mark: domain.use_cases.medicine.delete_medicine
- As an administrator, I would like to update medicine in my pharmacy
    - :white_check_mark: domain.use_cases.medicine.update_medicine
- As an administrator, I would like to list the remaining stock of a medicine in my pharmacy

**Patient**

- As an administrator, I would like to insert a new patient in my pharmacy
    - :white_check_mark: domain.use_cases.patient.insert_patient
- As an administrator, I would like to update patient in my pharmacy
    - :white_check_mark: domain.use_cases.patient.update_patient
- As an administrator, I would like to delete a patient in my pharmacy
    - :white_check_mark: domain.use_cases.patient.delete_patient
- As an administrator, I would like to list all patients in my pharmacy
    - :white_check_mark: domain.use_cases.patient.list_patients

**Prescription**

- As an administrator, I would like to register a medical prescription for a patient in my pharmacy
- As an administrator, I would like to calculate the total cost amount of a patient's prescription