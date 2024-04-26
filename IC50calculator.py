import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.title('pIC50 calculator')

st.write('### Input Data')
IC50val = st.number_input('IC50 (nM)', min_value = 1.0)

#Calculate pIC50
pIC50val = float(-np.log10(0.000000001*IC50val))
pIC50val = round(pIC50val, 2)

st.write('### Your pIC50 value')
#Display the pIC50
col1, col2 = st.columns(2)
col1.metric(label = 'IC50 (nM)', value = f'{IC50val:,.2f}')
col2.metric(label = 'pIC50', value = f'{pIC50val:,.2f}')
