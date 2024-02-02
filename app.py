import streamlit as st

import utils
import vertex

st.set_page_config(
    page_title="Contract liability predictor",
    page_icon=":robot:",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# You will discover by yourself"
    }
)

#creating session states
utils.create_session_state()


st.title(":pink[PaLM 2 fine tuned] :pink[Rafa-Stephane-Julie] Contract Liability Predictor")



with st.container():
    st.write("Current Generator Settings: ")
    # if st.session_state['temperature'] or st.session_state['debug_mode'] or :
    st.write ("Temperature: ",st.session_state['temperature']," \t \t Token limit: ",st.session_state['token_limit']
                ," \t \t Top-K: ",st.session_state['top_k']
                ," \t \t Top-P: ",st.session_state['top_p']
                ," \t \t Debug Model: ",st.session_state['debug_mode'])


    prompt = st.text_area("Add your prompt: ",height = 100)
    
###trial julie


#####
    
    
    

    
    if prompt:
        st.session_state['prompt'].append(prompt)
        st.markdown("<h3 style='text-align: center; color: blue;'>Generator Model Response</h3>", unsafe_allow_html=True)
        with st.spinner('PaLM is working to generate, wait.....'):
            response = vertex.get_text_generation(prompt=prompt, temperature = st.session_state['temperature'],
                                max_output_tokens = st.session_state['token_limit'],
                                top_p = st.session_state['top_p'],
                                top_k = st.session_state['top_k'])
            st.session_state['response'].append(response)
            st.markdown(response)
