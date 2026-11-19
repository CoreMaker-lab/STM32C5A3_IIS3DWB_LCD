# CoreMaker STM32C5A3RGT6 + IIS3DWB 三轴振动监测平台

**COREMAKER | 3-Axis Vibration Monitoring & Edge Analytics**

基于 **STM32C5A3RGT6** 与 **ST IIS3DWB** 的三轴振动采集和边缘分析项目。MCU 端负责传感器 FIFO 采集、振动特征计算、FFT、正常状态学习、异常判断及 LCD 显示；Windows PC 上位机通过 USART1 + CH343 USB-UART 与设备通信，提供双语界面、波形/频谱显示、六位置校准、CSV 记录和串口完整性诊断。

> **当前工程版本标识**
> - MCU：`IIS3DWB_PERF_R5`（工程中还包含 MCU OPT V1.2、CAL V1.4、RATE V1.1、FFT V3、FLASH ECC V3、UART V3 等模块标识）
> - PC：`CRC Diagnostic R6`（中文 / English）
> - R6 增加串口错误证据记录与诊断能力；**不代表 CRC/数据不连续问题已被彻底修复**。

---

## 目录

- [项目功能](#项目功能)
- [硬件组成与接口](#硬件组成与接口)
- [系统架构](#系统架构)
- [采样率与数据处理](#采样率与数据处理)
- [六位置校准](#六位置校准)
- [PC 上位机使用](#pc-上位机使用)
- [CSV 与诊断日志](#csv-与诊断日志)
- [串口命令](#串口命令)
- [MCU 工程编译](#mcu-工程编译)
- [关键注意事项](#关键注意事项)
- [工程目录](#工程目录)
- [License](#license)

---

## 项目功能

### MCU 固件

- STM32C5A3RGT6 主控，ST IIS3DWB 三轴加速度传感器。
- IIS3DWB 配置量程 **±16 g**，原生 ODR 约 **26.667 kHz**。
- SPI1 + DMA 读取传感器 FIFO，INT1 用于 FIFO 水位/溢出事件通知。
- 支持 26.667 / 13.333 / 6.667 / 3.333 kS/s 四档输出采样率。
- 低速输出档由 MCU 数字滤波与抽取形成，传感器 FIFO 仍按原生 ODR 工作。
- 5 Hz 高通处理，约 200 ms 特征窗口。
- 每轴计算 RMS、峰峰值（P-P）和峰值因子（Crest Factor），共 9 项特征。
- MCU 端 1024 点 Hann 窗 FFT，输出 X/Y/Z 主峰频率与峰值幅度。
- 基于正常工况样本建立统计基线，并在 MCU 本地执行异常评分和状态判断。
- ST7796 480 × 320 LCD 显示设备状态和振动信息。
- USART1 + DMA 与 PC 通信；支持采样数据流、控制命令及运行遥测。
- 支持六位置加速度计校准，校准参数保存至设备 EDATA Flash。
- 学习模型按采样率分别保存；是否保存/加载成功以 MCU NVM 状态回报为准。

### Windows PC 上位机

- 中文 / English 双语界面。
- COM 端口刷新、连接、断开、采集启停。
- 采样率查询、选择和应用。
- 正常状态学习、进度显示、取消学习、模型状态和异常分数显示。
- X/Y/Z 三轴实时波形和 PC 端独立 FFT。
- 显示 MCU 端 FFT、性能遥测、模型 Flash 状态。
- 六位置校准向导：六面采集、求解、一致性检查、写入设备。
- CSV 原始数据记录。
- CRC、帧头格式错误、序号/样本索引断点和接收队列状态诊断。
- 自动生成串口诊断 JSONL 日志。

---

## 硬件组成与接口

| 模块 | 器件 / 引脚 | 说明 |
|---|---|---|
| MCU | STM32C5A3RGT6 | 主控制器 |
| 三轴加速度传感器 | ST IIS3DWB | ±16 g，SPI 接口 |
| Sensor SPI1 | PA5 / PA6 / PA7 | SCK / MISO / MOSI |
| Sensor CS | PB0 | 片选 |
| Sensor INT1 / INT2 | PB1 / PB2 | 中断输入 |
| USART1 | PA9 / PA10 | TX / RX |
| LCD | ST7796，480 × 320 | SPI2 显示 |
| LCD SPI2 | PC3 / PB10 / PB14 | MOSI / SCK / MISO |
| LCD 控制 | PC1 / PC2 / PC4 / PC5 | CS / DC / RESET / Backlight |
| PC 通信 | CH343 USB-UART | 连接 MCU USART1 |

> 接线时 TX/RX 交叉连接，并连接共同 GND。使用 3.3 V TTL 电平；不要将 5 V TTL 直接接入 MCU。实际 PCB 连接以对应板卡原理图为准。

### ⚠️ 串口波特率核对（重要）

当前压缩包中存在一处需要使用者留意的配置差异：

- PC `app.py` 的串口下拉框默认值为 **6,000,000 bps**。
- 当前 MCU 源码 `STM32C5A3_IIS3DWB_cmake/generated/hal/mx_usart1.c` 配置为 **4,000,000 bps**。

**PC 与 MCU 两端必须设置为相同波特率。** 若使用压缩包内未修改的 MCU 源码，请在 PC 端选择 4,000,000；若实际烧录固件已调整为 6,000,000，则 PC 端选择 6,000,000。不要仅凭 PC 默认值判断 MCU 实际波特率。

在 26.667 kS/s 下，按每组三轴样本 12 字节、UART 8N1 估算，仅数据载荷约需 3.2 Mbaud，尚未包含帧开销。实际链路连续性应以 CRC 错误、不连续事件和 MCU FIFO/串口统计为准。

---

## 系统架构

```text
ST IIS3DWB
  │
  │ SPI1 + DMA / FIFO + INT1
  ▼
STM32C5A3RGT6
  ├── 三轴原始数据采集
  ├── 数字滤波与抽取（/1、/2、/4、/8）
  ├── 振动特征计算（RMS / P-P / Crest Factor）
  ├── MCU FFT（1024-point Hann window）
  ├── 正常状态学习与异常判断
  ├── ST7796 LCD 显示
  └── USART1 + DMA 数据与命令
          │
          ▼
     CH343 USB-UART
          │
          ▼
     Windows PC Monitor
       ├── 中文 / English UI
       ├── 实时 XYZ 波形
       ├── PC FFT
       ├── MCU 状态 / FFT / NVM
       ├── 六位置校准
       ├── CSV 记录
       └── CRC / Continuity Diagnostics
```

MCU 是实时采集和异常判断的执行端；PC 主要负责可视化、控制、记录和辅助分析。PC FFT 与 MCU FFT 独立计算，点数和数据窗口可能不同，因此主峰结果允许存在小幅差异。

---

## 采样率与数据处理

### 支持的输出采样率

| 输出采样率 | 工作方式 |
|---:|---|
| 26,667 Hz | IIS3DWB 原生 ODR，/1 |
| 13,333 Hz | 数字滤波后 /2 |
| 6,667 Hz | 数字滤波后 /4 |
| 3,333 Hz | 数字滤波后 /8 |

传感器 FIFO 按约 26.667 kHz 原生 ODR 运行；低速输出档通过 MCU 数字滤波/抽取形成。

### 特征计算与异常判断

1. 设备固定安装在被测对象上，并确认设备处于稳定、可代表正常运行的工况。
2. 选择最终工作采样率后再启动正常状态学习。
3. MCU 使用约 200 ms 的特征窗口，学习 150 个有效特征块（约 30 秒有效数据，另有约 1 秒预热）。
4. 每个特征块包含 X/Y/Z 三轴 RMS、P-P 和 Crest Factor，共 9 项特征。
5. 监测时，MCU 计算当前特征相对正常基线的偏离分数；异常和恢复状态均采用连续窗口确认。

**异常分数是相对正常基线的偏离指标，不是故障概率，也不能单独作为设备故障诊断结论。** 实际应用应结合原始波形、频谱、工况和现场检查综合判断。

### 模型存储

当前固件将四个输出采样率的学习模型分别管理，并保存在 MCU EDATA Flash 中；四档模型共享六位置校准参数。学习结束后的保存由 MCU 自动执行，PC 界面会显示 NVM 初始化、加载、保存次数和序号等状态。

- 设备重新上电后，MCU 会尝试加载当前输出采样率对应的模型。
- 是否加载成功，以 PC 界面显示的 MCU NVM 状态为准。
- 六位置校准保存会清除已有学习模型；校准后必须重新学习。
- 切换采样率后，MCU 会尝试加载该采样率独立保存的模型；请检查模型/NVM 状态。若该档位没有成功恢复模型，再执行正常状态学习。不能沿用其他采样率下的统计基线。

---

## 六位置校准

六位置校准用于估计三轴加速度计零偏和比例参数，由 MCU 计算并应用，参数保存在设备 EDATA Flash。

### 操作步骤

1. 停止被测设备，使传感器处于稳定静止状态。
2. 连接 PC，打开“六位置校准 / Six-Position Calibration”。
3. 查询设备状态，确认 MCU 校准版本和当前参数可读取。
4. 点击“开始新校准”。
5. 按传感器轴向标识依次采集：`X+`、`X−`、`Y+`、`Y−`、`Z+`、`Z−`。
6. 每个方向放稳后点击“采集所选面（5 秒）”，等待完成再更换方向。
7. 六面采集完成后点击“计算并检查六面结果”。
8. 检查零偏/比例求解和综合一致性状态。
9. 通过后点击“写入设备并清除旧学习模型”，等待 MCU 最终保存确认。
10. 保存完成后，在正常运行工况下重新执行正常状态学习。

注意：
- 按实际传感器 XYZ 轴方向摆放，不要仅按外壳外观猜测方向。
- 若界面显示运动/振动，请放稳后再采集。
- 某一面失败时可重采该面，其他已采集面会保留。
- 六位置校准不替代高频振动幅值/频响校验。

---

## PC 上位机使用

### 环境要求

- Windows 10 / 11
- 64-bit Python 3.10 或更新版本
- 依赖：PySide6、pyqtgraph、numpy、pyserial

### 启动步骤

1. 下载或克隆仓库，并完整保留目录结构。
2. 进入 `PC/` 文件夹。
3. 双击 `start.bat`，或运行 `python app.py`。
4. 如未安装依赖，运行：

   ```bash
   python -m pip install -r requirements.txt
   ```

5. 在顶部选择 `中文` 或 `English`。
6. 点击刷新串口，选择 CH343 对应 COM 端口。
7. 选择与 MCU 一致的波特率，点击连接。
8. 点击查询采样率，确认 MCU 返回的支持档位。
9. 按需应用采样率，然后启动采集或正常状态学习。
10. 需要记录数据时点击 `保存 CSV`。

### 波形和 FFT 设置

- 显示时间窗：0.1 / 0.2 / 0.5 / 1 / 2 / 4 秒。
- 去均值：默认开启，便于观察微振动。
- PC FFT 点数：1024 / 2048 / 4096 / 8192。
- X/Y/Z：可分别显示或隐藏。
- 跟随时间窗：自动滚动显示最新数据。
- Y 轴自动量程：自动调整波形纵轴范围。

MCU FFT 为 1024 点 Hann 窗；PC FFT 独立计算。两端主峰结果不要求完全相同。

---

## CSV 与诊断日志

### CSV 字段

| 字段 | 含义 |
|---|---|
| `seq` | 数据包序号 |
| `sample_index` | 样本索引 |
| `fs_Hz` | 输出采样率（Hz） |
| `flags` | 数据包标志位 |
| `raw_x / raw_y / raw_z` | 三轴原始传感器数据 |
| `x_mg / y_mg / z_mg` | 换算后的三轴加速度（mg） |

### 串口诊断日志

连接期间，PC 会在 `PC/diagnostics/` 下生成 `serial_diagnostics.jsonl`。日志记录连接会话、PC 命令、MCU 状态文本、CRC/帧头错误、错误帧证据、序号/样本索引断点和接收摘要。

日志采用 2 MiB 轮转，最多保留当前文件和两份备份。出现 CRC 错误或数据不连续时，建议同时保存：
- 对应 CSV 文件；
- 整个 `PC/diagnostics/` 文件夹；
- PC 界面截图；
- 当前 MCU 固件标识、串口波特率和输出采样率。

不要仅凭截图判断 CRC 根因；R6 是诊断版本，不是 CRC 修复声明。

---

## 串口命令

调试时可通过 USART1 发送以换行结束的 ASCII 命令：

| 命令 | 功能 |
|---|---|
| `PING` | 连通性测试，回复 `PONG` |
| `START` / `STOP` | 开始 / 停止向 PC 上传采样数据 |
| `STATUS` | 查询 UART、LCD 和队列状态摘要 |
| `RATE?` | 查询当前采样率及支持档位 |
| `RATE 26667` | 设置输出采样率；可选 26667 / 13333 / 6667 / 3333 |
| `LEARN` / `CANCEL` | 启动 / 取消正常状态学习 |
| `RESET` | 复位 MCU 端振动处理与 FFT 状态 |
| `CAL INFO` | 查询校准能力/版本 |
| `CAL STATUS` | 查询校准会话状态 |
| `CAL DATA` | 查询六面采集数据和质量信息 |
| `CAL BEGIN` | 开始新校准会话 |
| `CAL FACE X+` | 采集指定方向；支持 X+、X−、Y+、Y−、Z+、Z− |
| `CAL SOLVE` | 求解并检查六面结果 |
| `CAL SAVE` | 保存校准参数并清除旧学习模型 |
| `CAL CANCEL` | 取消当前校准会话 |

---

## MCU 工程编译

MCU 工程目录：`STM32C5A3_IIS3DWB_cmake/`

工程使用 CMake Preset `debug_GCC_STM32C5A3RGT6`。推荐使用与工程匹配的 CMake、Ninja 和 ARM GNU 工具链。

示例命令（在工程目录执行，具体工具链路径以本机安装为准）：

```bash
cmake --preset debug_GCC_STM32C5A3RGT6
cmake --build --preset debug_GCC_STM32C5A3RGT6
```

构建目标为 `STM32C5A3_IIS3DWB.elf`。下载前请确认目标 MCU、链接脚本、工具链及板级接口与实际硬件一致。不要在未核对串口波特率的情况下直接将新固件用于现有 PC 配置。

---

## 关键注意事项

- 先固定安装，再学习；学习过程中不要改变设备安装方向或运行工况。
- 切换采样率后重新学习。
- 六位置校准保存会清除原有学习模型；校准后必须重新学习。
- PC 与 MCU 串口波特率必须一致；当前源码配置与 PC 默认值存在 4M / 6M 差异，首次使用前务必核对。
- CRC 错误、帧格式错误和数据不连续是不同诊断事件；应保留原始诊断文件。
- 异常分数不等于故障概率，不替代专业设备诊断和安全保护系统。
- 本项目用于振动采集与状态监测开发验证；实际安装和应用需结合设备安全规范。

---

## 工程目录

```text
.
├── PC/
│   ├── app.py
│   ├── i18n.py
│   ├── protocol.py
│   ├── detection.py
│   ├── learning_control.py
│   ├── calibration.py
│   ├── calibration_ui.py
│   ├── diagnostics.py
│   ├── telemetry.py
│   ├── requirements.txt
│   ├── start.bat
│   └── test_*.py
│
├── STM32C5A3_IIS3DWB_cmake/
│   ├── main.c / main.h
│   ├── sensor_app.c / sensor_app.h
│   ├── vibration.c / vibration.h
│   ├── mcu_fft.c / mcu_fft.h
│   ├── decimator.c / decimator.h
│   ├── iis3dwb_reg.c / iis3dwb_reg.h
│   ├── st7796.c / st7796.h
│   ├── lcd_ui.c / lcd_ui.h
│   ├── model_store.inc
│   ├── generated/
│   ├── stm32c5xx_drivers/
│   ├── stm32c5xx_dfp/
│   ├── cmake/
│   └── CMakeLists.txt
│
└── STM32C5A3_IIS3DWB.ioc2
```

---

## License

当前工程包含 ST HAL、CMSIS、Device Family Pack 等第三方组件，请保留各自原始许可文件。项目级许可请以仓库中实际提供的 `LICENSE` 文件为准；发布前请确认自有代码及第三方组件的授权范围。

---

# English

## Overview

A 3-axis vibration acquisition and edge analytics platform based on **STM32C5A3RGT6** and **ST IIS3DWB**.

The MCU handles sensor FIFO acquisition, vibration feature extraction, FFT, normal-state learning, anomaly evaluation and LCD display. The Windows PC application communicates through **USART1 + CH343 USB-to-UART**, providing bilingual UI, waveform/spectrum visualization, six-position calibration, CSV recording and serial-link diagnostics.

### Firmware / PC Version

- MCU firmware identifier: `IIS3DWB_PERF_R5`
- PC application: `CRC Diagnostic R6` with Chinese / English UI
- R6 improves evidence logging for CRC and continuity investigation. It does **not** claim that all CRC or link-integrity issues have been fixed.

## Key Features

### MCU

- STM32C5A3RGT6 + ST IIS3DWB.
- Accelerometer full scale configured to **±16 g**.
- Native sensor ODR: approximately **26.667 kHz**.
- Output rates: 26.667 / 13.333 / 6.667 / 3.333 kS/s.
- SPI1 + DMA, sensor FIFO and INT1 event handling.
- Digital filtering and decimation for lower output rates.
- 5 Hz high-pass processing and approximately 200 ms feature windows.
- RMS, peak-to-peak and crest-factor features for each axis.
- 1024-point Hann-window FFT on the MCU.
- Local normal-baseline learning and anomaly scoring.
- ST7796 480 × 320 display.
- Six-position accelerometer calibration with parameters stored in MCU EDATA Flash.

### Windows PC Application

- Chinese / English interface.
- COM port selection and connection management.
- ODR query and switching.
- Normal-state learning, progress, cancellation and model status.
- Real-time XYZ waveform and PC-side FFT.
- MCU FFT, performance telemetry and NVM status.
- Six-position calibration wizard.
- CSV data recording.
- CRC, frame-format, sequence-gap and sample-index continuity diagnostics.

## Sampling Rates

| Output rate | Method |
|---:|---|
| 26,667 Hz | Native ODR, /1 |
| 13,333 Hz | Filtered decimation, /2 |
| 6,667 Hz | Filtered decimation, /4 |
| 3,333 Hz | Filtered decimation, /8 |

The sensor FIFO runs at the native ODR. Lower output rates are generated by MCU filtering/decimation.

## Normal-State Learning

1. Mount the sensor firmly on the target machine or test fixture.
2. Ensure the target is operating in a representative normal condition.
3. Select the final output sampling rate before learning.
4. Start **Learn Normal State (30 s)**.
5. The MCU performs approximately 1 second of warm-up and collects 150 valid feature blocks, about 30 seconds of effective data.
6. Keep the mounting and operating condition stable until learning reaches 100%.

The model uses nine statistical features: RMS, peak-to-peak and crest factor for X/Y/Z. The anomaly score is a deviation metric, not a failure probability.

## Six-Position Calibration

1. Stop the target machine and keep the sensor stationary.
2. Open **Six-Position Calibration** and query the device state.
3. Start a new calibration session.
4. Capture the six orientations in order: X+, X−, Y+, Y−, Z+, Z−.
5. Keep each face stable and capture for 5 seconds.
6. Solve and check the six-face results.
7. Save the calibration parameters to the device.
8. Run normal-state learning again after calibration.

Saving calibration clears the previous learned vibration models. Six-position calibration does not replace high-frequency vibration amplitude or frequency-response calibration.

## PC Quick Start

1. Extract the complete project archive.
2. Open the `PC/` directory.
3. Run `start.bat`, or run `python app.py`.
4. Install dependencies if required:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Select Chinese or English.
6. Refresh COM ports and select the CH343 port connected to USART1.
7. Match the PC baud rate to the MCU firmware baud rate.
8. Query the output rate, apply the desired rate, and start acquisition or learning.

### Important Baud-Rate Configuration Note

The supplied PC application defaults to **6,000,000 bps**, while the current MCU source file `generated/hal/mx_usart1.c` configures USART1 to **4,000,000 bps**. The two sides must match. For the unmodified MCU source included in this archive, select 4,000,000 bps on the PC. If the flashed firmware has been rebuilt for 6,000,000 bps, select 6,000,000 bps instead.

At 26.667 kS/s, the three-axis payload alone is approximately 3.2 Mbaud under UART 8N1, before protocol overhead. Check CRC errors, continuity events and MCU FIFO statistics during high-rate operation.

## CSV and Diagnostics

CSV fields:

- `seq`: packet sequence
- `sample_index`: sample index
- `fs_Hz`: output sampling rate
- `flags`: packet flags
- `raw_x / raw_y / raw_z`: raw three-axis sensor data
- `x_mg / y_mg / z_mg`: converted acceleration in mg

The PC application writes `PC/diagnostics/serial_diagnostics.jsonl`. Preserve this file, the complete diagnostics folder, CSV data and screenshots when investigating CRC or continuity issues.

## MCU Build

The MCU project is in `STM32C5A3_IIS3DWB_cmake/` and provides the CMake preset `debug_GCC_STM32C5A3RGT6`.

```bash
cmake --preset debug_GCC_STM32C5A3RGT6
cmake --build --preset debug_GCC_STM32C5A3RGT6
```

The output target is `STM32C5A3_IIS3DWB.elf`. Verify the MCU target, toolchain, linker configuration and USART baud rate before flashing.

## Important Notes

- After changing the output rate, the MCU attempts to load the model stored for that specific rate. Verify the model/NVM status; run learning if no valid model is restored. Never reuse a baseline from a different rate.
- Relearn after saving a new six-position calibration.
- The PC and MCU UART baud rates must match.
- CRC and continuity diagnostics are evidence for investigation, not proof of a single root cause.
- The anomaly score is not a failure probability and does not replace professional machine diagnostics or safety systems.

**COREMAKER — Shenzhen Xintu Chuangke Electronic Technology Co., Ltd.**
