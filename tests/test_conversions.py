

def test_pressure_converter():
    from flowcv.conversions import pressure_converter
    assert pressure_converter(92, "kpa") == 13.343471871179249
    assert pressure_converter(74, "bar") == 1073.2792612534279
    assert pressure_converter(44, "mpa") == 6381.66046012


def test_flow_converter():
    from flowcv.conversions import flow_converter
    assert flow_converter(800, "lph") == 3.522296
    assert flow_converter(424, "lpm") == 112.00929888518928
    assert flow_converter(952, "lps") == 15089.554604532856
    assert flow_converter(521, "m3hr") == 2293.901128898727
