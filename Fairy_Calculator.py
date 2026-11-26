
import streamlit as st

st.set_page_config(
    page_title="Fairy Calculator",
    page_icon="🧚",
    layout="centered"
)

# Page heading
st.title("Fairy Calculator")
st.write("A little magic in every calculation! ✨")
st.success("Welcome to your magical calculator! 🧚‍♀️")

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #fff0f6;
    background-image:
        radial-gradient(circle, rgba(255,255,255,0.9) 1px, transparent 2px),
        radial-gradient(circle, rgba(255,255,255,0.6) 1px, transparent 2px);
    background-size: 65px 65px, 95px 95px;
    background-position: 0 0, 30px 40px;
}

.stApp::before {
    content: "🎀       🎀       🎀";
    white-space: pre;
    position: fixed;
    inset: 0;
    font-size: 27px;
    line-height: 85px;
    letter-spacing: 20px;
    opacity: 0.2;
    pointer-events: none;
    z-index: 0;
}

.stApp > header,
.stApp > div {
    position: relative;
    z-index: 1;
}

.stApp::after {
    content: "🪄";
    position: fixed;
    bottom: 25px;
    right: 25px;
    font-size: 48px;
    transform: rotate(-20deg);
    z-index: 10;
    pointer-events: none;
}

.st-key-calculator_panel {
    background: rgba(255, 220, 235, 0.48);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 2px solid rgba(255, 255, 255, 0.75);
    border-radius: 28px;
    padding: 30px;
    box-shadow: 0 8px 30px rgba(220, 130, 170, 0.18);
}
</style>
""", unsafe_allow_html=True)


# Initialize session state
if "display_value" not in st.session_state:
    st.session_state.display_value = "0"

if "first_number" not in st.session_state:
    st.session_state.first_number = None

if "operator" not in st.session_state:
    st.session_state.operator = None


# Calculator button function
def button_click(value):

    if value == "C":
        st.session_state.display_value = "0"
        st.session_state.first_number = None
        st.session_state.operator = None

    elif value in ["+", "-", "*", "/"]:
        st.session_state.first_number = float(
            st.session_state.display_value
        )
        st.session_state.operator = value
        st.session_state.display_value = "0"

    elif value == "=":

        if st.session_state.operator is not None:

            second_number = float(st.session_state.display_value)
            first_number = st.session_state.first_number
            operator = st.session_state.operator

            if operator == "+":
                result = first_number + second_number

            elif operator == "-":
                result = first_number - second_number

            elif operator == "*":
                result = first_number * second_number

            elif operator == "/":
                if second_number == 0:
                    st.session_state.display_value = "Error"
                    st.session_state.first_number = None
                    st.session_state.operator = None
                    return

                result = first_number / second_number

            st.session_state.display_value = str(result)
            st.session_state.first_number = None
            st.session_state.operator = None

    elif value == ".":

        if "." not in st.session_state.display_value:
            st.session_state.display_value += "."

    elif st.session_state.display_value == "0":
        st.session_state.display_value = value

    else:
        st.session_state.display_value += value


# Calculator interface
with st.container(key="calculator_panel"):

    st.markdown("### Your Magical Calculator")
    st.write("Let's make some magic! ✨")

    # Display
    st.text_input(
        "Your magical display",
        value=st.session_state.display_value,
        disabled=True
    )

    # Buttons
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button("7", on_click=button_click, args=("7",), use_container_width=True)
        st.button("4", on_click=button_click, args=("4",), use_container_width=True)
        st.button("1", on_click=button_click, args=("1",), use_container_width=True)
        st.button("0", on_click=button_click, args=("0",), use_container_width=True)

    with col2:
        st.button("8", on_click=button_click, args=("8",), use_container_width=True)
        st.button("5", on_click=button_click, args=("5",), use_container_width=True)
        st.button("2", on_click=button_click, args=("2",), use_container_width=True)
        st.button(".", on_click=button_click, args=(".",), use_container_width=True)

    with col3:
        st.button("9", on_click=button_click, args=("9",), use_container_width=True)
        st.button("6", on_click=button_click, args=("6",), use_container_width=True)
        st.button("3", on_click=button_click, args=("3",), use_container_width=True)
        st.button("=", on_click=button_click, args=("=",), use_container_width=True)

    with col4:
        st.button("C", on_click=button_click, args=("C",), use_container_width=True)
        st.button("+", on_click=button_click, args=("+",), use_container_width=True)
        st.button("-", on_click=button_click, args=("-",), use_container_width=True)
        st.button("*", on_click=button_click, args=("*",), use_container_width=True)
        st.button("/", on_click=button_click, args=("/",), use_container_width=True)
