# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 1

"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы: 

1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.

2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

3. Посчитайте долю погибших на параходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром survival;
2) полом человека и параметром survival;
3) классом, в котором пассажир ехал, и параметром survival.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?

"""

import pandas  # импортирование библиотеки для считывания данных
import numpy as np

# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pandas.read_csv('train.csv', index_col="PassengerId")


# TODO #1
def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """
    n_male, n_female = 0, 0
    all_people = data['Sex'].value_counts()
    n_male, n_female = all_people['male'], all_people['female']
    print("1. Мужчины и женщины на корабле:", n_male, n_female)
    return n_male, n_female

get_sex_distrib(data)


# TODO #2
def get_port_distrib(data):
    """  
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """
    port_S, port_C, port_Q = 0, 0, 0
    all_people = data['Embarked'].value_counts()
    port_S, port_C, port_Q = all_people['S'], all_people['C'], all_people['Q']
    print("2. Количество людей из каждого порта: ", port_S, port_C, port_Q)
    return port_S, port_C, port_Q

get_port_distrib(data)


# TODO #3
def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """
    n_died, perc_died = 0, 0
    all_dead_people = data['Survived'].value_counts()
    n_died = all_dead_people[0]
    perc_ofalldead = data['Survived'].value_counts(normalize=True) * 100
    perc_died = perc_ofalldead[0]
    print("3. Сколько умерло и процент умерших: ", n_died, perc_died)
    return n_died, perc_died

get_surv_percent(data)

# TODO #4
def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?    
    """
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = 0, 0, 0
    all_class_people = data['Pclass'].value_counts(normalize=True)
    n_pas_f_cl = all_class_people[1]
    n_pas_s_cl = all_class_people[2]
    n_pas_t_cl = all_class_people[3]
    print("4. Доли пассажиров каждого класса: ", n_pas_f_cl, n_pas_s_cl, n_pas_t_cl)
    return n_pas_f_cl, n_pas_s_cl, n_pas_t_cl
get_class_distrib(data)

# TODO #5
def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """
    from scipy import stats

    corr_val = -1
    sibsp = data['SibSp']
    parch = data['Parch']
    corr_val = stats.pearsonr(sibsp, parch)
    print("5. Корреляция Пирсона между супругами и детьми: ", corr_val)
    return corr_val

find_corr_sibsp_parch(data)

# TODO #6-1
def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - возрастом и параметром survival;

    """
    from scipy import stats

    corr_val = -1
    #surv = data['Survived']
    #age = data['Age']
    #corr_val = stats.pearsonr(surv, age)
    #print(corr_val)
    return corr_val

find_corr_age_survival(data)

# TODO #6-2
def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - полом человека и параметром survival;
    """
    from scipy import stats

    corr_val = -1
    #sex = data['Sex'] поменять строки на флоат  
    #surv = data['Survived']
    #corr_val = stats.pearsonr(sex, surv)
    #print(corr_val)
    return corr_val
find_corr_sex_survival(data)

# TODO #6-3
def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - классом, в котором пассажир ехал, и параметром survival.
    """
    from scipy import stats
    corr_val = -1
    class_p = data['Pclass']
    surv = data['Survived']
    corr_val = stats.pearsonr(class_p, surv)
    print("6.3. Корреляция Пирсона между классом и выжившими: ", corr_val)
    return corr_val

find_corr_class_survival(data)

# TODO #7
def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """

    mean_age, median = None, None
    mean_age = data['Age'].mean()
    median = data['Age'].median()
    print("7. Средний возраст и медиана: ", mean_age, median)
    return mean_age, median

find_pass_mean_median(data)

# TODO #8
def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """

    mean_price, median = None, None
    mean_price = data['Fare'].mean()
    median = data['Fare'].median()
    print("8. Средняя цена и медиана: ", mean_price, median)
    return mean_price, median

find_ticket_mean_median(data)

# TODO #9
def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """
    name = ''
    print(name)
    return name

find_popular_name(data)

# TODO #10
def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """


# ------------------------------

# Реализуем вычисление количества пассажиров на параходе и опишем предварительные действия с данными (считывание)

# После загрузки данных с помощью метода read_csv и индексации его по первому столбцу данных (PassangerId) становится доступно выборка данных по индексу. 
# С помощью запроса ниже мы можем получить имя сотого пассажира
print((data.iloc[100]['Name']))


def get_number_of_pass(data_file):
    """
        Подсчет количества пассажиров. 
        data_file - str
        В качестве аргумента удобнее всего использовать строковую переменную, куда будет передаваться название файла (т. к. далее, возможно, потребуется подсчитать параметры для другого набора данных test.csv)
    """
    male_int, female_int = 0, 0
    # считывание и обработка данных
    data = pandas.read_csv(data_file, index_col="PassengerId")

    # считать данных из столбца возможно с помощью метода value_counts()
    res = data['Sex'].value_counts()
    # res будет содержать ассоциативный массив, ключами в котором являются значения столбца sex, а целочисленные значениями - количества пассажиров обоих полов
    male_int, female_int = res['male'], res['female']
    return male_int, female_int


def test_get_number_of_pass():
    assert get_number_of_pass('train.csv') == (577,314), " Количество мужчин и женщин на Титанике"

# аналогично протестировать остальные функции


# пример использования коэфициента пирсона 
from scipy import stats
a = np.array(range(1, 10+1, 1))
b = np.array(list(range(5,0, -1))*2)
print(stats.pearsonr(a,b))
popular_male_name, popular_female_name = "", ""
