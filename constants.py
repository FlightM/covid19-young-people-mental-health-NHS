"""Module containing constants used throughout data use and processing, such as file
URIS.
"""
# Standard library imports
import os


# File Names
_name_2017_18 = "hosp-epis-stat-admi-diag-2017-18-tab.xlsx"
_name_2018_19 = "hosp-epis-stat-admi-diag-2018-19-tab.xlsx"
_name_2019_20 = "hosp-epis-stat-admi-diag-2019-20-tab supp.xlsx"
_name_2020_21 = "hosp-epis-stat-admi-diag-2020-21-tab.xlsx"
_name_2021_22 = "hosp-epis-stat-admi-diag-2021-22-tab.xlsx"
_name_2022_23 = "hosp-epis-stat-admi-diag-2022-23-tab_V2.xlsx"
_name_2023_24 = "hosp-epis-stat-admi-diag-2023-24-tab.xlsx"


# File URIs
excel_uri_2017_18 = os.path.normpath(os.path.join(
    os.path.dirname(__file__),
    f"../NHS Hospital Admissions/{_name_2017_18}"
))
excel_uri_2018_19 = os.path.normpath(os.path.join(
    os.path.dirname(__file__),
    f"../NHS Hospital Admissions/{_name_2018_19}"
))
excel_uri_2019_20 = os.path.normpath(os.path.join(
    os.path.dirname(__file__),
    f"../NHS Hospital Admissions/{_name_2019_20}"
))
excel_uri_2020_21 = os.path.normpath(os.path.join(
    os.path.dirname(__file__),
    f"../NHS Hospital Admissions/{_name_2020_21}"
))
excel_uri_2021_22 = os.path.normpath(os.path.join(
    os.path.dirname(__file__),
    f"../NHS Hospital Admissions/{_name_2021_22}"
))
excel_uri_2022_23 = os.path.normpath(os.path.join(
    os.path.dirname(__file__),
    f"../NHS Hospital Admissions/{_name_2022_23}"
))
excel_uri_2023_24 = os.path.normpath(os.path.join(
    os.path.dirname(__file__),
    f"../NHS Hospital Admissions/{_name_2023_24}"
))