class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def get_client(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'

    def get_client_corp(self):
        return f'{self.name} {self.surname}. {self.city}.'


client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Илья', 'Дядович', 'Минск', 50000)
client_3 = Client('Анастасия', 'Доропиевич', 'Минск', 900000)

client_list = [client_1, client_2, client_3]
for i in client_list:
    print(i.get_client())
print()
guest_list = client_list.copy()
for i in guest_list:
    print(i.get_client_corp())
