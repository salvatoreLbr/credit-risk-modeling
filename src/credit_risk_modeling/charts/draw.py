import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
from typing import Dict, Optional


def draw_plot(
    series1: np.array,
    series2: np.array,
    label: Optional[str]=None,
    title: Optional[str]=None,
    plot_chart_streamlit: Optional[bool]=False,
    plot_chart_local: Optional[bool]=False,
):
    # plotting CDF
    fig, ax = plt.subplots()
    ax.plot(series1, series2, label=label)
    # Set title
    ax.set_title(title)
    # Set legend
    ax.legend()
    if plot_chart_streamlit:
        st.pyplot(fig)
    elif plot_chart_local:
        fig.show()



def draw_vertical_line(
    ax: plt,
    x: float,
    ymin: Optional[float] = 0,
    ymax: Optional[float] = 1,
    color: Optional[str] = "r",
    label: Optional[str] = "",
    linestyle: Optional[str] = "solid",
):
    """Function for adding a vertical line to a chart.

    Args:
        ax (plt): _description_
        x (float): _description_
        ymin (Optional[float], optional): _description_. Defaults to 0.
        ymax (Optional[float], optional): _description_. Defaults to 1.
        color (Optional[str], optional): _description_. Defaults to "r".
        label (Optional[str], optional): _description_. Defaults to "".
        linestyle (Optional[str], optional): _description_. Defaults to "solid".

    Returns:
        _type_: _description_
    """
    ax.axvline(x=x, ymin=ymin, ymax=ymax, color=color, label=label, linestyle=linestyle)

    return ax


def get_probability_density_function_chart(
    distribution_value: np.array,
    plot_chart_streamlit: bool,
    plot_chart: bool,
    bins: Optional[int] = 30,
    title: Optional[str] = "Distribution",
    vertical_line_dict: Optional[Dict] = {},
):
    """Draw a histogram (PDF)"""
    fig, ax = plt.subplots()
    count, bins, _ = ax.hist(distribution_value, bins, density=True)
    # Add vertical lines (if any)
    for key, value in vertical_line_dict.items():
        ax = draw_vertical_line(
            ax=ax,
            x=value["x"],
            ymin=value["ymin"] if "ymin" in value.keys() else None,
            ymax=value["ymax"] if "ymax" in value.keys() else None,
            color=value["color"] if "color" in value.keys() else None,
            label=key,
            linestyle=value["linestyle"] if "linestyle" in value.keys() else None,
        )
    # Set title
    ax.set_title(title)
    # Set legend
    ax.legend()
    if plot_chart_streamlit:
        st.pyplot(fig)
    elif plot_chart:
        fig.show()

    return count, bins


def get_cumulative_distribution_function_chart(
    distribution_value: np.array,
    plot_chart_streamlit: bool,
    plot_chart: bool,
    bins: Optional[int] = 30,
    title: Optional[str] = "Distribution",
    vertical_line_dict: Optional[Dict] = {},
):
    """Draw a CDF chart."""
    count, bins = get_probability_density_function_chart(
        distribution_value, False, False, bins, title, vertical_line_dict
    )
    # finding the PDF of the histogram using count values
    pdf = count / sum(count)

    # using numpy np.cumsum to calculate the CDF
    # We can also find using the PDF values by looping and adding
    cdf = np.cumsum(pdf)

    # plotting CDF
    fig, ax = plt.subplots()
    ax.plot(bins[1:], cdf, label="CDF")
    # Set title
    ax.set_title(title)
    # Set legend
    ax.legend()
    if plot_chart_streamlit:
        st.pyplot(fig)
    elif plot_chart:
        fig.show()
