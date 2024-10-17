from entrenos import *

csv_path = '/Users/mac/US-python/Entrenos-US/data/entrenos.csv'
ds = [10, 20 , 25, 90, 1000, 43, 23, 19, 28]
dates = {'5/4/2019': '27/12/2019', '5/5/2019': '27/10/2019', '5/2/2019': '10/5/2025', '23/1/2020': '27/12/2024'}

def main():
    print('1) Intentamos ejecutar funcion tipos_entreno...')
    tipos_entreno(lee_entrenos('/Users/mac/US-python/Entrenos-US/data/entrenos.csv'))
    print('Esta bien !\n')

    print('2) Intentamos ejecutar funcion entrenos_duracion_superior...')
    for d in ds:
        entrenos_duracion_superior(lee_entrenos('/Users/mac/US-python/Entrenos-US/data/entrenos.csv'), d)
    print('Esta bien !\n')

    print('3) Intentamos ejecutar funcion entrenos_duracion_superior...')
    for d in ds:
        entrenos_duracion_superior(lee_entrenos('/Users/mac/US-python/Entrenos-US/data/entrenos.csv'), d)
    print('Esta bien !\n')

    print('4) Intentamos ejecutar funcion entrenos_duracion_superior...')
    for date_i, date_f in dates.keys, dates.items:
        entrenos_duracion_superior(lee_entrenos('/Users/mac/US-python/Entrenos-US/data/entrenos.csv'), date_i, date_f)
    print('Esta bien !\n')

if __name__ == '__main__':
    main()
