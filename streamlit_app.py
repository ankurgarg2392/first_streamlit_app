import streamlit
streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🍇Poha')
streamlit.text('🥔Chilla')
streamlit.text('🥒Oats')
streamlit.header('🥭🍓Build your own fruit smoothie 🥝🍨')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
