import streamlit as st
from smolagents import LiteLLMModel

# Constants
MODEL_NAMES = ["Qwen/Qwen2.5-7B-Instruct-Turbo"]  # Free of charge
API_KEY = "8ae37e11f2ff5d9bed6690c34591f6b85a6f11c173ae46e2e5343390981f2a41"
MODEL_IDENTIFIER = "together_ai/" + MODEL_NAMES[0]
TEMPERATURE = 0.2

# Initialize Model
model = LiteLLMModel(MODEL_IDENTIFIER, temperature=TEMPERATURE, api_key=API_KEY)

def generate_summary(content):
    """Generate summary using the model."""
    response = model([{"role": "user", "content": "針對本文幫我生成繁中重點摘要並包含Markdown:" + content}])
    return str(response.content)

def main():
    """Streamlit App."""
    st.title("Text Summarizer with Lite LLM Model")
    
    # Text Input
    st.subheader("Input Text for Summarization")
    content = st.text_area("", height=200, placeholder="Paste your text here...")
    
    # File Upload (Optional)
    # st.subheader("Or Upload a.txt File")
    # uploaded_file = st.file_uploader("", type=['txt'])
    # if uploaded_file is not None:
    #     content = uploaded_file.read().decode("utf-8")
    
    # Generate Summary Button
    if st.button("Generate Summary"):
        with st.spinner('Generating Summary...'):
            summary = generate_summary(content)
            st.subheader("Summary")
            st.write(summary)
            # Option to Save Summary to a File
            @st.cache
            def get_summary_as_downloadable(summary):
                return summary.encode('utf-8')
            downloadable_summary = get_summary_as_downloadable(summary)
            st.download_button(
                label="Download Summary as TXT",
                data=downloadable_summary,
                file_name="summary.txt",
                mime="text/plain",
            )

if __name__ == "__main__":
    main()
