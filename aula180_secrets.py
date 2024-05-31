# secrets gere números aleatórios seguros
import secrets
import secrets as s
from secrets import SystemRandom as Sr

# print(secrets.digits)
# print(Sr().choices(s.ascii_letters + s.digits))

random = secrets.SystemRandom()
print(secrets.randbelow(100))
print(secrets.choice([10, 12, 12]))


