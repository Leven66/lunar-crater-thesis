# Lunar Crater Recognition via Improved YOLOv8

毕业论文代码库：基于改进 YOLOv8 的月球陨石坑识别，通过引入注意力机制与改进卷积模块提升检测精度，并与多种基线模型进行对比实验。

> **Lunar Crater Recognition Accuracy Assurance via Ensemble Learning Techniques** — GONGYIYUAN, 2025 FYP

## 项目结构

```
LAST/
├── YoloV8_Improve/      # 改进版 YOLOv8 完整源码（训练/验证入口）
│   ├── yoloV8-train.py  # 训练脚本
│   ├── yoloV8-val.py    # 验证/测试脚本
│   ├── my_data.yaml     # 数据集配置（路径需按本机修改）
│   ├── train_yaml/      # 改进模型结构定义
│   └── ultralytics/     # 二次开发的 ultralytics 框架
│                        #   主要改进：C2f_AT、C2f_OD、CAFM、ODConv 等模块
├── basev8/              # 基线 YOLOv8n 实验结果（train12）
├── CAFMv8/              # + CAFM 注意力模块（train4）
├── ODConvv8/            # + ODConv 全维动态卷积（train3）
├── 32v8/                # + 32 组合改进（train13）
├── &&v8/                # + 全部改进集成（train5）
├── yolov5/              # YOLOv5 对比实验（exp4）
├── DataSet/             # 数据集（未纳入版本控制，见下方说明）
└── *.docx / *.pdf       # 论文终稿、草稿与改进说明
```

每个实验文件夹内的 `trainN/` 目录包含训练产物：`results.csv`（逐轮指标）、
`PR_curve.png`、`F1_curve.png`、`confusion_matrix.png` 等评估图表，以及 `weights/` 下的模型权重。

## 环境安装

```bash
pip install -r requirements.txt
```

核心依赖：`ultralytics==8.3.28`、`numpy==1.26.0`、`einops==0.8.0`，详见 `requirements.txt`。

## 训练

```bash
cd YoloV8_Improve
python yoloV8-train.py
```

训练前请修改 `my_data.yaml` 中的 `path` 为你本机的数据集路径。

## 验证 / 测试

```bash
python yoloV8-val.py
```

默认加载 `./runs/detect/train/weights/best.pt`，在测试集上评估。

## 数据集

本项目使用 **ODPLCD**（Optical-DEM Paired Lunar Crater Detection Dataset）公开数据集：

- 由国家空间科学数据中心于 2022-10-30 发布，共 2,784 对月球陨石坑样本图像
- 划分：训练集 1,781 / 验证集 446 / 测试集 557
- 光学图像（近红外波段）来自 LRO 探测器 LROC 广角相机（WAC），分辨率 100 m/像素；
  DEM 图像来自 LRO 与 Kaguya 搭载的激光高度计（LOLA）
- 检测类别：1 类（`crater`）

数据集未上传至本仓库，可通过 DOI 公开获取：

> Yuqi Dai. ODPLCD. V1. Science Data Bank, 2022.
> [https://doi.org/10.57760/sciencedb.o00009.00312](https://doi.org/10.57760/sciencedb.o00009.00312)

下载后按 `images/train`、`images/val`、`images/test` 组织，并在 `my_data.yaml` 中配置路径。

## 许可证

本项目基于 [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) 二次开发，
遵循 AGPL-3.0 许可证，详见 [LICENSE](LICENSE)。
