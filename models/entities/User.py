from random import sample

class User:
    def __init__(self, username, fullname) -> None:
        self.username = username
        self.fullname = fullname
        self.password = self.generatePassword(12);
        
    
    def generatePassword(self, numero:int) -> str:
        minus = "abcdefghijklmnopqrstuvwxyz"
        mayus = minus.upper()
        simbolos = "[]»¡!#$%/&*()_+Ç«¢∞\|¿?<>£≠-_|¶~"
        numeros = "0123456789"
        template = minus + mayus + simbolos + numeros
        password = "".join(sample(template, 12))
        return password;

