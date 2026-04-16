"""
This module contains functions that clean, format, and aggregate data for
visualisation.
"""
# Third party imports
import pandas as pd

# Local application imports
import constants


# tuples of URIs to NHS data Excel files and relevant attributes of the files
# relevant to importing data from the Primary 3 Character Diagnosis worksheet.
# tuples are of the following format:
# (workbook URI, extraneous data rows at the end of the Primary 3 Character Diagnosis
# worksheet, year that the data from the workbook should be associated with)
EXCEL_URIS_PRIMARY_3CHAR_ATTRS: dict[str, tuple[str, range, int]] = {
    "2017-2018": (constants.excel_uri_2017_18, range(1628,1641), 2018),
    "2018-2019": (constants.excel_uri_2018_19, range(1626,1639), 2019),
    "2019-2020": (constants.excel_uri_2019_20, range(1615,1628), 2020),
    "2020-2021": (constants.excel_uri_2020_21, range(1603,1616), 2021),
    "2021-2022": (constants.excel_uri_2021_22, range(1616,1628), 2022),
    "2022-2023": (constants.excel_uri_2022_23, range(1617,1624), 2023),
    "2023-2024": (constants.excel_uri_2023_24, range(1627,1634), 2024),
}


# Maps select NHS Primary 3 Character Diagnosis column names to their column indices.
COL_NAME_INDEX_MAP = {
    "Diagnosis Code": 0,
    "Diagnosis Name": 1,
    "Consults": 7,
    "Admissions": 8,
    "Male": 9,
    "Female": 10,
    "Mean Time Waited (Days)": 16,
    "Median Time Waited (Days)": 17,
    "Mean Age": 20,
    "Age 0": 21,
    "Age 1-4": 22,
    "Age 5-9": 23,
    "Age 10-14": 24,
    "Age 15": 25,
    "Age 16": 26,
    "Age 17": 27,
    "Age 18": 28,
    "Age 19": 29,
    "Age 20-24": 30,
    "Age 25-29": 31,
    "Age 30-34": 32,
    "Age 35-39": 33
}


def aggregate_data_w_ages(
        uri: str,
        skip_range: range,
        year: int,
        filter_regex: str,
        agg_characters: int,
        diagnosis_name: str = ""
    ):
    """Loads data from the specified dataset with age distributions columns
    aggregated by the specified number of diagnosis code characters.

    Data is filtered according to the regex string provided. The regex string should
    specify which diagnosis codes should be included in the returned data. For
    example, the regex string "^F3|^F4|^F5" will filter the data to only diagnosis
    codes which begin with "F3", "F4", or "F5"; the regex string "^F9[0-8]" will filter
    the data to only diagnosis codes F90-F98; etc.

    Data is aggregated according to the number of characters of the diagnosis code
    specified by agg_characters. For example, if agg_characters is 1, data will be
    aggregated by the first letter of the diagnosis code, e.g. All diagnosis codes
    which begin with "A" will be aggregated, all which begin with "B" will be
    aggregated, etc.
    
    Columns in the returned dataset, case sensitive and in order, are:
        "Year"
        "Diagnosis Name"
        "Consults"
        "Admissions"
        "Male"
        "Female"
        "Mean Time Waited (Days)"
        "Median Time Waited (Days)"
        "Mean Age"
        "Age 0"
        "Age 1-4"
        "Age 5-9"
        "Age 10-14"
        "Age 15"
        "Age 16"
        "Age 17"
        "Age 18"
        "Age 19"
        "Age 20-24"
        "Age 25-29"
        "Age 30-34"
        "Age 35-39"
    
    Args:
        uri: str URI of dataset to load
        skip_range: range of rows that should be skipped at the bottom of the
            spreadsheet
        year: int of the year which the data should be associated (e.g. 2018)
        filter_regex: regex string to use to filter the data by diagnosis code.
        agg_characters: number of diagnosis code characters which should be used to
            aggregate the data.
        diagnosis_name: string which should be inserted for every value in the
            "Diagnosis Name" column. If not provided, the value will be the string
            summation of every diagnosis name aggregated.
    
    Returns:
        DataFrame containing the data from the columns outlined above from the dataset.
    """
    # Extract all data in relevant columns from workbook
    extract_cols = [
        "Diagnosis Code", 
        "Diagnosis Name",
        "Consults",
        "Admissions",
        "Male",
        "Female",
        "Mean Time Waited (Days)",
        "Median Time Waited (Days)",
        "Mean Age",
        "Age 0",
        "Age 1-4",
        "Age 5-9",
        "Age 10-14",
        "Age 15",
        "Age 16",
        "Age 17",
        "Age 18",
        "Age 19",
        "Age 20-24",
        "Age 25-29",
        "Age 30-34",
        "Age 35-39"
    ]
    df = pd.read_excel(
        uri,
        sheet_name = "Primary Diagnosis 3 Character",
        header=12,
        index_col=0,
        names=extract_cols,
        usecols=[COL_NAME_INDEX_MAP[n] for n in extract_cols],
        skiprows = list(skip_range)
    )

    # Filter dataset using specified regex and insert a year column
    if filter_regex:
        filtered_df = df.filter(regex=filter_regex, axis=0)
    else:
        filtered_df = df
    filtered_df.insert(0, "Year", year)
    filtered_df.replace("*", 3, inplace=True)

    # Aggregate data by the specified number of diagnosis code characters
    if agg_characters == 0:
        summed_series = df.sum(axis=0)
        agg_df = summed_series.to_frame().transpose()
        # Need to redo year col since it will have been summed
        agg_df.drop("Year", axis=1, inplace=True)
        agg_df.insert(0, "Year", year)
    else:
        filtered_df = filtered_df.groupby(by=lambda x: x[:agg_characters])
        agg_df = filtered_df.agg(
            {
                "Year": "first",
                "Diagnosis Name": "sum",
                "Consults": "sum",
                "Admissions": "sum",
                "Male": "sum",
                "Female": "sum",
                "Mean Time Waited (Days)": "mean",
                "Median Time Waited (Days)": "mean",
                "Mean Age": "mean",
                "Age 0": "sum",
                "Age 1-4": "sum",
                "Age 5-9": "sum",
                "Age 10-14": "sum",
                "Age 15": "sum",
                "Age 16": "sum",
                "Age 17": "sum",
                "Age 18": "sum",
                "Age 19": "sum",
                "Age 20-24": "sum",
                "Age 25-29": "sum",
                "Age 30-34": "sum",
                "Age 35-39": "sum"
            }
        )

    if diagnosis_name:
        agg_df = agg_df.drop("Diagnosis Name", axis=1)\
            .insert(1, "Diagnosis Name", diagnosis_name)

    return agg_df


def compile_annual_data_w_ages(diagnosis_code_regex: str, agg_level: int):
    """Compile data of diagnoses codes which meet the specified regex from years
    2017-2018 to 2023-2024.
    
    Args:
        diagnosis_code_regex: str regex to filter diagnosis codes
    
    Returns:
        DataFrame of data.
    """
    raw_dfs = []
    for _, v in EXCEL_URIS_PRIMARY_3CHAR_ATTRS.items():
        raw_dfs.append(
            aggregate_data_w_ages(v[0], v[1], v[2], diagnosis_code_regex, agg_level)
        )

    for df in raw_dfs:
        consolidate_ya_ages_into_brackets(df)
    
    merged_df = merge_dataframes(raw_dfs)

    bracket_df = dimensionalise_age_brackets(
        merged_df,
        ["Age 0-4", "Age 5-9", "Age 10-14", "Age 15-19", "Age 20-24", "Age 25-29", "Age 30-34", "Age 35-39"]
    )

    return bracket_df


def merge_dataframes(dataframes: list[pd.DataFrame]) -> pd.DataFrame:
    """Merges the provided DataFrames into a single DataFrame via a series of outer
    joins.
    
    Args:
        dataframes: DataFrames to be merged.
    
    Returns:
        Single merged DataFrame.
    """
    merged_df: pd.DataFrame = dataframes.pop(0)
    for df in dataframes:
        merged_df = merged_df.merge(df, how='outer')
    return merged_df


def consolidate_ya_ages_into_brackets(df: pd.DataFrame):
    """Consolidates the youth and adolescent ages in the provided DataFrame into five
    year brackets. The provided DataFrame is modified in-place.
    
    Args:
        df: DataFrame containing youth and adolescent age data to be consolidated.
        
    Returns:
        DataFrame with consolidated youth and adolescent age data.
    """
    insert_idx = df.columns.get_loc("Age 0")
    df.insert(insert_idx, "Age 0-4", df["Age 0"] + df["Age 1-4"])
    df.drop(["Age 0", "Age 1-4"], axis=1, inplace=True)

    insert_idx = df.columns.get_loc("Age 15")
    df.insert(insert_idx, "Age 15-19", (
        df["Age 15"]
        + df["Age 16"]
        + df["Age 17"]
        + df["Age 18"]
        + df["Age 19"]
    ))
    df.drop(
        ["Age 15", "Age 16", "Age 17", "Age 18", "Age 19"],
        axis=1,
        inplace=True
    )

    return df


def dimensionalise_age_brackets(
    df: pd.DataFrame,
    age_bracket_col_names: list[str]
) -> pd.DataFrame:
    """Takes an existing DataFrame and creates a new DataFrame with age bracket
    columns converted to a dimension measurement in a single column named
    "Age Bracket".
    
    Args:
        age_bracket_col_names: list of names of age bracket columns in the provided
            DataFrame.
    
    Returns:
        pandas DataFrame with specified age bracket columns consolidated as dimensions
        in a single column named "Age Bracket".
    """
    bracket_df_dict = {
        "Year": [],
        "Diagnosis Name": [],
        "Age Bracket": [],
        "Admissions": [],
    }
    for idx, row in df.iterrows():
        year = row["Year"]
        diagnosis_name = row["Diagnosis Name"]
        age_bracket_cols = age_bracket_col_names
        for age_col in age_bracket_cols:
            bracket_df_dict["Year"].append(year)
            bracket_df_dict["Diagnosis Name"].append(diagnosis_name)
            bracket_df_dict["Age Bracket"].append(age_col)
            bracket_df_dict["Admissions"].append(row[age_col])
    
    return pd.DataFrame(bracket_df_dict)
