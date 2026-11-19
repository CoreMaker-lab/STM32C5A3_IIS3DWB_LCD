"""Lightweight reversible Chinese/English UI text translation for the IIS3DWB PC app."""
from __future__ import annotations


ZH_EN = {
    "IIS3DWB 三轴振动监测 · CRC定位 R6": "IIS3DWB 3-Axis Vibration Monitor · CRC Diagnostics R6",
    "IIS3DWB：±16g / 约26.7 kHz；串口波特率须与 MCU 一致。": "IIS3DWB: ±16g / approx. 26.7 kHz; serial baud rate must match the MCU.",
    "IIS3DWB：±16g，当前输出 ": "IIS3DWB: ±16g, current output ",
    "刷新串口": "Refresh Ports",
    "中文": "Chinese",
    "切换界面语言": "Switch UI language",
    "断开连接后选择；MCU串口必须设为相同波特率。选择此项不会自动修改MCU。": "Select after disconnecting. The MCU serial baud rate must match; this selection does not change the MCU setting.",
    "连接已关闭": "Connection closed",
    "连接": "Connect",
    "断开": "Disconnect",
    "开始采集": "Start Acquisition",
    "停止采集": "Stop Acquisition",
    "保存 CSV": "Save CSV",
    "结束保存": "Stop Saving",
    "传感器采样率": "Sensor Sample Rate",
    "等待 MCU 支持列表": "Waiting for MCU supported rates",
    "查询采样率": "Query Sample Rate",
    "应用采样率": "Apply Sample Rate",
    "等待 MCU 查询结果；切换后需重新学习": "Waiting for MCU response; relearning is required after a rate change",
    "六位置校准…": "Six-Position Calibration…",
    "PC：CRC定位 R6 | MCU：等待版本回复": "PC: CRC Diagnostics R6 | MCU: Waiting for version",
    "原始实际加速度 (mg)": "Raw Acceleration (mg)",
    "校准后加速度 (mg)": "Calibrated Acceleration (mg)",
    "等待原始数据": "Waiting for raw data",
    "尚未确认校准": "Calibration not yet confirmed",
    "约0.5秒均值，含重力；校准后值仅采用MCU明确标记的结果。": "Approx. 0.5 s mean, including gravity. Calibrated values are shown only when explicitly identified by the MCU.",
    "MCU版本：等待核验": "MCU version: awaiting verification",
    "MCU 本地正常状态学习": "MCU Local Baseline Learning",
    "学习正常状态（30秒）": "Learn Normal State (30 s)",
    "取消学习": "Cancel Learning",
    "等待设备结果": "Waiting for device result",
    "异常分数：—": "Anomaly Score: —",
    "模型：未知": "Model: Unknown",
    "固定安装并确认设备正常后学习；约1秒预热＋30秒有效数据。支持配套固件保存模型；是否保存成功以 MCU 存储结果为准。": "Securely mount the device and confirm normal operation before learning. Approx. 1 s warm-up + 30 s of valid data. Model saving requires compatible firmware; the MCU storage status is authoritative.",
    "MCU FFT · 1024点 / Hann窗 / 峰值幅度": "MCU FFT · 1024 points / Hann window / Peak Amplitude",
    "等待 MCU FFT 结果": "Waiting for MCU FFT result",
    "以下频谱曲线由 PC 计算；两端 FFT 点数不同，主峰可能略有差异。": "The spectrum below is calculated by the PC. Different FFT sizes may cause slight differences in peak frequency.",
    "模型存储：等待 MCU 状态": "Model Storage: Waiting for MCU status",
    "显示时长": "Display Duration",
    "去均值（观察微振动）": "Remove Mean (View Micro-vibration)",
    "FFT 点数": "FFT Size",
    "跟随时间窗": "Follow Time Window",
    "Y轴自动量程": "Auto Y-Axis Range",
    "恢复视图": "Reset View",
    "取消跟随后：滚轮缩放、左键拖动；频谱可独立缩放。": "When follow mode is off: use the mouse wheel to zoom and left-drag to pan. The spectrum can be zoomed independently.",
    "等待数据；RMS/峰峰值基于所选显示窗口，去除均值。": "Waiting for data. RMS and peak-to-peak values use the selected display window after mean removal.",
    "三轴加速度波形": "3-Axis Acceleration Waveform",
    "加速度": "Acceleration",
    "相对时间": "Relative Time",
    "频谱（Hann 窗，去直流）": "Spectrum (Hann Window, DC Removed)",
    "幅值": "Amplitude",
    "频率": "Frequency",
    "MCU 异常分数（偏差指标，非故障概率；虚线为判断阈值）": "MCU Anomaly Score (Deviation Metric, Not Failure Probability; Dashed Line = Threshold)",
    "异常分数": "Anomaly Score",
    "MCU 运行状态：等待上报（约5秒一次）": "MCU Runtime: Waiting for report (approx. every 5 s)",
    "主循环忙碌率估计：扣除循环末尾HAL_Delay时间，包含SPI同步等待；不是精确CPU执行占用率。FFT/LCD为本统计周期的累计前台耗时，毫秒精度。队列峰值为本次启动累计值。": "Main-loop busy-time estimate: excludes the final HAL_Delay but includes synchronous SPI waits; it is not an exact CPU utilization measurement. FFT/LCD values are accumulated foreground time for this reporting period (ms). Queue peak is cumulative since startup.",
    "未连接": "Disconnected",
    "原始值 · 含零偏": "Raw · Includes Bias",
    "未收到 / 超时": "No Data / Timeout",
    "已应用设备校准": "Device Calibration Applied",
    "两行均为约0.5秒均值、含重力；校准后值已应用设备参数。": "Both rows show approx. 0.5 s means including gravity. Calibrated values use the device calibration parameters.",
    "尚未校准": "Not Calibrated",
    "请先完成六位置校准并保存；此处不把原始值当作校准后值。": "Complete and save the six-position calibration first. Raw values are not presented as calibrated values.",
    "约0.5秒均值，含重力；两行分别以原始/已校准报文为准。": "Approx. 0.5 s mean including gravity; each row follows the raw/calibrated message from the MCU.",
    "六位置校准": "Six-Position Calibration",
    "请先结束 CSV 保存、采样率切换或正常状态学习。": "Finish CSV recording, sample-rate switching, or baseline learning first.",
    "等待串口线程退出": "Waiting for the serial thread to stop",
    "串口": "Serial Port",
    "请先选择串口。": "Please select a serial port first.",
    "校准会话或校准操作尚未结束，请先完成或取消校准。": "Calibration is still active. Complete or cancel calibration first.",
    "正在切换采样率，请等待完成。": "Sample rate change in progress. Please wait.",
    "串口未连接，学习指令未发送。": "Serial port is not connected. The learning command was not sent.",
    "结果超时": "Result Timeout",
    "模型：未知（无最新结果）": "Model: Unknown (No Recent Result)",
    "正在查询 MCU 实际采样率及支持档位…": "Querying the MCU's actual sample rate and supported options…",
    "已请求 ": "Requested ",
    " Hz，等待 MCU 确认；原学习模型需重新学习": " Hz; waiting for MCU confirmation. The previous baseline model must be relearned",
    "切换未收到确认，实际速率未知；请重新查询，界面未假定切换成功。": "No confirmation received for the rate change. The actual rate is unknown; query again. The UI does not assume the change succeeded.",
    "未收到采样率能力回复：当前固件可能尚不支持 RATE 指令。原有采集可继续。": "No sample-rate capability response. This firmware may not support the RATE command; existing acquisition can continue.",
    "以下频谱由 PC 计算；暂无有效 MCU FFT 结果。": "The spectrum below is calculated by the PC; no valid MCU FFT result is currently available.",
    "保存收到的采样（保留索引与断点）": "Save Received Samples (Preserve Indices and Gaps)",
    "PC：CRC定位 R6 | MCU：": "PC: CRC Diagnostics R6 | MCU: ",
    "连接已结束，请断开后重连": "Connection ended. Disconnect and reconnect.",
    "接收中": "Receiving",
    "已连接，等待采样数据": "Connected; waiting for sample data",
    "串口 ": "Port ",
    " bps | Fs=": " bps | Fs=",
    " Hz | 样本 ": " Hz | Samples ",
    " | CRC/格式错误 ": " | CRC/Format Errors ",
    " | 不连续事件 ": " | Discontinuity Events ",
    " | 显示队列丢帧 ": " | Display Queue Drops ",
    " 点": " points",
    "数据不连续，等待新的连续统计窗口": "Data discontinuity; waiting for a new continuous analysis window",
    "FFT 等待新的连续数据窗口": "FFT waiting for a new continuous data window",
    "FFT 等待连续数据 ": "FFT waiting for continuous data ",
    "PC 主峰: ": "PC Peaks: ",
    "PC 版本：CRC定位 R6；入口：": "PC Version: CRC Diagnostics R6; entry: ",
    "已打开串口：": "Opened serial port: ",
    "，配置波特率 ": ", baud rate ",
    "诊断记录：": "Diagnostic log: ",
    "诊断文件无法写入：": "Cannot write diagnostic file: ",
    "错误: ": "Error: ",
    "串口指令未完整写出": "Serial command was not fully written",
    "接收诊断：": "Receive diagnostic: ",
    "；原始帧已记录": "; raw frame recorded",
    "CSV 保存中": "CSV recording",
    "CSV 已关闭": "CSV closed",
    "26.667 kHz（原生）": "26.667 kHz (Native)",
    "13.333 kHz（滤波降采样 /2）": "13.333 kHz (Filtered Decimation /2)",
    "6.667 kHz（滤波降采样 /4）": "6.667 kHz (Filtered Decimation /4)",
    "3.333 kHz（滤波降采样 /8）": "3.333 kHz (Filtered Decimation /8)",
    " — MCU未支持": " — Not Supported by MCU",
    "；设备仅上报一档，低速项暂不可用。": "; only one rate was reported by the device; lower-rate options are unavailable.",
    "；选择输出率后点击应用。": "; select an output rate and click Apply.",
    "确认速率不匹配：请求 ": "Sample-rate mismatch: requested ",
    " Hz，设备返回 ": " Hz, but device returned ",
    " Hz；请重新查询。": " Hz. Please query again.",
    "已确认切换为 ": "Confirmed switch to ",
    " Hz；连续数据缓存已清空，请重新学习。": " Hz. Continuous data buffers were cleared; please relearn.",
    "MCU 采样率操作失败：": "MCU sample-rate operation failed: ",
    "MCU 运行状态：上报超时": "MCU Runtime: Report Timeout",
    "MCU 忙碌≈": "MCU Busy ≈",
    "%  |  FFT调度 ": "%  |  FFT scheduling ",
    " ms / ": " ms / ",
    "s  |  LCD ": "s  |  LCD ",
    " ms，最长 ": " ms, max ",
    " FPS  |  TX队列 ": " FPS  |  TX queue ",
    "，峰值 ": ", peak ",
    "MCU FFT：结果超时": "MCU FFT: Result Timeout",
    "MCU FFT：等待设备结果": "MCU FFT: Waiting for Device Result",
    "MCU FFT：等待完整连续数据窗口": "MCU FFT: Waiting for a Complete Continuous Data Window",
    "模型存储：状态超时": "Model Storage: Status Timeout",
    "模型存储：初始化失败 ": "Model Storage: Initialization Failed ",
    "本次启动已从 Flash 恢复模型": "Model restored from Flash during this boot",
    "本次启动未恢复模型": "Model not restored during this boot",
    "本次启动尚无成功保存": "No successful save during this boot",
    "本次启动已成功保存 ": "Successfully saved ",
    " 次": " times",
    "；最近保存错误 ": "; latest save error ",
    "启动加载失败 ": "Startup load failed ",
    "模型存储：": "Model Storage: ",
    "；Flash 序号 ": "; Flash sequence ",
    "本次启动": "This boot",
    "已建立（MCU）": "Established (MCU)",
    "未建立": "Not Established",
    "学习中，请保持固定安装和正常运行。": "Learning in progress. Keep the device securely mounted and operating normally.",
    "检测在 MCU 本地执行；超过阈值需连续5个窗口才报警，恢复也需连续正常窗口。": "Detection runs locally on the MCU. An alarm requires 5 consecutive windows above the threshold; recovery also requires consecutive normal windows.",
    " 当前分数不是故障概率；报警与恢复均有连续窗口确认。": " The current score is not a failure probability; alarms and recovery are confirmed over consecutive windows.",
    "当前格式仅数据载荷就需要 ": "The current format requires ",
    "M baud，另有帧开销；当前 ": "M baud for payload alone, plus frame overhead; current rate is ",
    "M 不足。丢帧后 PC FFT 会等待连续数据；可查看 MCU FFT。": "M is insufficient. After dropped frames, PC FFT waits for continuous data; MCU FFT remains available.",
    "约0.5秒均值，包含重力；不是振动RMS或瞬时峰值。": "Approx. 0.5 s mean including gravity; not vibration RMS or an instantaneous peak.",
    "MCU版本：等待核验": "MCU version: awaiting verification",
    "MCU 版本：等待核验": "MCU version: awaiting verification",
    "MCU 运行状态：": "MCU Runtime: ",
    "模型存储：等待 MCU 状态": "Model Storage: Waiting for MCU status",
    "MCU FFT 未连接": "MCU FFT: Not Connected",
    "PC：CRC定位 R6 | MCU：等待版本回复": "PC: CRC Diagnostics R6 | MCU: Waiting for version",
    # Calibration dialog
    "六位置校准 · MCU 参数保存": "Six-Position Calibration · Save Parameters to MCU",
    "停机后操作：依次让 X+、X−、Y+、Y−、Z+、Z− 朝上。每面放稳后采集 5 秒，收到完成结果再换面。\n校准由 MCU 计算和应用；本软件不会对收到的数据重复校正。": "Perform with the machine stopped. Orient X+, X−, Y+, Y−, Z+, and Z− upward in sequence. Stabilize each face and capture for 5 s; move to the next face only after completion is reported.\nCalibration is calculated and applied by the MCU. This software does not recalibrate received data.",
    "未校准三轴读数 · 约0.5秒均值": "Uncalibrated 3-Axis Readings · Approx. 0.5 s Mean",
    "等待实时数据": "Waiting for live data",
    "这些数值包含重力和零偏；校准前不要求某轴恰好为±1000 mg、其余轴为0。请按传感器轴向标识摆放。": "These values include gravity and bias. Before calibration, one axis is not expected to be exactly ±1000 mg with the other axes at zero. Position the sensor according to its axis markings.",
    "开始新校准": "Start New Calibration",
    "查询设备状态": "Query Device Status",
    "取消本次校准": "Cancel This Calibration",
    "朝上方向": "Face-Up Direction",
    "原始 X (mg)": "Raw X (mg)",
    "原始 Y (mg)": "Raw Y (mg)",
    "原始 Z (mg)": "Raw Z (mg)",
    "校正残差 X / Y / Z (mg)": "Correction Residual X / Y / Z (mg)",
    "结果": "Result",
    "采集所选面（5秒）": "Capture Selected Face (5 s)",
    "本面原始均值：—": "Current Face Raw Mean: —",
    "计算并检查六面结果": "Solve and Check Six-Face Results",
    "零偏/比例：待求解；综合一致性：待核验。旁轴残差为姿态提示。": "Bias/Scale: Pending solution; overall consistency: pending verification. Cross-axis residuals are posture guidance.",
    "写入设备并清除旧学习模型": "Write to Device and Clear Previous Baseline Model",
    "保存后需在正常运行工况下重新学习。六面校准不替代高频振动幅值/频响校验。": "After saving, relearn under normal operating conditions. Six-face calibration does not replace high-frequency vibration amplitude/frequency-response verification.",
    "校准尚未结束，请先点“取消本次校准”；保存过程中请等待最终确认。": "Calibration is not complete. Click “Cancel This Calibration” first; wait for final confirmation while saving.",
    "静止（仍需保持到本面采集结束）": "Stationary (remain still until this face capture is complete)",
    "检测到运动 / 振动，请放稳": "Motion / vibration detected. Please stabilize the device.",
    "实时数据未到达或已超时；需配套 MCU_Calibration_V1_4，且无需点击“开始采集”。": "Live data has not arrived or has timed out. Compatible MCU_Calibration_V1_4 firmware is required; do not click “Start Acquisition”.",
    "（5秒，其余面保留）": "(5 s; other faces are retained)",
    "本面采集 %p%": "Capturing This Face %p%",
    "已采集 ": "Captured ",
    "/6 面": "/6 Faces",
    "最近一面原始均值：": "Latest Face Raw Mean: ",
    "零偏 ": "Bias ",
    " mg；比例 ": " mg; scale ",
    "当前设备参数：等待查询": "Current Device Parameters: Waiting for Query",
    "当前设备参数：": "Current Device Parameters: ",
    "（已校准）": "(Calibrated)",
    "（默认值，尚未校准）": "(Default; Not Calibrated)",
    "本次候选参数：": "Candidate Parameters: ",
    "零偏/比例：通过；综合一致性：": "Bias/Scale: Passed; overall consistency: ",
    "零偏/比例及综合一致性：待完成六面求解。旁轴残差为姿态提示。": "Bias/Scale and overall consistency: complete the six-face solution first. Cross-axis residuals are posture guidance.",
    "通过": "Passed",
    "未通过": "Failed",
    "待采集": "Not Captured",
    "已采集": "Captured",
    "明细待返回": "Details Pending",
    "已核验": "Verified",
    "一致性超限": "Consistency Limit Exceeded",
    "姿态提示": "Posture Warning",
    "采集中…": "Capturing…",
    "待求解核验": "Pending Solution / Verification",
    "重采所选面": "Recapture Selected Face",
    "采集所选面": "Capture Selected Face",
    " 轴": " Axis",
    "方向朝上": " Facing Up",
    "对应传感器 ": "Corresponds to sensor ",
    "轴正方向朝上": "Axis Positive Facing Up",
    "轴负方向朝上": "Axis Negative Facing Up",
    "  |  标准差 X/Y/Z：": "  |  Std. Dev. X/Y/Z: ",
    "本面原始均值：": "Current Face Raw Mean: ",
    "六面合量相对1g偏差 (mg)：": "Six-Face Vector Magnitude Deviation from 1g (mg): ",
    "\nX/Y/Z 正反面对称性偏差 (mg)：": "\nX/Y/Z Positive/Negative Face Symmetry Deviation (mg): ",
    "。旁轴残差>50 mg仅为黄色姿态提示。": ". Cross-axis residuals >50 mg are only a yellow posture warning.",
    "零偏/比例及综合一致性：": "Bias/Scale and Overall Consistency: ",
    "标准差": "Standard Deviation",
    "结果超时": "Result Timeout",
    "未收到": "Not Received",
    "MCU：等待版本回复": "MCU: Waiting for version",

    # Calibration state and protocol feedback
    "连接设备后查询校准状态。": "Connect the device and query calibration status.",
    "MCU版本未确认：需烧录V1.4，确认 main.c 和 calibration.inc 均已替换并重新编译。": "MCU version not verified: flash V1.4, ensure both main.c and calibration.inc have been replaced, then rebuild.",
    "正在核对 MCU 校准协议版本…": "Checking the MCU calibration protocol version…",
    "串口已断开；未确认的采集或保存不视为成功。重连后查询设备状态。": "Serial port disconnected. Unconfirmed capture or save operations are not considered successful. Reconnect and query device status.",
    "设备拒绝求解，但六面诊断明细尚未返回；请查询设备状态并确认MCU版本。": "The device rejected the solution, but six-face diagnostic details have not returned. Query device status and verify the MCU version.",
    "六面数据尚未齐全，请补采缺失面。": "Six-face data is incomplete. Capture the missing faces.",
    "零偏/比例及综合一致性检查通过。": "Bias/scale and overall consistency checks passed.",
    "未收到校准能力回复。请检查是否使用 MCU_Calibration_V1；原有采集功能仍可使用。": "No calibration capability response. Check whether MCU_Calibration_V1 is installed; existing acquisition functions remain available.",
    " · 校准协议": " · Calibration Protocol",
    "MCU 启动标识 V": "MCU boot identifier V",
    "；尚未收到V1.4能力确认": "; V1.4 capability has not been confirmed",
    "合量核验未通过：": "Vector magnitude check failed: ",
    " 面校正后合量偏离1g ": " face magnitude after correction deviates from 1g by ",
    " mg（允许±50 mg），请检查该面倾斜及对应正反面基准。": " mg (limit ±50 mg). Check the face tilt and the corresponding positive/negative face references.",
    "正反面对称性未通过：": "Positive/negative face symmetry check failed: ",
    " 轴两面的校正中点偏差 ": " axis corrected midpoint deviation between the two faces is ",
    " mg（允许50 mg）。请检查这两面及各轴零偏是否稳定。": " mg (limit 50 mg). Check these two faces and verify that each axis bias is stable.",
    "六面核验未通过：最大残差在 ": "Six-face verification failed: maximum residual is on face ",
    " 面的 ": " (axis ",
    " 轴，": "), residual ",
    " mg（门限50 mg）。先检查该面，并核对该轴正反面；最大残差不能唯一确定问题来源。选中一面重采会保留其余数据。": " mg (50 mg limit). Check that face first, then verify the positive/negative faces for that axis. The maximum residual alone cannot identify the cause. Recapturing one face preserves the others.",
    " mg；各轴应约为+2000 mg，请检查是否选错方向、重复同一面或正反面颠倒。": " mg; each axis should be about +2000 mg. Check for an incorrect direction, duplicate face, or reversed positive/negative face.",
    "等待 MCU 开始校准确认…": "Waiting for MCU confirmation to start calibration…",
    "保持静止，正在采集这一面…": "Keep still. Capturing this face…",
    "等待 MCU 计算和检查六面结果…": "Waiting for the MCU to solve and check the six-face results…",
    "正在写入设备，等待最终结果；请勿断电。": "Writing to the device and waiting for the final result. Do not power off.",
    "等待 MCU 取消确认…": "Waiting for MCU cancellation confirmation…",
    "已重新查询设备。上次操作结果未确认，请检查参数；不要将此提示当作保存成功。": "Device queried again. The previous operation was not confirmed. Check the parameters; do not treat this message as a successful save.",
    "MCU报告已采集，但六面明细未完整返回。请检查当前固件版本及串口日志；缺失值不会被当成0。": "The MCU reported capture completion, but the six-face details were incomplete. Check the firmware version and serial log. Missing values are not treated as zero.",
    " 未收到完整确认，结果未知；正在查询设备，请勿重复写入。": " No complete confirmation was received; the result is unknown. Query the device and do not repeat the write.",
    "正反面差值或参数不合格。X/Y/Z 正反面差值：": "Positive/negative face differences or parameters are out of range. X/Y/Z face differences: ",
    "按六个方向逐面放稳，再点击“采集所选面”。": "Stabilize the device in each of the six orientations, then click “Capture Selected Face”.",
    "匹配": "Matched",
    "不匹配，需V1.4": "Mismatch; V1.4 required",
    "校准会话进行中，可继续采集或取消。": "Calibration session in progress. You can continue capturing or cancel.",
    "设备支持六位置校准。先停机，将板子静止放稳。": "The device supports six-position calibration. Stop the machine and place the board securely on a stable surface.",
    "零偏/比例与综合一致性检查通过，可以保存。旁轴残差超过50 mg仅提示检查姿态；写入后须重新学习。": "Bias/scale and overall consistency checks passed; you can save. Cross-axis residuals above 50 mg only indicate that posture should be checked. Relearn after writing.",
    "保存成功，已读回当前参数。请安装到正常工况，按设备当前采样率重新学习（IIS3DWB 支持原生及软件降采样档）；掉电恢复需重启后另行验证。": "Save succeeded and the current parameters were read back. Install the device in its normal operating condition and relearn at the current sample rate (IIS3DWB supports native and software-decimated rates). Power-loss recovery must be verified separately after reboot.",
    "保存回复与读回参数不一致，请检查设备。": "The save response does not match the parameters read back. Check the device.",
    "采集方向回复不匹配，请查询设备状态。": "The captured-face direction response does not match. Query device status.",
    "本面静止检查通过，可以换下一面；方向和零偏将在六面求解时核验。": "Stationarity check passed for this face. You can move to the next face; direction and bias will be verified during the six-face solution.",
    "本面未通过：": "This face failed: ",
    "采集期间有振动，请放稳重试；方向会在六面求解时检查。": "Vibration was detected during capture. Stabilize the device and retry; direction will be checked during the six-face solution.",
    "采集数据中断或超时，请重试。": "Capture data was interrupted or timed out. Please retry.",
    "收到延迟的保存回复，请查询当前参数并检查设备。": "A delayed save response was received. Query the current parameters and check the device.",
    "MCU 已确认保存，正在读回参数…": "MCU confirmed the save. Reading back parameters…",
    "已取消未保存的校准；原有参数保持。": "Uncommitted calibration was cancelled; the previous parameters are retained.",
    "保存未完整确认：写入返回 ": "Save was not fully confirmed: write returned ",
    "，传感器恢复 ": ", sensor recovery ",
    "。请查询参数；可能已提交，需要重新学习。": ". Query the parameters. The write may have been committed; relearning is required.",
    "固件不支持校准命令，请使用 MCU_Calibration_V1。": "Firmware does not support calibration commands. Use MCU_Calibration_V1.",
    "MCU 拒绝操作：": "MCU rejected the operation: ",
    " [设备返回 ": " [device returned ",
    # Baseline-learning transaction feedback
    "MCU已接收学习指令": "MCU accepted the learning command",
    "MCU已取消学习": "MCU cancelled learning",
    "学习指令已排队，等待串口发送。": "Learning command queued; waiting for serial transmission.",
    "取消指令已排队，等待发送。": "Cancel command queued; waiting to be sent.",
    "尚未收到 MCU 确认，正在有限重试。": "No MCU acknowledgement yet; retrying a limited number of times.",
    "取消已发送，等待 MCU 确认。": "Cancel command sent; waiting for MCU acknowledgement.",
    "串口已断开，操作结果未确认。": "Serial port disconnected; operation result is unconfirmed.",
    "学习指令已发送（第": "Learning command sent (attempt ",
    "次），等待 MCU 确认。": "); waiting for MCU acknowledgement.",
    "MCU已接收学习指令，等待学习状态；请保持固定安装和正常工况。": "MCU accepted the learning command. Waiting for the learning state; keep the device securely mounted under normal operating conditions.",
    "MCU已进入正常状态学习，约1秒预热＋30秒有效数据。": "MCU entered baseline learning: approx. 1 s warm-up + 30 s of valid data.",
    "MCU已退出学习状态。": "MCU exited the learning state.",
    "MCU已接收指令，但未确认持续学习状态；请检查采集错误或复位日志。": "MCU accepted the command but did not confirm an ongoing learning state. Check acquisition errors or reset logs.",
    "操作未收到完整确认，已停止重试，请查看串口日志。": "The operation did not receive complete confirmation. Retries have stopped; check the serial log.",
    "MCU已确认取消学习。": "MCU confirmed cancellation of learning.",
    "正在切换采样率，请稍后再试": "Sample-rate change in progress; try again later",
    "。本次不视为学习成功。": ". This operation is not considered a successful learning session.",
    "正在保存模型，请稍后再试": "Model is being saved; try again later",
    "MCU拒绝操作：": "MCU rejected the operation: ",
    "六位置校准会话尚未结束，请先取消或保存校准": "The six-position calibration session is still active. Cancel or save calibration first.",
    "传感器尚未就绪": "Sensor is not ready",
    "设备正忙（可能正在学习、保存或切换采样率）": "Device is busy (it may be learning, saving, or changing the sample rate)",

    "退出前请先取消校准；保存过程中请等待最终确认。": "Cancel calibration before exiting; wait for final confirmation while saving.",
    "模型：": "Model: ",
    "未收到版本标识；请查询采样率": "No firmware version received; query the sample rate",
    " Hz。当前波特率理论带宽足够，实际是否连续以不连续事件、CRC和MCU FIFO统计为准。": " Hz. The baud rate is theoretically sufficient; verify continuity using discontinuity events, CRC errors, and MCU FIFO statistics.",
    "已完成 ": "Completed ",
    " 组 · 跳过 ": " windows · skipped ",
    " 个分析窗口": " analysis windows",
    " · 发布后样本时间 ": " · sample age after publication ",
    " ms · 调度批次最大 ": " ms · maximum scheduling batch ",
    " ms；幅值为峰值，非 RMS。": " ms; amplitude is peak, not RMS.",
    " 【结果超过1秒未更新】": " [Result not updated for over 1 s]",
    "最长 ": "max ",
    "队列": "queue",
    "峰值 ": "peak ",

    "未学习": "Not Learned",
    "学习中": "Learning",
    "滤波预热": "Filter Warm-up",
    "正常": "Normal",
    "疑似异常": "Suspected Anomaly",
    "异常报警": "Anomaly Alarm",
}

# Reverse lookup is used to normalize already-translated text before switching languages.
EN_ZH = {v: k for k, v in ZH_EN.items() if v}


def _replace_longest(text: str, mapping: dict[str, str]) -> str:
    for source in sorted(mapping, key=len, reverse=True):
        if source and source in text:
            text = text.replace(source, mapping[source])
    return text


class LanguageManager:
    """Reversible text translation applied to the live Qt widget tree."""

    def __init__(self):
        self.language = "zh"

    def set_language(self, language: str):
        self.language = "en" if str(language).lower().startswith("en") else "zh"

    def text(self, value):
        if not isinstance(value, str) or not value:
            return value
        # Normalize translated text to Chinese first so toggling is reversible.
        canonical = _replace_longest(value, EN_ZH)
        if self.language == "en":
            return _replace_longest(canonical, ZH_EN)
        return canonical

    def apply(self, root):
        if root is None:
            return
        from PySide6 import QtWidgets

        widgets = [root] + root.findChildren(QtWidgets.QWidget)
        for widget in widgets:
            # Standard text-bearing widgets.
            if isinstance(widget, QtWidgets.QComboBox):
                for index in range(widget.count()):
                    old = widget.itemText(index)
                    new = self.text(old)
                    if new != old:
                        widget.setItemText(index, new)
            elif isinstance(widget, QtWidgets.QTableWidget):
                for col in range(widget.columnCount()):
                    item = widget.horizontalHeaderItem(col)
                    if item:
                        old = item.text()
                        new = self.text(old)
                        if new != old:
                            item.setText(new)
                for row in range(widget.rowCount()):
                    for col in range(widget.columnCount()):
                        item = widget.item(row, col)
                        if item:
                            old = item.text()
                            new = self.text(old)
                            if new != old:
                                item.setText(new)
            elif isinstance(widget, QtWidgets.QProgressBar):
                old = widget.format()
                new = self.text(old)
                if new != old:
                    widget.setFormat(new)
            elif isinstance(widget, QtWidgets.QGroupBox):
                old = widget.title()
                new = self.text(old)
                if new != old:
                    widget.setTitle(new)
            elif isinstance(widget, (QtWidgets.QLabel, QtWidgets.QAbstractButton)):
                old = widget.text()
                new = self.text(old)
                if new != old:
                    widget.setText(new)

            # Tooltips and top-level window titles.
            if isinstance(widget, QtWidgets.QWidget):
                old_tip = widget.toolTip()
                new_tip = self.text(old_tip)
                if new_tip != old_tip:
                    widget.setToolTip(new_tip)
            if isinstance(widget, (QtWidgets.QMainWindow, QtWidgets.QDialog)):
                old_title = widget.windowTitle()
                new_title = self.text(old_title)
                if new_title != old_title:
                    widget.setWindowTitle(new_title)

            # Translate the rolling text log without changing its scroll position.
            if isinstance(widget, QtWidgets.QPlainTextEdit):
                old = widget.toPlainText()
                new = self.text(old)
                if new != old:
                    bar = widget.verticalScrollBar()
                    value = bar.value()
                    cursor = widget.textCursor()
                    position = cursor.position()
                    widget.setPlainText(new)
                    cursor = widget.textCursor()
                    cursor.setPosition(min(position, len(new)))
                    widget.setTextCursor(cursor)
                    bar.setValue(value)

            # pyqtgraph plot titles and axis labels are not all regular child labels.
            if hasattr(widget, "getPlotItem"):
                try:
                    plot = widget.getPlotItem()
                    title_label = getattr(plot, "titleLabel", None)
                    if title_label is not None and hasattr(title_label, "text"):
                        old = title_label.text
                        new = self.text(old)
                        if new != old:
                            title_label.setText(new)
                    for axis_name in ("left", "bottom"):
                        axis = plot.getAxis(axis_name)
                        label_text = getattr(axis, "labelText", None)
                        if label_text:
                            new_label = self.text(label_text)
                            if new_label != label_text:
                                axis.setLabel(text=new_label, units=axis.labelUnits)
                except Exception:
                    pass
