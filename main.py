import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('プログレスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)#0.1秒停止して次の処理に移行する

'Done!!!'

#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#    columns=['lat','lon']
#    )
#
#st.map(df)
st.write('Interactive Widgets')

left_column,right_column = st.beta_columns(2)
button = left_column.button('右からに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

#text = st.text_input('あなたの趣味を教えてください')
#
#condition = st.slider('あなたの今の調子は？', 0,10,7)
#'コンディション：', condition
#'あなたの趣味:',text,'です'
#if st.checkbox('Show Image'):
#    img = Image.open('WIN_20150521_065330.JPG')
#    st.image(img, caption='hogehoge', use_column_width=True)

#st.table(df.style.highlight_max(axis=0))



#"""
## 章
### 節
#### 項
#
#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```

#"""