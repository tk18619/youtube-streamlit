import streamlit as st
import time

st.title("Streamlit超入門")
st.write('プログレスバー')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!'

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('これは右カラム')



expander =st.expander('問い合わせ')
expander.write('問い合わせ内容を記載する')


text = st.text_input('あなたの趣味を教えてください')
condition =st.sidebar.slider('あなたの今の調子は',0,100,50)

'あなたの趣味:',text
'コンディション',condition







#　if st.checkbox('Show Image'):
#  img = Image.open('marupi.png')
#   st.image(img,caption='marupi',use_column_width=True);



#st.map(df)