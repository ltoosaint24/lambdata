import pandas as pd
import numpy as numy
import random
import scrapeasy



def randomizr(df,seed):
  Xcv= df.copy()
  col= df.columns.values.tolist()
  df_trans =df.T
  df_trans.index = df_trans.columns.values
  df_trans.columns = col
  return df_trans
  
  #following function will take an input of state and match in list dictionary to output the abbreviation
def abbr_2_st(state_series, abbr_2_st=True):
  state_dict = {'Alabama':	'AL','Alaska':	'AK','Arizona':	'AZ','Arkansas': 'AR','California':	'CA','Colorado':	'CO','Connecticut':	'CT','Delaware':	'DE','Florida':	'FL','Georgia':	'GA',
'Hawaii':	'HI','Idaho':	'ID','Illinois':	'IL','Indiana':	'IN','Iowa':	'IA','Kansas':	'KS','Kentucky':'KY','Louisiana'	:'LA','Maine':'ME','Maryland':'MD','Massachusetts':'MA',
'Michigan':	'MI','Minnesota':	'MN','Mississippi':'MS','Missouri':'MO','Montana':'MT','Nebraska':'NE','Nevada'	:'NV','New Hampshire'	:'NH','New Jersey':	'NJ','New Mexico':	'NM',
'New York':	'NY','North Carolina'	:'NC','North Dakota':	'ND','Ohio'	:'OH','Oklahoma'	:'OK','Oregon':	'OR','Pennsylvania':	'PA','Rhode Island':	'RI','South Carolina':	'SC','South Dakota':	'SD',
'Tennessee':	'TN','Texas':	'TX',
'Utah':	'UT','Vermont':	'VT','Virginia':'VA','Washington':'WA','West Virginia':	'WV','Wisconsin':	'WI','Wyoming':'WY'}
  
  us_territories ={'American Samoa':	'AS','District of Columbia':	'DC','Guam':	'GU',
'Marshall Islands':	'MH','Northern Mariana Island':'MP','Puerto Rico':	'PR','Virgin Islands':	'VI'}
    abbrva =[]
    for xc in state_series:
      if xc  in state_dict:
        abbrva.append(state_dict[state_series])
      else:
        if xc in us_terriories:
          print("This not a state but a U.S. territory", xc)
          abbrva.append(us_territories[xc])
        else:
          print("Not a U.S state or territory")
  return abbrva
