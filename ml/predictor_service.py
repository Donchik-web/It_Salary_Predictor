import pandas as pd
import numpy as np

from ml.models_loader import tfidf, linear_model, columns
from ml.features import (exp_mapping, format_mapping, level_it_skills, categorize_role, regroup_role, str_to_list,
                         has_any_lang, group_mapping, count_skills, high_skill_counts, skills_vector,
                         clean_detailed_info, lemmatize_text, remove_stopwords)


def vacancy_dict_to_dataframe(vacancy_info: dict):
    """Основная функция по преобразованию входящей строки в df для применения моделей"""
    test_df = pd.DataFrame([vacancy_info])

    test_df['Exp_Label'] = test_df['experience'].map(exp_mapping)
    test_df['Format_Label'] = test_df['work_format'].map(format_mapping)

    test_df['Is_Full_Time'] = (test_df['common_employment'] == 'Полная занятость').astype(int)
    test_df['Is_Part_Time'] = (test_df['common_employment'] == 'Частичная занятость').astype(int)

    test_df['Is_Classic_Schedule'] = (test_df['work_schedule'] == 'Классический (5/2)').astype(int)

    test_df['Classic_Schedule_with_Other_Hours'] = ((test_df['work_schedule'] == 'Классический (5/2)') & (test_df['work_hours'] == 'Другие')).astype(int)

    test_df['Is_Flexible_Hours'] = (test_df['work_hours'] == 'По договоренности').astype(int)
    test_df['Is_8_Hours'] = (test_df['work_hours'] == '8 часов').astype(int)

    test_df['Medium_Exp_with_8_Hours'] = ((test_df['work_hours'] == '8 часов') & (test_df['experience'] == '3-6 лет')).astype(int)
    test_df['Low_Exp_with_8_Hours'] = ((test_df['work_hours'] == '8 часов') & (test_df['experience'] == '1-3 года')).astype(int)
    test_df['Zero_Exp_with_8_Hours'] = ((test_df['work_hours'] == '8 часов') & (test_df['experience'] == 'Нет опыта')).astype(int)

    test_df['Remote_Senior'] = ((test_df['work_format'] == 'Удалённо') & (test_df['experience'] == '6+ лет')).astype(int)
    test_df['Remote_Middle'] = ((test_df['work_format'] == 'Удалённо') & (test_df['experience'] == '3-6 лет')).astype(int)
    test_df['Office_Junior'] = ((test_df['work_format'] == 'Офис') & (test_df['experience'] == '1-3 года')).astype(int)

    test_df['Senior_Fulltime'] = ((test_df['experience'] == '6+ лет') & (test_df['common_employment'] == 'Полная занятость')).astype(int)

    test_df['Office_Fulltime'] = ((test_df['work_format'] == 'Офис') & (test_df['common_employment'] == 'Полная занятость')).astype(int)

    test_df['Classic_Remote'] = ((test_df['work_schedule'] == 'Классический (5/2)') & (test_df['work_format'] == 'Удалённо')).astype(int)

    test_df['Hours_8_Hybrid'] = ((test_df['work_hours'] == '8 часов') & (test_df['work_format'] == 'Гибрид')).astype(int)
    test_df['Hours_12_Office'] = ((test_df['work_hours'] == '12 часов') & (test_df['work_format'] == 'Офис')).astype(int)

    test_df['Is_Moscow'] = (test_df['city'] == 'Moscow').astype(int)
    test_df['Is_Kazan_SPB'] = (test_df['city'].isin(['Kazan', 'SPB'])).astype(int)
    test_df['Is_Million_city'] = (test_df['city'].isin(['Ekaterinburg', 'Novosibirsk', 'Krasnodar', 'Ufa', 'Volgograd'])).astype(int)
    test_df['Other_City'] = (~test_df['city'].isin(['Moscow', 'Kazan', 'SPB', 'Ekaterinburg', 'Novosibirsk', 'Krasnodar', 'Ufa', 'Volgograd'])).astype(int)

    test_df.drop('address', axis=1, inplace=True)

    test_df['Kazan_Remote'] = ((test_df['city'] == 'Kazan') & (test_df['work_format'] == 'Удалённо')).astype(int)

    test_df['Moscow_Remote'] = ((test_df['city'] == 'Moscow') & (test_df['work_format'] == 'Удалённо')).astype(int)

    test_df['SmallCity_Office'] = ((test_df['Other_City'] == 1) & (test_df['work_format'] == 'Офис')).astype(int)

    test_df['Level_It_Skills'] = test_df['title'].apply(level_it_skills)

    test_df['Role_Category'] = test_df['title'].apply(categorize_role)

    test_df['Role_Group'] = test_df['Role_Category'].apply(regroup_role)

    test_df['Role_Level'] = test_df['Role_Group'].map(group_mapping)

    test_df.drop('Role_Category', axis=1, inplace=True)

    test_df['Other_Office'] = ((test_df['Role_Group'] == 'Other') & (test_df['work_format'] == 'Офис')).astype(int)

    test_df.drop('name_company', axis=1, inplace=True)

    test_df['Payment_Monthly'] = (test_df['count_payments'] == 'Раз в месяц').astype(int)

    test_df.drop(['Role_Group', 'count_payments'], axis=1, inplace=True)

    test_df['skills'] = test_df['skills'].apply(str_to_list)

    test_df['Has_Program_Lang'] = test_df['skills'].apply(has_any_lang).astype(int)

    test_df['Skills_Count'] = test_df['skills'].apply(count_skills)

    test_df['Is_High_Skills'] = test_df['Skills_Count'].isin(high_skill_counts).astype(int)

    test_vectors = [skills_vector(skills) for skills in test_df['skills']]

    test_vectors_df = pd.DataFrame(
        test_vectors,
        columns=[f'Skill_Vector_{i}' for i in range(100)],
        index=test_df.index
    )

    test_df = pd.concat([test_df, test_vectors_df], axis=1)

    test_df['detailed_information'] = test_df['detailed_information'].apply(clean_detailed_info)

    test_df['detailed_information'] = test_df['detailed_information'].apply(lemmatize_text)

    test_df['detailed_information'] = test_df['detailed_information'].apply(remove_stopwords)

    tfidf_matrix_val = tfidf.transform(test_df['detailed_information'])

    tfidf_df_test = pd.DataFrame(
        tfidf_matrix_val.toarray(),
        columns=[f"tfidf_{col}" for col in tfidf.get_feature_names_out()],
        index=test_df.index
    )

    test_df = pd.concat([test_df, tfidf_df_test], axis=1)

    return test_df


def predict_salary(X_test) -> float:
    """Вызов модели по предсказанию з/п"""
    numeric_cols = X_test.select_dtypes(include=['int64', 'float64']).columns.tolist()
    X_test_clean = X_test[numeric_cols]

    X_test_ordered = X_test_clean[columns] # последовательность колонок

    y_prediction_log = linear_model.predict(X_test_ordered)
    y_prediction = np.expm1(y_prediction_log)

    salary = round(float(y_prediction[0]), 0)
    print(f"Примерная зарплата по требованиям для вакансии - {salary} ₽")

    return salary
