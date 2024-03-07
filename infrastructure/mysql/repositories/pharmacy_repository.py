import copy
from typing import List

from domain.entities.medicine import Medicine
from domain.entities.pharmacy import Pharmacy
from domain.repositories.pharmacy_repository import PharmacyRepository as Repository
import mysql.connector


class GeradorDeConexao:
    def __init__(self, host, user, password, database):
        self.conexao = mysql.connector.connect(
            host= host,
            user= user,
            password= password,
            database= database
        )


class PharmacyRepository(Repository):
    def __init__(self, conexao: GeradorDeConexao ):
        self.gerador_de_conexao = conexao

    def insert(self, pharmacy: Pharmacy):
        cursor = self.gerador_de_conexao.conexao.cursor()
        query = "INSERT INTO pharmacies (name) VALUES (%s)"
        valores = (pharmacy.name,)
        cursor.execute(query, valores)
        self.gerador_de_conexao.conexao.commit()
        print("Registro inserido com sucesso.")


    def delete(self, pharmacy_id: str):
        cursor = self.gerador_de_conexao.conexao.cursor()
        query = "DELETE FROM pharmacies WHERE id = %s"
        valores = (pharmacy_id)
        cursor.execute(query, valores)
        self.gerador_de_conexao.conexao.commit()
        print("Registro excluído com sucesso.")


    def list(self) -> List[Pharmacy]:
        pharmacies: List[Pharmacy] = []
        cursor = self.gerador_de_conexao.conexao.cursor()
        query = "SELECT * FROM pharmacies"
        cursor.execute(query)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
            pharmacy = Pharmacy(name=registro[1])
            pharmacy.id = registro[0]
            pharmacies.append(pharmacy)
            
        return pharmacies




    def update(self, pharmacy_id: str, updated_pharmacy: Pharmacy):
        cursor = self.gerador_de_conexao.conexao.cursor()
        query = "UPDATE pharmacies SET name = %s WHERE id = %s"
        valores = (updated_pharmacy.name, pharmacy_id)
        cursor.execute(query, valores)
        self.gerador_de_conexao.conexao.commit()
        pharmacy = self.find_by_id(pharmacy_id=pharmacy_id)
        for medicine in updated_pharmacy.medicines:
            self.add_medicine(pharmacy=pharmacy, medicine=medicine)
        print("Registro atualizado com sucesso.")


    
    def find_by_id(self, pharmacy_id: str) -> Pharmacy | None:
        cursor = self.gerador_de_conexao.conexao.cursor()
        query = "SELECT * FROM pharmacies WHERE id = %s"
        valores = (pharmacy_id,)
        cursor.execute(query, valores)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
            pharmacy = Pharmacy(name=registro[1])
            pharmacy.id = registro[0]
            pharmacy.medicines = self.list_medicine(pharmacy_id)
            return pharmacy

        return None


    def add_medicine(self, pharmacy: Pharmacy, medicine: Medicine):
        cursor = self.gerador_de_conexao.conexao.cursor()
        query = "INSERT INTO medicines (pharmacy_id, name, dosage, boxes, prescription) VALUES (%s, %s, %s, %s, %s)"
        valores = (pharmacy.id, medicine.name, medicine.dosage, medicine.boxes, medicine.prescription)
        cursor.execute(query, valores)
        self.gerador_de_conexao.conexao.commit()
        print("Registro inserido com sucesso.")


    def list_medicine(self, pharmacy_id: str) -> List[Medicine]:
        medicines: List[Medicine] = []
        cursor = self.gerador_de_conexao.conexao.cursor()
        query = "SELECT * FROM medicines WHERE pharmacy_id = %s"
        valores = (pharmacy_id,)
        cursor.execute(query, valores)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
            medicine = Medicine(registro[2], registro[3], registro[4], registro[5])
            medicines.append(medicine)
            
        return medicines
