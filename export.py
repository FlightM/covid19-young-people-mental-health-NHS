"""This module contains code for exporting the data needed to create the three
visualisations.
"""
# Standard library imports
from datetime import datetime
import os

# Local application imports
from data import compile_annual_data_w_ages


def compile_data():
    """Compiles data necessary to create all three visualisations into a single
    pandas DataFrame.
    
    Acquires three sets of data and combines them together. The three datasets acquired
    are:
        - Aggregated diagnosis data related to reviewed literature pertaining to mental
        health impacts of COVID-19 on youth and adolescents by age bracket.
        - All diagnosis aggregated by age bracket.
        - Aggregated diagnosis data pertaining to behavioural and emotional disorders
          usually occurring during childhood and adolescence.
        
    Args:
        None
    
    Returns:
        Single DataFrame containing the data described above.
    """
    # Get data
    lr_data = compile_annual_data_w_ages("^F3|^F4|^F5", 1)
    all_data = compile_annual_data_w_ages("", 0)
    ya_dev_data = compile_annual_data_w_ages("^F9[1-8]", 1)

    # Format data and set indices
    lr_data = lr_data.drop("Diagnosis Name", axis=1)\
        .rename({"Admissions": "# of Literature-Related Diagnoses"}, axis=1)\
        .set_index(["Year", "Age Bracket"])
    
    all_data = all_data.drop("Diagnosis Name", axis=1)\
        .rename({"Admissions": "Total Diagnoses"}, axis=1)\
        .set_index(["Year", "Age Bracket"])

    ya_dev_data = ya_dev_data.drop("Diagnosis Name", axis=1)\
        .rename({"Admissions": "# of Y-A Onset Disorder Diagnoses"}, axis=1)\
        .set_index(["Year", "Age Bracket"])\
    
    # Join dataframes and add calculated attributes
    data = all_data.join(lr_data, on=["Year", "Age Bracket"])\
        .join(ya_dev_data, on=["Year", "Age Bracket"])
    data["LR Percent of Total Diagnoses"] = (
        data["# of Literature-Related Diagnoses"] / data["Total Diagnoses"] * 100
    )
    
    return data


def export_data():
    """Exports DataFrame of compiled data to an Excel spreadsheet.

    The spreadsheet is saved in the "exported_data/" directory.
    
    Args:
        None
    
    Returns:
        None
    """
    data = compile_data()
    wb_uri = os.path.normpath(os.path.join(
        os.path.dirname(__file__),
        f"../exported_data/compileddata_{datetime.now().strftime('%m-%d_%H-%M-%s')}.xlsx"
    ))
    data.to_excel(wb_uri, merge_cells=False)


if __name__ == "__main__":
    export_data()
