from src.models.store import Store
from src.models.user import User
from src.service.service_user import ServiceUser

store = Store()
print(store.bd)

print("#primeiro teste")
name = "Laura"
job = "QA"

user = User(name=name, job=job)
#print(user.name)
#print(user.job)

service = ServiceUser()
resultado = service.add_user(name = name, job = job)
print(service.store.bd[0].name)
print(service.store.bd[0].job)
print(resultado)

print("#segundo teste")
name = None
job = "QA"

service = ServiceUser()
resultado = service.add_user(name = name, job = job)
print(service.store.bd)
print(resultado)

