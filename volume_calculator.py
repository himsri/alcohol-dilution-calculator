import streamlit as st
import streamlit.components.v1 as components
import requests
import time

def final_volume(V_water, V_ethanol, T, k_0=0.05, T_0=25, alpha=0.0001):
    """
    Calculate the final volume after mixing water and ethanol, considering temperature dependency.

    Parameters:
    V_water (float): Volume of water in ml
    V_ethanol (float): Volume of ethanol in ml
    T (float): Temperature in Celsius
    k_0 (float): Base volume contraction factor at reference temperature
    T_0 (float): Reference temperature in Celsius
    alpha (float): Temperature coefficient

    Returns:
    float: Final volume of the solution in ml
    """
    k = k_0 + alpha * (T - T_0)
    V_solution = V_water + V_ethanol - k * (V_water * V_ethanol) ** 0.5
    return V_solution

#https://www.notion.so/images/page-cover/gradients_8.png
background_html = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://www.notion.so/images/page-cover/gradients_8.png");
    #background-size: 95% 90%;  # This sets the size to cover 100% of the viewport width and height
    background-size: cover;  # This sets the size to cover 100% of the viewport width and height
    # background-position: center;
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_html, unsafe_allow_html=True)

st.title(":blue[Alcohol Dilution Calculator]")

problem_statement = """
Do you need to accurately dilute alcohol for your mixtures? 

This website app simplifies the process! Enter the volume of water and alcohol (in milliliters) you want to mix, along with the room temperature (in degrees Celsius). We'll calculate the final solution volume, considering potential volume contraction when mixing water and alcohol.
"""

white_text_html = f"""<span style='color: black;'>{problem_statement}</span>"""

st.write(white_text_html, unsafe_allow_html=True)

st.header("Inputs")
V_water = st.text_input("Volume of Water (ml)", "250")
V_ethanol = st.text_input("Volume of Alcohol (ml)", "250")
T = st.slider("Room Temperature (°C)", min_value=-10, max_value=100, value=25)

# Calculate the final volume
if V_water.isdigit() and V_ethanol.isdigit():
    V_water = float(V_water)
    V_ethanol = float(V_ethanol)

    if st.button("Calculate Volume"):
        time.sleep(1)
        final_vol = final_volume(V_water, V_ethanol, T)
        st.header(f":blue[The final volume of the solution at {T}°C is approximately {final_vol:.2f} ml :sunglasses:]")

else:
    st.write("Please enter valid numeric values for water and alcohol volumes.")

