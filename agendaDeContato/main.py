'''This exercise asks you to create a PhoneBook class that stores names and phone numbers and allows the operations of look-up, insertion and deletion.

You are given a LinkedList class that maintains a traversable linked list of strings. You will be using this to create a PhoneBook. You would want to create two linked lists in a PhoneBook, one for storing names and one for storing phone numbers. Make sure that the two lists are traversed in lock step so that you get the corresponding names and numbers.

Requirements for the PhoneBook class

Constructor:

PhoneBook() - creates a new empty phone-book.
Instance methods:

void insert(String name, String number)
Inserts a new entry in the phone-book. The entry can be inserted anywhere, but it is advisable to insert it at the end, in order to avoid confusion to the user.
void lookUp(String prefix, StringBuffer name, StringBuffer number) throws NotFoundException
Looks up the entry of a name starts with the given string prefix. If no such entry exists, throws the exception. If an entry is found, appends the name of the entry to the StringBuffer name and the phone number of the entry to the StringBuffer number.
void repeatLookUp(String prefix, StringBuffer name, StringBuffer number) throws NotFoundException
Like lookUp, but continues search for another entry that begins with the String prefix.
void delete()
Deletes the entry last looked up.'''

from classes.funcionalidade import theFunctions

agenda1 = theFunctions()
agenda1.addContact('Ricardo', '951540122')
agenda1.addContact('Wilson', '1951540122')
agenda1.addContact('Pereira', '12345678')
agenda1.checkAllContacts()
agenda1.checkContact('951540122')
agenda1.checkContact('Wilson')
agenda1.checkContact('Carlos')
agenda1.checkContact('Carlos')
agenda1.checkContact('Pereira')
agenda1.checkContact('Carlos')
agenda1.ligar('Ricardo')
agenda1.ligar('Wilson')
agenda1.ligar('Wilson')
agenda1.ligar('Wilson')
agenda1.desligar()
agenda1.ligar('Wilson')
agenda1.desligar()
agenda1.desligar()
agenda1.desligar()
agenda1.ligar('Ricardo')
agenda1.addContact('Pereira', '12345678')
agenda1.checkAllContacts()