import streamlit as st

from streamlit_toy_dict_input import dict_input


st.title("Toy `dict_input` component")

st.write(
    """
    A version of the standard dict view that is editable would be handy for
    quick prototyping, for when an app has many parameters, and as a
    supplemental way to copy configuration in and out of a streamlit app.
    
    A native `dict_input` widget might be used to edit a
    dictionary like this
    """
)
with st.echo():
    dict_template = {
        "a": 1,
        "b": 2.0,
        "c": "abc",
        "d": {"a": 3},
        "e": [4, 5.0, "def"],
    }

st.write(
    """
    and might look like a cross between the widgets below. The left is an
    editable view of the standard dict widget on the right.
    """
)

col1, col2 = st.beta_columns(2)
with col1:
    st.write("A dict_input composite widget:")
    with st.echo():
        d = dict_input("Edit me!", dict_template)
with col2:
    st.write("A standard dictionary view:")
    with st.echo():
        st.write(".", d)

st.write(
    """
    The view on the left can be edited. It will revert to its last valid
    state if invalid json is entered, or if the key-structure of the dict
    is changed or the type of a value is changed from that of its initial
    value (`config`).  The buttons copy json out of the widget or into it.

    ### Call with a function

    The value given to `json_input` might be a function rather than a dict.
    As long as all the parameters have defaults then the inital dict is
    inferred.  For example:
    """
)

with st.echo():

    def func(a=1, b=2.0, c="c"):
        return a, b, c

    config = dict_input("Parameters to call `func` with", func)

    st.write("func output:\n\n", func(**config))

st.write(
    """
    ### Options

    `dict_input` might also take a `dataclass` (not implemented). The option
    `mutable_structure` may be set to True allowing the key structure and
    value types to change (implemented)."""
)
