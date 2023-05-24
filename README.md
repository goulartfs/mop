# M.O.P - My own pharmacy

With this project I hope to easily manage the medications that my family and I need.


This project is also an object-oriented programming exercise seeking to follow Domain Driven Development, Test Driven Development, Clean Architecture and Clean Code concepts.

## Project Structure

> Should I use a service layer or make my
> application depend directly on the use case?
> It makes a difference?

- **app** - Application main directory. Concrete implementations.

- **domain** - Domain layer, with entities and business rules. Abstract implementations.

- **infrastructure** - Technical implementations and infrastructure details.

- **tests** - testing module, here we concentrate unit and functional tests, etc.


## Mapped Entities

- **Medicine** - represents a medicine

- **Patient** - represents a patient. A patient can have one or more medical prescriptions

- **Pharmacy** - represents a pharmacy. In our case, a personal stock of medicines that we have in our house, work, etc. A pharmacy may have none or many drugs in stock.

# User's Stories

- As an administrator, I would like to list all drugs in my pharmacy
- As an administrator, I would like to add a new medicine to my pharmacy
- As an administrator, I would like to remove a medicine in my pharmacy
- As an administrator, I would like to update the price of a drug in my pharmacy
- As an administrator, I would like to update the data for a drug in my pharmacy
- As an administrator, I would like to register a patient in my pharmacy
- As an administrator, I would like to register a medical prescription for a patient
- As an administrator, I would like to list the remaining stock of drugs
- As an administrator, I would like to calculate the total cost amount of a patient's prescription