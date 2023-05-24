from domain.use_cases.caso_de_uso import CasoDeUso
from domain.entities.medicine import Medicine
from domain.entities.pharmacy import Pharmacy


class AdicionarNovoRemedioNaFarmacia(CasoDeUso):
    """
    Caso de uso: Adicionar novo remédio

    História do usuário: Como administrador, gostaria de adicionar um novo medicamento a uma determinada farmácia
    """
    def executar(self, remedio: Medicine, farmacia: Pharmacy):
        super().execute()