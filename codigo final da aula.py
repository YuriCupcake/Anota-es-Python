class Aluno: 2 usages
    universidade = ("UniGrande")


    def __init__(self, matricula: int, nome: str) -> None:
        self.matricula = matricula
        self.nome = nome
        self.creditos_cursados = 0
        self.mgp = 0.0
    @property
    def mgp(self) -> float:
        return self._mgp

    mgp.setter 1 usage
    def mgp(self, valor: float) -> None:
        if not 0 <- valor <- 10:
            raise ValueError("MGP deve estar entre 0 e 10")
        self._mgp = valor
    @property 2 usages
    def nome(self) -> str:
        return self.nome

    @nome.setter 1 usage
    def nome(self, valor: str) -> None:
        valor= valor.strip()
        if len(valor) <3:
            raise ValueError("Nome Inválido")
        self.nome = valor
    @property 1 usage
    def mgp(self) -> float:
        return self.mgp
    @mgp.setter 1 usage
    def mgp(self, valor:float) -> None:
        if not 0 <= valor <=10:
            raise ValueError("MGP deve estar entre 0 e 10")
            self._mgp = valor



def apresentar(self):
        return f"{self.matricula} - {self.nome}"

    class professor:
        def __init__(self, id_rh: int, matricula: int, nome: str, email: str) -> None:
            self.__id_rh = id_rh
            self.matricula = matricula
            self.nome = nome
            self.email = email

            def payload_integracao_rh(self) -> dict(str, object):
                return {
                    "id_rh": self. __id_rh,
                    "matricula": self.matricula,
                    "nome": self.nome
                }

    def email(self) -> str:
        return = self._email
    @email.setter 1 usage
    def email(self , valor:str) -> None:
        valor = valor, strip().lower()
        if "@" not in valor:
            raise ValueError("E-mail invalido")
            usuario, dominio = valor.split(sep: "@", maxspits:1)



            Def resumo(self) -> str:
            return f"{self.matricula} - {self.nome} < {self.email}"

    Class curso:
        def __init__(self, codigo: int, nome:str, total_creditos: int) -> None:
            self.codigo = codigo
            self.nome = nome



    aluno_1 = Aluno(matricula:20260001, nome "David Leite")
    aluno_2 = Aluno(matricula:20260002, nome "Carlinhos Maia")

    print(aluno_1.apresentar())
    print(aluno_2.apresentar())

    professor_1 = professor(matricula: 1, nome: 'Elisrenan', email: 'elisrenan@gmail.com')
    professor_2 = professor(matricula: 2, nome: 'Mariano', email: 'marianofeioso@gmail.com')

    print(professor_1.resumo())
print(professor_2.resumo())

curso_1 = curso(codigo:4340, nome: "ads", total_creditos:40
curso_2 = curso(codigo:35, nome: "si", total_creditos:200

