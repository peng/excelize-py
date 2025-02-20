"""Copyright 2024 The excelize Authors. All rights reserved. Use of this source
code is governed by a BSD-style license that can be found in the LICENSE file.

Package excelize-py is a Python port of Go Excelize library, providing a set of
functions that allow you to write and read from XLAM / XLSM / XLSX / XLTM / XLTX
files. Supports reading and writing spreadsheet documents generated by Microsoft
Excel™ 2007 and later. Supports complex components by high compatibility, and
provided streaming API for generating or reading data from a worksheet with huge
amounts of data. This library needs Python version 3.9 or later.
"""

from dataclasses import dataclass
from enum import IntEnum
from typing import Optional


class CultureName(IntEnum):
    """
    This section defines the currently supported country code types enumeration
    for apply number format.
    """

    CultureNameUnknown = 0
    CultureNameEnUS = 1
    CultureNameJaJP = 2
    CultureNameKoKR = 3
    CultureNameZhCN = 4
    CultureNameZhTW = 5


class CellType(IntEnum):
    """
    This section defines the cell value types enumeration.
    """

    CellTypeUnset = 0
    CellTypeBool = 1
    CellTypeDate = 2
    CellTypeError = 3
    CellTypeFormula = 4
    CellTypeInlineString = 5
    CellTypeNumber = 6
    CellTypeSharedString = 7


class FormControlType(IntEnum):
    """
    FormControlType is the type of supported form controls.
    """

    FormControlNote = 0
    FormControlButton = 1
    FormControlOptionButton = 2
    FormControlSpinButton = 3
    FormControlCheckBox = 4
    FormControlGroupBox = 5
    FormControlLabel = 6
    FormControlScrollBar = 7


class ChartLineType(IntEnum):
    """
    ChartLineType defines the currently supported chart line types enumeration.
    """

    ChartLineUnset = 0
    ChartLineSolid = 1
    ChartLineNone = 2
    ChartLineAutomatic = 3


class ChartType(IntEnum):
    """
    ChartType defines the currently supported chart types enumeration.
    """

    Area = 0
    AreaStacked = 1
    AreaPercentStacked = 2
    Area3D = 3
    Area3DStacked = 4
    Area3DPercentStacked = 5
    Bar = 6
    BarStacked = 7
    BarPercentStacked = 8
    Bar3DClustered = 9
    Bar3DStacked = 10
    Bar3DPercentStacked = 11
    Bar3DConeClustered = 12
    Bar3DConeStacked = 13
    Bar3DConePercentStacked = 14
    Bar3DPyramidClustered = 15
    Bar3DPyramidStacked = 16
    Bar3DPyramidPercentStacked = 17
    Bar3DCylinderClustered = 18
    Bar3DCylinderStacked = 19
    Bar3DCylinderPercentStacked = 20
    Col = 21
    ColStacked = 22
    ColPercentStacked = 23
    Col3D = 24
    Col3DClustered = 25
    Col3DStacked = 26
    Col3DPercentStacked = 27
    Col3DCone = 28
    Col3DConeClustered = 29
    Col3DConeStacked = 30
    Col3DConePercentStacked = 31
    Col3DPyramid = 32
    Col3DPyramidClustered = 33
    Col3DPyramidStacked = 34
    Col3DPyramidPercentStacked = 35
    Col3DCylinder = 36
    Col3DCylinderClustered = 37
    Col3DCylinderStacked = 38
    Col3DCylinderPercentStacked = 39
    Doughnut = 40
    Line = 41
    Line3D = 42
    Pie = 43
    Pie3D = 44
    PieOfPie = 45
    BarOfPie = 46
    Radar = 47
    Scatter = 48
    Surface3D = 49
    WireframeSurface3D = 50
    Contour = 51
    WireframeContour = 52
    Bubble = 53
    Bubble3D = 54


class ChartDataLabelPositionType(IntEnum):
    """
    ChartDataLabelPositionType is the type of chart data labels position.
    """

    ChartDataLabelsPositionUnset = 0
    ChartDataLabelsPositionBestFit = 1
    ChartDataLabelsPositionBelow = 2
    ChartDataLabelsPositionCenter = 3
    ChartDataLabelsPositionInsideBase = 4
    ChartDataLabelsPositionInsideEnd = 5
    ChartDataLabelsPositionLeft = 6
    ChartDataLabelsPositionOutsideEnd = 7
    ChartDataLabelsPositionRight = 8
    ChartDataLabelsPositionAbove = 9


class ChartTickLabelPositionType(IntEnum):
    """
    ChartTickLabelPositionType is the type of supported chart tick label
    """

    ChartTickLabelNextToAxis = 0
    ChartTickLabelHigh = 1
    ChartTickLabelLow = 2
    ChartTickLabelNone = 3


class PictureInsertType(IntEnum):
    """
    PictureInsertType defines the type of the picture has been inserted into the
    worksheet.
    """

    PictureInsertTypePlaceOverCells = 0
    PictureInsertTypePlaceInCell = 1
    PictureInsertTypeDISPIMG = 2


@dataclass
class Interface:
    type: int = 0
    integer: int = 0
    string: str = ""
    float64: float = 0
    boolean: bool = False


@dataclass
class Options:
    max_calc_iterations: int = 0
    password: str = ""
    raw_cell_value: bool = False
    unzip_size_limit: int = 0
    unzip_xml_size_limit: int = 0
    short_date_pattern: str = ""
    long_date_pattern: str = ""
    long_time_pattern: str = ""
    culture_info: CultureName = CultureName.CultureNameUnknown


@dataclass
class AppProperties:
    application: str = ""
    scale_crop: bool = False
    doc_security: int = 0
    company: str = ""
    links_up_to_date: bool = False
    hyperlinks_changed: bool = False
    app_version: str = ""


@dataclass
class Border:
    type: str = ""
    color: str = ""
    style: int = 0


@dataclass
class Fill:
    type: str = ""
    pattern: int = 0
    color: Optional[list[str]] = None
    shading: int = 0


@dataclass
class Font:
    bold: bool = False
    italic: bool = False
    underline: str = ""
    family: str = ""
    size: float = 0
    strike: bool = False
    color: str = ""
    color_indexed: int = 0
    color_theme: Optional[int] = None
    color_tint: float = 0
    vert_align: str = ""


@dataclass
class Alignment:
    horizontal: str = ""
    indent: int = 0
    justify_last_line: bool = False
    reading_order: int = 0
    relative_indent: int = 0
    shrink_to_fit: bool = False
    text_rotation: int = 0
    vertical: str = ""
    wrap_text: bool = False


@dataclass
class Protection:
    hidden: bool = False
    locked: bool = False


@dataclass
class Style:
    border: Optional[list[Border]] = None
    fill: Fill = Fill
    font: Optional[Font] = None
    alignment: Optional[Alignment] = None
    protection: Optional[Protection] = None
    num_fmt: int = 0
    decimal_places: Optional[int] = None
    custom_num_fmt: Optional[str] = None
    neg_red: bool = False


@dataclass
class Row:
    cell: Optional[list[str]] = None


@dataclass
class GetRowsResult:
    row: Optional[list[Row]] = None


@dataclass
class GraphicOptions:
    alt_text: str = ""
    print_object: Optional[bool] = None
    locked: Optional[bool] = None
    lock_aspect_ratio: bool = False
    auto_fit: bool = False
    auto_fit_ignore_aspect: bool = False
    offset_x: int = 0
    offset_y: int = 0
    scale_x: float = 0
    scale_y: float = 0
    hyperlink: str = ""
    hyperlink_type: str = ""
    positioning: str = ""


@dataclass
class RichTextRun:
    font: Optional[Font] = None
    text: str = ""


@dataclass
class Comment:
    author: str = ""
    author_id: int = 0
    cell: str = ""
    text: str = ""
    width: int = 0
    height: int = 0
    paragraph: Optional[list[RichTextRun]] = None


@dataclass
class ChartNumFmt:
    custom_num_fmt: str = ""
    source_linked: bool = False


@dataclass
class ChartAxis:
    none: bool = False
    major_grid_lines: bool = False
    minor_grid_lines: bool = False
    major_unit: float = 0
    tick_label_position: ChartDataLabelPositionType = (
        ChartDataLabelPositionType.ChartDataLabelsPositionUnset
    )
    tick_label_skip: int = 0
    reverse_order: bool = False
    secondary: bool = False
    maximum: Optional[float] = None
    minimum: Optional[float] = None
    alignment: Alignment = Alignment
    font: Font = Font
    log_base: float = 0
    num_fmt: ChartNumFmt = ChartNumFmt
    title: Optional[RichTextRun] = None


@dataclass
class ChartDimension:
    width: int = 0
    height: int = 0


@dataclass
class ChartPlotArea:
    second_plot_values: int = 0
    show_bubble_size: bool = False
    show_cat_name: bool = False
    show_leader_lines: bool = False
    show_percent: bool = False
    show_ser_name: bool = False
    show_val: bool = False
    fill: Fill = Fill
    num_fmt: ChartNumFmt = ChartNumFmt


@dataclass
class ChartLegend:
    position: str = ""
    show_legend_key: bool = False


@dataclass
class ChartMarker:
    fill: Fill = Fill
    symbol: str = ""
    size: int = 0


@dataclass
class ChartLine:
    type: ChartLineType = ChartLineType.ChartLineUnset
    smooth: bool = False
    width: float = 0


@dataclass
class ChartSeries:
    name: str = ""
    categories: str = ""
    values: str = ""
    sizes: str = ""
    fill: Fill = Fill
    line: ChartLine = ChartLine
    marker: ChartMarker = ChartMarker
    data_label_position: ChartDataLabelPositionType = (
        ChartDataLabelPositionType.ChartDataLabelsPositionUnset
    )


@dataclass
class Chart:
    type: ChartType = ChartType.Area
    series: Optional[list[ChartSeries]] = None
    format: GraphicOptions = GraphicOptions
    dimension: ChartDimension = ChartDimension
    legend: ChartLegend = ChartLegend
    title: Optional[list[RichTextRun]] = None
    vary_colors: Optional[bool] = None
    x_axis: ChartAxis = ChartAxis
    y_axis: ChartAxis = ChartAxis
    plot_area: ChartPlotArea = ChartPlotArea
    fill: Fill = Fill
    border: ChartLine = ChartLine
    show_blanks_as: str = ""
    bubble_size: int = 0
    hole_size: int = 0


@dataclass
class PivotTableField:
    compact: bool = False
    data: str = ""
    name: str = ""
    outline: bool = False
    show_all: bool = False
    insert_blank_row: bool = False
    subtotal: str = ""
    default_subtotal: bool = False
    num_fmt: int = 0


@dataclass
class PivotTableOptions:
    data_range: str = ""
    pivot_table_range: str = ""
    name: str = ""
    rows: Optional[list[PivotTableField]] = None
    columns: Optional[list[PivotTableField]] = None
    data: Optional[list[PivotTableField]] = None
    filter: Optional[list[PivotTableField]] = None
    row_grand_totals: bool = False
    col_grand_totals: bool = False
    show_drill: bool = False
    use_auto_formatting: bool = False
    page_over_then_down: bool = False
    merge_item: bool = False
    classic_layout: bool = False
    compact_data: bool = False
    show_error: bool = False
    show_row_headers: bool = False
    show_col_headers: bool = False
    show_row_stripes: bool = False
    show_col_stripes: bool = False
    show_last_column: bool = False
    field_print_titles: bool = False
    item_print_titles: bool = False
    pivot_table_style_name: str = ""
