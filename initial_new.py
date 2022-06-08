import pandas as pd
import numpy as np

thyroidDF = pd.read_csv('landing/temporal/raw/thyroid.data', sep=',', header=None)

# defining dataset columns
initial_columns = ['age', 'sex', 'on_thyroxine', 'query_on_thyroxine', 'on_antithyroid_meds', 'sick',
                    'pregnant', 'thyroid_surgery', 'I131_treatment', 'query_hypothyroid', 'query_hyperthyroid', 'lithium',
                    'goitre', 'tumor', 'hypopituitary', 'psych', 'TSH_measured', 'TSH', 
                    'T3_measured', 'T3', 'TT4_measured', 'TT4', 'T4U_measured', 'T4U', 
                    'FTI_measured', 'FTI', 'TBG_measured', 'TBG', 'referral_source', 'target']

thyroidDF.columns = initial_columns

# replacing '?' values with NaN
thyroidDF.replace('?', np.nan, inplace=True)

# split 'target' and extract 'patient_id'
thyroidDF[['target', 'patient_id']] = thyroidDF['target'].str.split('[', expand=True)
# clean-up 'target' **gives weird warning**
thyroidDF['patient_id'] = thyroidDF['patient_id'].str.replace(']', '')

# export to csv in persistent landing zone
thyroidDF.to_csv('landing/persistent/thyroidDF.csv', index=False)