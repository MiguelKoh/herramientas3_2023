# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import plotly.figure_factory as ff

import plotly.express as px
import pandas as pd

df = px.data.gapminder()
st.dataframe(df)
listaPaises = df["country"].unique().tolist()
st.write(listaPaises)
pais = "canada"
with st.sidebar:
    pais = st.selectbox("paises",listaPaises)
    #st.write(pais)

datosPais = df.query("country == '"+pais+"'")
fig = px.bar(datosPais, x='year', y='pop')
st.plotly_chart(fig,use_container_width=True)
    #fig.show()




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    st.header("hola desde streamlit")
    st.subheader("probando 1..2..3")
    st.write("Hola soy Miguel")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('´prueba')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
