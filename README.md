# CNContact
从包含联系方式的中文字符串中提取结构化数据。

```Python
import CNContact as CC

content = '【联系方式】壹柒捌玖陆零陆捌柒贰玖'
tel = CC.tel(content)
```

## 项目规划
1. 文本数据清理：删除多余空行
2. 联系方式的可能变种形式梳理
3. 联系方式的关键词判定
4. 其他结构化信息的判定
4. 发布到Pip

### 联系方式的可能变种形式
大多数变种都以以下类型的混合形式呈现，我们相信采用穷举法可以列出所有可能的常见形态。
1. 汉字大写
2. o代替0
3. 同音字
4. 近音字：`幺三六 4幺零7 3642`
5. 无任何变形

### 联系方式的关键词判定
1. 电话：`电话号码：`, `手机号码`
2. 微信：`微信号`, `微信`

### 其他结构化信息的判定
1. 小区名称：可以考虑关联[XiaoQu](https://github.com/rangduju/XiaoQu)来做关键词判定
2. 时间日期：`ThuJul1109:13:492019`
