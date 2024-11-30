"""Copyright 2024 The excelize Authors. All rights reserved. Use of this source
code is governed by a BSD-style license that can be found in the LICENSE file.

Package excelize-py is a Python port of Go Excelize library, providing a set of
functions that allow you to write and read from XLAM / XLSM / XLSX / XLTM / XLTX
files. Supports reading and writing spreadsheet documents generated by Microsoft
Excel™ 2007 and later. Supports complex components by high compatibility, and
provided streaming API for generating or reading data from a worksheet with huge
amounts of data. This library needs Python version 3.9 or later.
"""

from ctypes import (
    c_bool,
    c_char_p,
    c_char,
    c_double,
    c_int,
    c_long,
    c_uint,
    Structure,
    POINTER,
)


class _Interface(Structure):
    _fields_ = [
        ("Type", c_int),
        ("Integer", c_int),
        ("String", c_char_p),
        ("Float64", c_double),
        ("Boolean", c_bool),
    ]


class _Options(Structure):
    _fields_ = [
        ("MaxCalcIterations", c_uint),
        ("Password", c_char_p),
        ("RawCellValue", c_bool),
        ("UnzipSizeLimit", c_long),
        ("UnzipXMLSizeLimit", c_long),
        ("ShortDatePattern", c_char_p),
        ("LongDatePattern", c_char_p),
        ("LongTimePattern", c_char_p),
        ("CultureInfo", c_uint),
    ]


class _Border(Structure):
    _fields_ = [
        ("Type", c_char_p),
        ("Color", c_char_p),
        ("Style", c_int),
    ]


class _Fill(Structure):
    _fields_ = [
        ("Type", c_char_p),
        ("Pattern", c_int),
        ("ColorLen", c_int),
        ("Color", POINTER(POINTER(c_char))),
        ("Shading", c_int),
    ]


class _Font(Structure):
    _fields_ = [
        ("Bold", c_bool),
        ("Italic", c_bool),
        ("Underline", c_char_p),
        ("Family", c_char_p),
        ("Size", c_double),
        ("Strike", c_bool),
        ("Color", c_char_p),
        ("ColorIndexed", c_int),
        ("ColorTheme", POINTER(c_int)),
        ("ColorTint", c_double),
        ("VertAlign", c_char_p),
    ]


class _Alignment(Structure):
    _fields_ = [
        ("Horizontal", c_char_p),
        ("Indent", c_int),
        ("JustifyLastLine", c_bool),
        ("ReadingOrder", c_uint),
        ("RelativeIndent", c_int),
        ("ShrinkToFit", c_bool),
        ("TextRotation", c_int),
        ("Vertical", c_char_p),
        ("WrapText", c_bool),
    ]


class _Protection(Structure):
    _fields_ = [
        ("Hidden", c_bool),
        ("Locked", c_bool),
    ]


class _Style(Structure):
    _fields_ = [
        ("BorderLen", c_int),
        ("Border", POINTER(_Border)),
        ("Fill", _Fill),
        ("Font", POINTER(_Font)),
        ("Alignment", POINTER(_Alignment)),
        ("Protection", POINTER(_Protection)),
        ("NumFmt", c_int),
        ("DecimalPlaces", POINTER(c_int)),
        ("CustomNumFmt", POINTER(c_char_p)),
        ("NegRed", c_bool),
    ]


class _GetCellValueResult(Structure):
    _fields_ = [
        ("val", c_char_p),
        ("err", c_char_p),
    ]


class _Row(Structure):
    _fields_ = [
        ("CellLen", c_int),
        ("Cell", POINTER(POINTER(c_char))),
    ]


class _GetRowsResult(Structure):
    _fields_ = [
        ("RowLen", c_int),
        ("Row", POINTER(_Row)),
        ("err", c_char_p),
    ]


class _NewSheetResult(Structure):
    _fields_ = [
        ("idx", c_int),
        ("err", c_char_p),
    ]


class _NewStyleResult(Structure):
    _fields_ = [
        ("style", c_int),
        ("err", c_char_p),
    ]


class _GetStyleResult(Structure):
    _fields_ = [
        ("style", _Style),
        ("err", c_char_p),
    ]


class _OptionsResult(Structure):
    _fields_ = [
        ("idx", c_int),
        ("err", c_char_p),
    ]
