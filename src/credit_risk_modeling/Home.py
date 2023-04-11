import streamlit as st

from src.credit_risk_modeling.fe.utils import change_language, get_language


st.set_page_config(page_title="Home")
change_language()
language = get_language()

if language == "en":
    st.header("Credit risk's Notes")
    st.write(
        "In this site I report notes and code from the book Credit-Risk Modeling by David Jamieson Bolder."
    )
    st.write(
        "The codes given are a reworking of what is given in the book and what can be found at the following GitHub repo: https://github.com/djbolder/credit-risk-modelling"
    )
else:
    st.header("Appunti di credit risk management")
    st.write(
        "In questo sito riporto degli appunti e il codice tratto dal libro Credit-Risk Modeling di David Jamieson Bolder."
    )
    st.write(
        "Parte del codice utilizzato in questo sito è un re-work di quanto è possibile trovare sulla seguente pagina GitHub: https://github.com/djbolder/credit-risk-modelling"
    )
