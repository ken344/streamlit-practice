import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.03)

'Done!!'

left_column, right_column = st.columns(2)
button = left_column.button('ここは右カラム')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問合せ')
expander.write('問い合わせ内容を書く')

#
# text= st.sidebar.text_input('好きな言葉を教えて♪')
# 'あなたの好きな言葉は：', text
#
# temperature = st.sidebar.slider('今日のあなたの体温は？', 34.0, 42.0, 36.0)
# '今日の体温：', temperature, '度'


# if st.checkbox('Show Image'):
#     img = Image.open('dra.jpeg')
#     st.image(img, caption="doraemon", use_column_width=True)

# st.write('DataFrame')
#
# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 1]
# })
#
# st.table(df)
#
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# st.bar_chart(df)
#
# # st.dataframe(df.style.highlight_max(axis=0))
#
#
# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

