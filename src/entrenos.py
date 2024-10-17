from collections import namedtuple
import csv
from datetime import datetime

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(csv_filename: str) -> list[Entreno]:
    entrenos_list = []
    with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            entrenos_list.append(Entreno(tipo=row[0],
                                         fechahora=datetime.strptime(row[1], '%d/%m/%Y %H:%M'),
                                         ubicacion=row[2],
                                         duracion=int(row[3]),
                                         calorias=int(row[4]),
                                         distancia=row[5],
                                         frecuencia=row[6],
                                         compartido=bool(row[7]))
                                )

    return sorted(entrenos_list)


def tipos_entreno(entrenos: list[Entreno]) -> list:
    entrenamientos_set = set()

    for entreno in entrenos:
        entrenamientos_set.add(entreno.tipo)

    return list(entrenamientos_set)


def entrenos_duracion_superior(entrenos: list[Entreno], d: int) -> list[Entreno]:
    entrenos_list = []

    for entreno in entrenos:
        if entreno.duracion > d:
            entrenos_list.append(entreno)

    return entrenos_list


def suma_calorias(entrenos: list[Entreno], f_inicio: str, f_fin: datetime.date) -> int:
    final_sum = 0

    try:
        f_inicio_datetime = datetime.strptime(f_inicio, '%d/%m/%Y')
        f_fin_datetime = datetime.strptime(f_fin, '%d/%m/%Y')
    except ValueError:
        print("There is a problem with f_inicio, f_fin")
    finally:
        if f_inicio_datetime > f_fin_datetime:
            raise ValueError("Begin date is bigger than final date")

        for entreno in entrenos:
            if f_inicio_datetime < entreno.fechahora < f_fin_datetime:
                final_sum += entreno.calorias

        return final_sum


print(suma_calorias(lee_entrenos('/Users/mac/US-python/Entrenos-US/data/entrenos.csv'), '5/4/2019', '27/12/2019'))