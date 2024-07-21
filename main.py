'''
Зараз на тебе чекає домашнє завдання, завдяки якому ти навчишся наступним корисним навичкам:

• Основи об'єктно-орієнтованого програмування (ООП)
• Робота з класами та об'єктами
• Робота з методами класу
'''

from collections import UserDict

def Errors(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("The phone number is not correct") 
        except IndexError:
            print("There is no such phone number in the list") 
    return inner

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    # реалізація класу

    @Errors
    def is_validate_phone(self) -> bool:
        is_num = False
        if not len(self.value) == 10 or not self.value.isdigit():
            raise ValueError()
        else:
            is_num = True
        return is_num

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone):
        phone = Phone(phone)
        if phone.is_validate_phone():
            self.phones.append(phone)

    def remove_phone(self, phone):
        phone_v = Phone(phone)
        if phone_v.is_validate_phone:
            for iphone in self.phones:
                if iphone.value == phone:
                    self.phones.remove(iphone)

    @Errors
    def edit_phone(self, old_phone, new_phone):
        isedit = False
        phone_new = Phone(new_phone)
        phone_old = Phone(new_phone)
        if phone_new.is_validate_phone or phone_old.is_validate_phone:
            for iphone in self.phones:
                if iphone.value == old_phone:
                    iphone.value = new_phone
                    isedit = True
                    break
        
        if not isedit: raise IndexError()

    def find_phone(self, phone):
        phone_v = Phone(phone)
        if phone_v.is_validate_phone:
            for iphone in self.phones:
                if iphone.value == phone:
                    iphone.value = phone
                    return iphone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        if name in self.data:
            return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self) -> str:
        text = "{:^33}\n".format('Address Book')
        text += "{:^39}\n".format('-'*39)
        base_format = '{:<13} | {:<11}'
        text += f"{base_format.format('Contact name', 'Phones')}\n"
        text += f"{base_format.format('-'*13 , '-'*23)}\n"

        for idata in self.data:
            icont, iitem = idata, '; '.join(p.value for p in self.data[idata].phones)
            text += f"{base_format.format(icont,  iitem)}\n"
        return text


# ----------------------------------------------------------------------------------
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)


# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# # Виведення всіх записів у книзі
    
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")

