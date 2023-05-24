# :pill: M.O.P - My own pharmacy :pill:

With this project I hope to easily manage the medications that my family and I need.

This project is also an object-oriented programming exercise seeking to follow Domain Driven Development, Test Driven
Development, Clean Architecture and Clean Code concepts.

## Running

*To run tests*

```
python3 -m pytest
```

## Project Structure

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

## Mapped Entities

- **Medicine** - represents a medicine

- **Patient** - represents a patient. A patient can have one or more medical prescriptions

- **Pharmacy** - represents a pharmacy. In our case, a personal stock of medicines that we have in our house, work, etc.
  A pharmacy may have none or many drugs in stock.

## User's Stories

**Pharmacy**

- As an administrator, I would like to add new pharmacy
  - :white_check_mark: domain.use_cases.pharmacy.add_new_pharmacy
- As an administrator, I would like to update a pharmacy
  - :white_check_mark: domain.use_cases.pharmacy.update_pharmacy
- As an administrator, I would like to update a pharmacy
  - :white_check_mark: domain.use_cases.pharmacy.remove_pharmacy

**Medicine**

- As an administrator, I would like to list all medicines in my pharmacy
- As an administrator, I would like to add a new medicine to my pharmacy
  - :white_check_mark: domain.use_cases.medicine.add_new_medicine
- As an administrator, I would like to remove a medicine in my pharmacy
  - :white_check_mark: domain.use_cases.medicine.remove_medicine
- As an administrator, I would like to update medicine in my pharmacy
  - :white_check_mark: domain.use_cases.medicine.update_medicine
- As an administrator, I would like to list the remaining stock of a medicine in my pharmacy

**Patient**

- As an administrator, I would like to register a new patient in my pharmacy
  - :white_check_mark: domain.use_cases.patient.add_new_patient

**Prescription**

- As an administrator, I would like to register a medical prescription for a patient in my pharmacy
- As an administrator, I would like to calculate the total cost amount of a patient's prescription