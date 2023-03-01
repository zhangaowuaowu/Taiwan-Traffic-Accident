# Taiwan-Traffic-Accident

## 此專題為小組專題,簡報連接如下
[車禍數據分析](https://www.canva.com/design/DAFb70ynuEQ/KgHuPwAk2AQTq6NsAeaN1A/view?utm_content=DAFb70ynuEQ&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu)

### 資料清整過程
1. 下載車禍數據,人口密度,車流量數據.

2. 爬蟲抓取天氣資料,台灣道路經緯度資料.

3. 天氣資料,車流量以時間及測站距離合併車禍資料.

4. 人口密度以行政區與時間合併車禍資料.

5. 依有發生車禍的正樣本資料數，製作無發生車禍的負樣本，保持類別平衡。給負樣本隨機的時間、台灣道路經緯度，並依前述流程合併人口密度、車流量、天氣資料。
