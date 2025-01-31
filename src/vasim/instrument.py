# -*- coding: utf-8 -*-

"""
vasim.instrument
-------------------

This module contains the class an ODK XLS form.
"""
from pandas import DataFrame, read_excel
from pkgutil import get_data
from io import BytesIO


class Instrument:
    """
    Representation of ODK XLS form
    """
    pass


def get_who2022() -> tuple[DataFrame, DataFrame]:
    """
    Get 2022 WHO VA instrument.

    :return: the survey and choices sheets from the XLSX form
    :rtype: tuple[DataFrame, DataFrame]
    """

    who2022_bytes = get_data(__name__, "data/WHOVA2022_XLS_form_for_ODK.xlsx")
    survey = read_excel(BytesIO(who2022_bytes), sheet_name="survey")
    choices = read_excel(BytesIO(who2022_bytes), sheet_name="choices")
    return survey, choices


def get_instrument(xlsx_name: str) -> tuple[DataFrame, DataFrame]:
    """
        Get XLSX instrument.

        :param xlsx_name: Name of XLSX file with two sheets labeled
        survey and choices.

        :return: the survey and choices sheets from the XLSX form
        :rtype: tuple[DataFrame, DataFrame]
        """

    xlsx_bytes = get_data(__name__, xlsx_name)
    survey = read_excel(BytesIO(xlsx_bytes), sheet_name="survey")
    choices = read_excel(BytesIO(xlsx_bytes), sheet_name="choices")
    return survey, choices
