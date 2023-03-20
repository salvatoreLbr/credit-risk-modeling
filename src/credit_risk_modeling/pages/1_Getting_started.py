import numpy as np
import streamlit as st

from src.credit_risk_modeling.charts.draw import get_cumulative_distribution_function_chart, get_probability_density_function_chart


st.set_page_config(page_title="Getting started")

st.header("Basic concepts")
st.markdown("""Credit risk is a topic that been interested in: <br><ul><li><b>Default risk</b>: The defaulting of a counterparty (or obligor) obligation.</li>
<li><b>Migration risk</b>: The deterioration of an obligor's ability to pay, which makes default more probable.</li></ul><br>""", unsafe_allow_html=True)
st.markdown("There are two applications of credit-risk models: <br><ul><li><b>Pricing credit risk</b></li><li><b>Measuring the riskiness of credit exposures</b></li></ul><br>", unsafe_allow_html=True)
st.markdown("The distribution of default losses is the object of central interest for credit-risk modellers. <br> Pricing is interested on the central part of distribution, instead risk management is more interested on its tails.<br>", unsafe_allow_html=True)
st.markdown("Let us observe the following graph:", unsafe_allow_html=True)

mu = 0
sigma = 1
s = np.random.normal(mu, sigma, 1000)
vertical_line_dict = {
    "Tail": {
        "x": -2.75,
        "ymin": 0,
        "ymax": 1,
        "color": "r",
        "linestyle": "dashed"
    },
    "Mean": {
        "x": 0,
        "ymin": 0,
        "ymax": 1,
        "color": "b",
        "linestyle": "dashed"
    }
}
get_probability_density_function_chart(distribution_value=s, plot_chart=True, title="Probability Density Function", vertical_line_dict=vertical_line_dict)

st.markdown("And now see this chart:")
get_cumulative_distribution_function_chart(distribution_value=s, plot_chart=True, title="Cumulative Distribution Function", vertical_line_dict=vertical_line_dict)




st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)


