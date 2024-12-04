# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Example Streamlit App :apple:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)

# Get the current credentials
name_on_order = st.text_input('Name on Smoothie');
st.write('test', name_on_order );
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select (col("FRUIT_NAME"))
#st.dataframe(data=my_dataframe, use_container_width=True)

ing_list = st.multiselect('select fruit', my_dataframe, max_selections = 5)

if ing_list:

    ing_string = ''

    for each_ing in ing_list:
        ing_string += each_ing + ' '

    if ing_string:
        st.write(ing_string);
        
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
            values ('""" + ing_string + """','"""+name_on_order+"""')"""

    st.write(my_insert_stmt)

    time_to_insert = st.button('Submit order')

    if time_to_insert:
        if ing_string:
            session.sql(my_insert_stmt).collect()
            st.success('Your Smoothie is ordered!', icon="✅")
    