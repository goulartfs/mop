from domain.entities.medicine import Medicine
from domain.entities.pharmacy import Pharmacy


class RemoveMedicine:
    """
    Caso de uso: Adicionar novo remédio

    História do usuário: Como administrador, gostaria de adicionar um novo medicamento a uma determinada farmácia
    """
    def execute(self, medicine_to_remove: Medicine, pharmacy: Pharmacy):
        raise NotImplementedError()