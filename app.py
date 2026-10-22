
import streamlit as st

st.title("Car Fuel Cost Calculator")
st.write("Calculate the fuel cost of your trip.")

distance = st.number_input("Distance (km)", min_value=0.0)
efficiency = st.number_input("Fuel Efficiency (km/liter)", min_value=0.0)
price = st.number_input("Fuel Price (SAR/liter)", min_value=0.0)

if st.button("Calculate Cost"):
    if distance <= 0 or efficiency <= 0 or price <= 0:
        st.error("Please enter values greater than zero.")
    else:
        fuel = distance / efficiency
        cost = fuel * price

        st.write(f"Fuel needed: {fuel:.2f} liters")
        st.write(f"Total cost: {cost:.2f} SAR")

        if cost < 50:
            st.info("Cost Level: Low")
        elif cost <= 150:
            st.info("Cost Level: Medium")
        else:
            st.info("Cost Level: High")
