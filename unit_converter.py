import streamlit as st

def length_conversion(value, from_unit, to_unit):
   
    meters = {
        'Kilometer': value * 1000,
        'Meter': value,
        'Centimeter': value * 0.01,
        'Millimeter': value * 0.001,
        'Mile': value * 1609.34,
        'Yard': value * 0.9144,
        'Foot': value * 0.3048,
        'Inch': value * 0.0254
    }

    result = {
        'Kilometer': meters[from_unit] / 1000,
        'Meter': meters[from_unit],
        'Centimeter': meters[from_unit] * 100,
        'Millimeter': meters[from_unit] * 1000,
        'Mile': meters[from_unit] / 1609.34,
        'Yard': meters[from_unit] / 0.9144,
        'Foot': meters[from_unit] / 0.3048,
        'Inch': meters[from_unit] / 0.0254
    }
    return result[to_unit]

def weight_conversion(value, from_unit, to_unit):
  
    kg = {
        'Kilogram': value,
        'Gram': value * 0.001,
        'Milligram': value * 1e-6,
        'Pound': value * 0.453592,
        'Ounce': value * 0.0283495
    }
   
    result = {
        'Kilogram': kg[from_unit],
        'Gram': kg[from_unit] * 1000,
        'Milligram': kg[from_unit] * 1e6,
        'Pound': kg[from_unit] * 2.20462,
        'Ounce': kg[from_unit] * 35.274
    }
    return result[to_unit]

def temperature_conversion(value, from_unit, to_unit):
  
    if from_unit == 'Fahrenheit':
        celsius = (value - 32) * 5/9
    elif from_unit == 'Kelvin':
        celsius = value - 273.15
    else:
        celsius = value
    
 
    if to_unit == 'Celsius':
        return celsius
    elif to_unit == 'Fahrenheit':
        return (celsius * 9/5) + 32
    else:  # Kelvin
        return celsius + 273.15

def time_conversion(value, from_unit, to_unit):

    seconds = {
        'Second': value,
        'Minute': value * 60,
        'Hour': value * 3600,
        'Day': value * 86400,
        'Week': value * 604800
    }
  
    result = {
        'Second': seconds[from_unit],
        'Minute': seconds[from_unit] / 60,
        'Hour': seconds[from_unit] / 3600,
        'Day': seconds[from_unit] / 86400,
        'Week': seconds[from_unit] / 604800
    }
    return result[to_unit]

def speed_conversion(value, from_unit, to_unit):
   
    mps = {
        'Meters per second': value,
        'Kilometers per hour': value * 0.277778,
        'Miles per hour': value * 0.44704,
        'Knots': value * 0.514444,
        'Feet per second': value * 0.3048
    }

    result = {
        'Meters per second': mps[from_unit],
        'Kilometers per hour': mps[from_unit] * 3.6,
        'Miles per hour': mps[from_unit] * 2.23694,
        'Knots': mps[from_unit] * 1.94384,
        'Feet per second': mps[from_unit] * 3.28084
    }
    return result[to_unit]

def main():
  
    st.markdown("""
        <style>
        .main-header {
            text-align: center;
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .stButton>button {
            width: 100%;
            background-color: #ff4b4b;
            color: white;
            padding: 10px;
            font-size: 18px;
        }
        .result-container {
            background-color: #e6ffe6;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

 
    st.markdown('<div class="main-header"><h1>📏 Unit Converter by SHAHID QASIM</h1></div>', unsafe_allow_html=True)
    
    units = ['Kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Mile', 'Yard', 'Foot', 'Inch']
    

    st.write("")
    
   
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("### Enter Value")
        value = st.number_input("", value=0.0, key="value_input")
    
    with col2:
        st.markdown("### From Unit")
        from_unit = st.selectbox("", units, key="from_unit")
    
    with col3:
        st.markdown("### To Unit")
        to_unit = st.selectbox("", units, key="to_unit")
    
   
    st.write("")
    st.write("")
    

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        convert_button = st.button('Convert ↔️')
    
    if convert_button:
        result = length_conversion(value, from_unit, to_unit)
  
        st.markdown(f"""
            <div class="result-container">
                <h2>{value} {from_unit} = {result:.6f} {to_unit}</h2>
            </div>
        """, unsafe_allow_html=True)
        
        
        st.write("")
        st.info("💡 Did you know? The metric system is used by 95% of the world's population!")

if __name__ == '__main__':
    main()