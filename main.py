import streamlit as st

# st.image("logo2.jpeg")
st.title("2305A21L47-PS6")


def Tran_Eff(Ratin, CL, FCL, K, PF):
    
    CUL = FCL * (K ** 2) 
    Pout = Ratin * K * PF
    Pin = Pout + CL + CUL
    Eff = (Pout / Pin) * 100
    return Eff, CUL


col1,col2 = st.columns(2)

with col1:
    with st.container(border = True):
        
        Ratin = st.number_input("Transformer Rating (VA):", min_value=0.0, step=50.0, format="%.0f")
        CL = st.number_input("Core Losses (CL) in Watts:", min_value=0.0, step=10.0, format="%.1f")
        FCL = st.number_input("Full Load Copper Losses (FCL) in Watts:", min_value=0.0, step=10.0, format="%.1f")
        K = st.number_input("Loading on Transformer (K):", min_value=0.0, max_value=1.0, step=0.05, format="%.2f")
        PF = st.number_input("Power Factor (PF):", min_value=0.0, max_value=1.0, step=0.05, format="%.2f")
    
    compute = st.button("Calculate Efficiency")
    
with col2:    
    if compute:
        Eff, CUL = Tran_Eff(Ratin, CL, FCL, K, PF)
        st.write(f"Transformer Efficiency: {Eff:.2f}%")
        st.write(f"Copper Losses at {K*100:.0f}% Load: {CUL:.2f} Watts")
    
    st.caption("Developed by [Your Name]")

# if "name" == "_main_":
#     main