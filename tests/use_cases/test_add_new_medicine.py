from app.use_cases.adicionar_novo_remedio_na_farmacia import AdicionarNovoRemedioNaFarmacia
from app.entities.pharmacy import Pharmacy
from app.entities.medicine import Medicine
from infrastructure.memory.repositories.medicine_repository import MedicineRepository

def test_deve_adicionar_medicamento_para_farmacia_1():
    """
    Caso de uso: Adicionar novo remédio

    História do usuário: Como administrador, gostaria de adicionar um novo medicamento a uma determinada farmácia

    Cenário 1:

    Dado "farmácia 1",
    Adiciono novo medicamento, com nome "remedio1" e dosagem "1mg"
    Espero que ao listar medicamentos da "farmácia 1"
    Retorne lista de medicamentos com 1 item
    """

    farmacia1 = Pharmacy("farmácia 1")
    remedio1 = Medicine("remedio1", "1mg")

    caso_de_uso = AdicionarNovoRemedioNaFarmacia()
    caso_de_uso.executar(
        farmacia=farmacia1,
        remedio=remedio1
    )

    assert 1 == len(farmacia1.medicines)

def test_deve_adicionar_medicamento_para_farmacia_1_e_na_farmacia_2():
    farmacia1 = Pharmacy("farmácia 1")
    farmacia2 = Pharmacy("farmácia 2")
    remedio1 = Medicine("remedio1", "1mg")
    remedio2 = Medicine("remedio2", "1mg")

    caso_de_uso = AdicionarNovoRemedioNaFarmacia()
    caso_de_uso.executar(
        farmacia=farmacia1,
        remedio=remedio1
    )

    caso_de_uso.executar(
        farmacia=farmacia2,
        remedio=remedio1
    )

    caso_de_uso.executar(
        farmacia=farmacia2,
        remedio=remedio2
    )

    assert 1 == len(farmacia1.medicines)
    assert 2 == len(farmacia2.medicines)
