import streamlit as st
import pandas as pd

"""
# Biodata
Berikut data alamat dari 4 mahasiswa:
"""

df = pd.DataFrame({
  'Nama Mahasiswa': ['bayu','april','ayumas','satriya'],
  'Alamat': ['sukawati','kerambitan','kerambitan','perum bersemi']
})

df