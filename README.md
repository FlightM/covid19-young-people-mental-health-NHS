# Analyzing the Impact of COVID-19 on Young People's Mental Health: NHS Data Trends

- [What this repository is](#what-this-repository-is)
- [Running the code](#running-the-code)
- [Code structure](#code-structure)

## What this repository is
This repository includes code used to process data from the 2017-18 to 2023-24 releases of United Kingdom (UK) National Health Service (NHS) datasets from the Office of National Statistics (ONS) hospital admissions data. The datasets are also related to the following work: A. Y. Naser, ‘Hospitalisation profile in England and Wales, 1999 to 2019: an ecological study’, BMJ Open, vol. 13, no. 4, p. e068393, Apr. 2023, doi: 10.1136/bmjopen-2022-068393.

The data was processed for visualisation to explore the questions "How did the number of diagnoses of COVID-19-related mental health disorders identified in previous literature change during and after COVID-19?” and "How did COVID-19’s impact on young people’s mental health compare to its impact on adults’ mental health?"

Visualisations created using the processed data can be [viewed on Tableau public](https://public.tableau.com/views/COVID-19andYoungPeoplesMentalHealthNHSDataTrends/DiagnosesQuantityandRankings?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).

Previous literature reviewed on the subject includes:
- I. H. Bell et al., ‘The impact of COVID-19 on youth mental health: A mixed methods survey’, Psychiatry Research, vol. 321, p. 115082, Mar. 2023, doi: 10.1016/j.psychres.2023.115082.
- J. Montero-Marin et al., ‘Young People’s Mental Health Changes, Risk, and Resilience During the COVID-19 Pandemic’, JAMA Netw Open, vol. 6, no. 9, p. e2335016, Sep. 2023, doi: 10.1001/jamanetworkopen.2023.35016.
- O. Y. Rouquette, D. Dekel, A.-M. Siddiqi, C. Seymour, L. Weeks, and A. John, ‘Mental health and its wider determinants in young people in the UK during 12 months of the COVID-19 pandemic: repeated cross-sectional representative survey’, BJPsych Open, vol. 10, no. 6, p. e214, Dec. 2024, doi: 10.1192/bjo.2024.726.

## Running the code
Executing export.py will create an Excel workbook (.xlsx) containing the data used for visualisation creation. Note you will likely need to change the local location to which the export should be saved. Local URIs in constants.py may also need to be updated.

## Code structure
The code is composed of three modules:
- constants.py - Constants and static local URIs.
- data.py - Data processing and manipulation functions.
- export.py - Exports processed data to an Excel workbook (.xlsx).
