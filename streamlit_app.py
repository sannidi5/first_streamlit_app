import streamlit
import pandas

streamlit.title("Healthy Dinner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Breakfast 1")
streamlit.text("🥗 Breakfast 2")
streamlit.text("🐔 Breakfast 3")
streamlit.text("🥑🍞Breakfast 4")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
