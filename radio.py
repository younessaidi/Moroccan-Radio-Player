import streamlit as st #streamlit run radio.py and python -m pip install streamlit
import json
#Younes</>
with open("radio.json", "r") as file:
    data = json.load(file)

st.set_page_config(
    page_title="Radio Player",
    page_icon="📻",
    layout="centered"
)

st.title("🎧 Moroccan Radio Player")
st.write("📻 Enjoy with the best radio stations!")

col1, col2, col3 = st.columns([1, 2, 3])

option = st.selectbox("Choose your favorite radio station 📻:", ["Aswat", "Mfm", "Hit radio"])

if option == "Hit radio":
    with col1:
        st.image("https://www.hitradio.ma/logo/small-logo-hitradio_0.png", caption="🎵 HitRadio", width=150)
    with col2:
        st.audio(data["hitradio"], format="audio/mp3")
    with col3:
        st.write("🔥 Enjoy the latest hits and energetic music!")

elif option == "Mfm":
    with col1:
        st.image("https://www.mfmradio.ma/wp-content/themes/mfmradio/assets/img/mfm-brand.png", caption="🎵 MFM", width=150)
    with col2:
        st.audio(data["mfm"], format="audio/mp3")
    with col3:
        st.write(" A mix of great music and amazing shows from MFM!")

elif option == "Aswat":
    with col1:
        st.image("https://radioaswat.ma/wp-content/themes/aswata108/img/xlogo.png.pagespeed.ic.IsNRFEd7cG.webp", caption="🎵 Aswat", width=150)
    with col2:
        st.audio(data["aswat"], format="audio/mp3")
    with col3:
        st.write("🌟 Discover the best Moroccan songs with Aswat!")
else:
    st.write("❌ No station selected.")
st.markdown("**Thanks for see my project** [Younes](https://github.com/younessaidi)") #Younes </>