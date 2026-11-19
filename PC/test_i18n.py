from i18n import LanguageManager


def test_main_ui_text_round_trip():
    manager = LanguageManager()
    samples = [
        "IIS3DWB 三轴振动监测 · CRC定位 R6",
        "等待 MCU 查询结果；切换后需重新学习",
        "当前设备参数：零偏 1.000, 2.000, 3.000 mg；比例 1.000000",
        "MCU已接收学习指令，等待学习状态；请保持固定安装和正常工况。",
        "X+ 对应传感器 X 轴正方向朝上",
        "模型：已建立（MCU）",
    ]
    for source in samples:
        manager.set_language("en")
        english = manager.text(source)
        assert english != source
        manager.set_language("zh")
        assert manager.text(english) == source


def test_detection_states_are_translated():
    manager = LanguageManager()
    manager.set_language("en")
    assert [manager.text(s) for s in ("未学习", "学习中", "滤波预热", "正常", "疑似异常", "异常报警")] == [
        "Not Learned", "Learning", "Filter Warm-up", "Normal", "Suspected Anomaly", "Anomaly Alarm"
    ]


def test_language_selector_labels_are_reversible():
    manager = LanguageManager()
    manager.set_language("en")
    assert manager.text("中文") == "Chinese"
    manager.set_language("zh")
    assert manager.text("Chinese") == "中文"
