# emotion-recognition
基于皮肤电信号的情绪识别算法emotion-recognition

基于皮肤电信号的情绪识别算法

### 代码架构

├── butter.py			巴特沃斯滤波器（代码中并未使用，可参考）
├── data				训练数据集
│   ├── happy			高兴
│   │   ├── x.csv
│   ├── normal			平静
│   │   ├── x.csv
│   └── sad				悲伤
│       ├── x.csv
├── database.py			数据库连接
├── generatevector.py	特征向量提取，调用getattr
├── getattr.py			提取算法
├── main.py				主函数
├── model				训练所得模型
│   ├── happy_model.m
│   ├── happy_other.csv
│   ├── normal_sad.csv
│   ├── sad_model.m
│   ├── train_model.m
│   ├── vector.mat
│   └── vector_select.m
├── my_svm.py			支持向量机
├── plotdata.py			绘图（测试代码，未使用）
├── pre.pptx			PPT展示
├── __pycache__
│   ├── database.cpython-36.pyc
│   ├── generatevector.cpython-36.pyc
│   ├── getattr.cpython-36.pyc
│   └── my_svm.cpython-36.pyc
└── README.md

### 工作流程

1 通过MP150提取被试皮电信号，情绪激发通过视频素材激发

2 每个被试每种情绪采集80s有效信号，采样频率20Hz，共1600个数据点

3 提取皮电信号特征向量，时域信号28个，频域信号6个，共34个，如下表

| 特征编号 | 特征代号              | 特征含义           |
| ---- | ----------------- | -------------- |
| 1    | sc_mean           | GSR信号均值        |
| 2    | sc_median         | GSR信号中值        |
| 3    | sc_std            | GSR信号标准差       |
| 4    | sc_min            | GSR信号最小值       |
| 5    | sc_max            | GSR信号最大值       |
| 6    | sc_range          | GSR最大值最小值之差    |
| 7    | sc_min_ratio      | GSR最小值比率       |
| 8    | sc_max_ratio      | GST最大值比率       |
| 9    | sc1diff_mean      | 一阶差分均值         |
| 10   | sc1diff_median    | 一阶差分中值         |
| 11   | sc1diff_std       | 一阶差分标准差        |
| 12   | sc1diff_min       | 一阶差分最小值        |
| 13   | sc1diff_max       | 一阶差分最大值        |
| 14   | sc1diff_range     | 一阶差分最大值最小值之差   |
| 15   | sc1diff_min_ratio | 一阶差分最小值比率      |
| 16   | sc1diff_max_ratio | 一阶差分最大值比率      |
| 17   | sc1adiff_mean     | 一阶差分绝对值均值      |
| 18   | sc1gdiff_mean     | 归一化信号一阶差分绝对值均值 |
| 19   | sc2diff_mean      | 二阶差分均值         |
| 20   | sc2diff_median    | 二阶差分中值         |
| 21   | sc2diff_std       | 二阶差分标准差        |
| 22   | sc2diff_min       | 二阶差分最小值        |
| 23   | sc2diff_max       | 二阶差分最大值        |
| 24   | sc2diff_range     | 二阶差分最大值最小值之差   |
| 25   | sc2diff_min_ratio | 二阶差分最小值比率      |
| 26   | sc2diff_max_ratio | 二阶差分最大值比率      |
| 27   | sc2adiff_mean     | 二阶差分绝对值均值      |
| 28   | sc2gdiff_mean     | 归一化信号二阶差分绝对值均值 |
| 29   | scfft_mean        | GSR频域均值        |
| 30   | scfft_median      | GSR频域中值        |
| 31   | scfft_std         | GSR频域标准差       |
| 32   | scfft_min         | GSR频域最小值       |
| 33   | scfft_max         | GSR频域最大值       |
| 34   | scfft_range       | GSR频域最大值最小值之差  |



4 特征选取，使用随机森林算法，最终选取贡献度为平均贡献度1.25倍的特征，组建新的特征向量。

5 训练模型，采取支持向量机，一对多策略从而实现多分类的目的。

6 预测，arduino进行信号采集写入到端口中，该工程读取串口数据存入缓存区。当缓存区数据点>50时，计算特征向量给出预测结果。整个过程通过matplotlib进行交互式展现。



