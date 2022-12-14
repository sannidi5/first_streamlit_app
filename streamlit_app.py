import streamlit
import pandas
import requests
import snowflake.connector

from urllib.error import URLError

streamlit.title("Healthy Dinner")
streamlit.header("Breakfast Menu")
streamlit.text("π₯£ Breakfast 1")
streamlit.text("π₯ Breakfast 2")
streamlit.text("π Breakfast 3")
streamlit.text("π₯πBreakfast 4")
streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")
def get_fruitvyce_data(this_fruit_coice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice )
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get info")
  else:
    back_from_funct = get_fruitvyce_data(fruit_choice)
    streamlit.dataframe(back_from_funct)
except URLError as e:
  streamlit.error()
  


#streamlit.write('The user entered ', fruit_choice)

#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?

streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

my_cur = my_cnx.cursor()

my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_rows)


#streamlit.write('Thanks for adding')
#my_cur.execute("insert nto fruit_load_list values ('from streamlit')")


add_my_fruit = streamlit.text_input('What fruit would you like to add?','JackFruit')
streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")



