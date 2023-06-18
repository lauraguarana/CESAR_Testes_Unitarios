from src.service.service_user import ServiceUser

class TestServiceUser:

    def test_add_user_successfully(self):
        # Setup
        name_1 = "Fabricio"
        job_1 = "Eng"
        resultado_esperado = "User added"
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_1, job=job_1)

        # Avaliacao
        assert resultado_esperado == resultado


    def test_add_user_invalid_user(self):
        # Setup
        name_1 = None
        job_1 = "Eng"
        resultado_esperado = "Invalid user"
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_1, job=job_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_user_invalid_user_notString(self):
        # Setup
        name_1 = 32
        job_1 = "Eng"
        resultado_esperado = "User cannot be added"
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_1, job=job_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_user_user_duplicated(self):
        # Setup
        name_1 = "Fabricio"
        job_1 = "Eng"
        resultado_esperado = "User duplicated"
        service = ServiceUser()

        # Adicionar user
        service.add_user(name=name_1, job=job_1)

        # Chamada
        resultado = service.add_user(name=name_1, job=job_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_delete_user(self):
        # Setup
        name_1 = "Fabricio"
        job_1 = "Eng"
        resultado_esperado = "The user was removed successfully"
        service = ServiceUser()

        # Adicionar user
        service.add_user(name=name_1, job=job_1)

        # Chamada
        resultado = service.delete_user(name=name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_delete_invalid_user(self):
        # Setup
        name_1 = "Fabricio"
        job_1 = "Eng"
        resultado_esperado = "The user cannot be found"
        service = ServiceUser()

        # Adicionar user
        service.add_user(name=name_1, job=job_1)

        # Chamada
        resultado = service.delete_user(name="Laura")

        # Avaliacao
        assert resultado_esperado == resultado

    def test_update_user(self):
        # Setup
        name_1 = "Fabricio"
        job_1 = "Eng"
        resultado_esperado = "User updated"
        service = ServiceUser()

        # Adicionar user
        service.add_user(name=name_1, job=job_1)

        # Chamada
        resultado = service.update_user(name=name_1, job="SDET")

        # Avaliacao
        assert resultado_esperado == resultado

    def test_update_invalid_user(self):
        # Setup
        name_1 = "Fabricio"
        job_1 = "Eng"
        resultado_esperado = "The user cannot be found."
        service = ServiceUser()

        # Adicionar user
        service.add_user(name=name_1, job=job_1)

        # Chamada
        resultado = service.update_user(name="Laura", job=job_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_select_user(self):
        # Setup
        name_1 = "Fabricio"
        job_1 = "Eng"
        resultado_esperado = "Eng"
        service = ServiceUser()

        # Adicionar user
        service.add_user(name=name_1, job=job_1)

        # Chamada
        resultado = service.select_user(name=name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_select_invalid_user(self):
        # Setup
        name_1 = "Fabricio"
        job_1 = "Eng"
        resultado_esperado = "The user cannot be found."
        service = ServiceUser()

        # Adicionar user
        service.add_user(name=name_1, job=job_1)

        # Chamada
        resultado = service.select_user(name="Laura")

        # Avaliacao
        assert resultado_esperado == resultado