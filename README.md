# Taiwan-Traffic-Accident

## 此專題為小組專題,簡報連接如下
[車禍數據分析](https://www.canva.com/design/DAFb70ynuEQ/KgHuPwAk2AQTq6NsAeaN1A/view?utm_content=DAFb70ynuEQ&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu)

### 資料清整過程
1. 下載車禍數據,人口密度,車流量數據.

2. 爬蟲抓取天氣資料,台灣道路經緯度資料.

3. 天氣資料,車流量以時間及測站距離合併車禍資料.

4. 人口密度以行政區與時間合併車禍資料.

5. 依有發生車禍的正樣本資料數，製作無發生車禍的負樣本，保持類別平衡。給負樣本隨機的時間、台灣道路經緯度，並依前述流程合併人口密度、車流量、天氣資料。

### 數據分析過程
1. 以對數轉換及標準化轉換，處理特徵偏態並限縮各特徵數值範圍.

2. 以循環特徵選擇法進行特徵篩選，避免部分機器學習演算法發生維數災難.

3. 為避免數據洩露(Data leakage)，以2018-2021年資料做訓練集，2022年資料做測試集，維持訓練數據無出現未來數據.

4. 以邏輯斯回歸、KNN、隨機森林、XGBoost等四種演算法來訓練分類模型，並搭配五摺交叉驗證及網格搜尋，找到最佳模型及最佳參數.

5. 以XGBoost為最終模型（正確率.88），並將模型輸出的機率值分佈彙整出十個車禍發生可能性的級距，作為本組網頁api應用的基礎.

