from domain.entities.medicine import Medicine
from domain.repositories.medicine_repository import MedicineRepository as Repository
import mysql.connector
from typing import List


class Conexao:
    def __init__(self, host, user, password, database):
        self.conexao = mysql.connector.connect(
            host= host,
            user= user,
            password= password,
            database= database
        )


class MedicineRepository(Repository):
    def __init__(self, conexao: Conexao ) -> None:
        self.conexao = conexao

    def insert(self, medicine: Medicine) -> None:
        pass

    def delete(self, medicine: Medicine) -> None:
        pass

    def list(self) -> List[Medicine]:
        pass
