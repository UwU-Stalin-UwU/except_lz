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
            raise SystemExit()
        
    def __neg__(self):                        #remaking func
        return self.df.drop_duplicates()
    
    def dividing_df(self):                    #func to divide into 2 dataframes
        new_df = Dataframe(self.filename)
        new_df = -new_df
        df_cash = new_df[new_df['Вид расчета'] == 'наличный']
        df_no_cash = new_df[new_df['Вид расчета'] == 'безналичный']
        del_str = 100000 - len(df_cash) - len(df_no_cash)
        df_cash.to_csv('files_out/df_cash.csv')
        df_no_cash.to_csv('files_out/df_no_cash.csv')
        return(del_str)

def main():
    filename = input("Please, enter name of your file: ")            
    df = Dataframe(filename)
    del_str = df.dividing_df()
    print(del_str, ' lines deleted')
    

if __name__ == "__main__":
    main()