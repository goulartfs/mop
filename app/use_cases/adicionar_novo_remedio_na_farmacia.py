from domain.use_cases.adicionar_novo_remedio_na_farmacia import AdicionarNovoRemedioNaFarmacia as CasoDeUso
from app.entities.medicine import Medicine
from app.entities.pharmacy import Pharmacy


class AdicionarNovoRemedioNaFarmacia(CasoDeUso):

    def executar(self, remedio: Medicine, farmacia: Pharmacy) -> None:
        farmacia.add_medicine(remedio)
