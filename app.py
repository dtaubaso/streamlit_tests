import streamlit as st


st.title("Probar videos")

video_url = st.text_input("Ingrese la url del video")

if st.button("Ver video"):
    if video_url:
        try:
            st.video(video_url)
        except Exception as e:
            st.error(f"Ocurrio un error {e}")
    else:
        st.error("No hay url de video")