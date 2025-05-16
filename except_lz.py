import pandas as pd


class DataFrameStructureError(Exception):
    #print("Wrong structure of DataFrame")
    pass


class TypeError(Exception):
    pass


class Dataframe:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.df = pd.read_csv(filename)
            #print(self.df)
        except FileNotFoundError:
            print('Возникла следующая ошибка: Отсутствует файл: ', self.filename)
            raise SystemExit()
        except pd.errors.EmptyDataError:
            print('Возникла следующая ошибка: Пустой файл')
            raise SystemExit()
        except pd.errors.ParserError:
            print('Возникла следующая ошибка: Колонки странно себя ведут')
            raise SystemExit()
        try:
            self.column_list_from_file = self.df.columns.to_list()
            self.df_original = pd.read_csv('var4_original.csv')
            self.column_list_main = self.df_original.columns.to_list()
            #print(self.column_list_from_file)
            #print(self.column_list_main)
            if self.column_list_from_file != self.column_list_main:
                raise DataFrameStructureError('Wrong structure, you goddamn piece of shit')
        except DataFrameStructureError:
            print('Возникла следующая ошибка: Названия столбцов не совпадают: \n' \
            'Ожидаемые: ', self.column_list_main,
            '\nПолученные: ', self.column_list_from_file)
            raise SystemExit()
        try:
            self.file_types = self.df.dtypes
            self.file_types = str(self.file_types)
            self.main_types = self.df_original.dtypes
            self.main_types = str(self.main_types)
            if self.file_types != self.main_types:
                raise TypeError('Неверные типы данных')
            else:
                print('Чтение файла завершено успешно')
        except TypeError:
            print('Возникла следующая ошибка: Несовпадение типов данных с ожидаемыми: \n' \
            'Ожидалось: ', self.main_types,
            '\nПолучено: ', self.file_types)

def main():
    filename = input("Please, enter name of your file: ")            
    df = Dataframe(filename)

if __name__ == "__main__":
    main()