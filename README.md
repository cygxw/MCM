# MCM 站点数据绘图示例

读取三行教学数据，输出各站点次数和均值，并生成柱状图。数据为演示用途，不代表真实观测结果。

## 文件说明

- `plot.py`：读取数据、打印统计结果并绘图。
- `data/stations.csv`：三行教学数据（另含一行表头）。
- `requirements.txt`：Python 依赖清单。
- `figures/stations.png`：运行后自动生成的图片，不提交到 Git。

| station | count |
| --- | ---: |
| A | 8 |
| B | 11 |
| C | 5 |

## 创建环境、安装依赖并运行

需要 Python 3.13 及 Git。以下命令从终端执行；若已有仓库副本，直接进入仓库目录。

```text
git clone https://github.com/yunyuxuanyuan111/MCM.git
cd MCM
```

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe plot.py
```

以上命令直接使用虚拟环境中的 Python，无需激活环境或调整 PowerShell 执行策略。如果系统使用 `py` 启动 Python，可将第一条命令改为 `py -3 -m venv .venv`。

如果已安装 `uv`，也可将创建环境的第一条命令替换为 `uv venv --python 3.13 --seed .venv`；后续安装与运行命令相同。

### macOS / Linux

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python plot.py
```

脚本使用 Matplotlib 的 `Agg` 后端，不会弹出窗口；生成的图片位于 `figures/stations.png`。数据和输出路径均相对于脚本目录。

## 核查结果

运行后会输出以下统计结果，最后一行显示图片的实际保存路径：

```text
station=A, count=8
station=B, count=11
station=C, count=5
Mean: 8 rentals/station
Saved plot: <仓库目录>/figures/stations.png
```

教学数据共 3 个站点，总次数为 24，均值为 8 次/站。
