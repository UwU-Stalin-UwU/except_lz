#Shurupovert

import pandas as pd

class Dataframe:           #class to use
    def __init__(self, filename):
        self.filename = filename
        self.df = pd.read_csv(self.filename)  #reading from csv

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
    filename = "program_files/files_in/var4.csv"
    dataframes = Dataframe(filename)
    del_str = dataframes.dividing_df()
    print(del_str, ' lines deleted')

if __name__ == "__main__":
    main()