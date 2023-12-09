<div align="center">
    <h1>Salary Application</h1>
</div>

## A machine learning application to predict the annual salary of full-time software engineers.

### Introduction
#### Stack Overflow Annual Developer Survey
In May 2023 over 90,000 developers responded to Stack Overflow annual survey about how they learn and level up, which tools they're using, and which ones they want.
[Survey](https://insights.stackoverflow.com/survey)


### Repository Structure
* **README.md**: The top-level README for reviewers of this project
* **requirements.txt**: requirements file; including the needed tools
* **notebooks**: Jupyter notebooks: `01.data_exploration.ipynb` exploring the features that I selected to train my model. `02.processing_model.ipynb` processing the selected features and training the model.
* **data folder**: has a file how to download the dataset to run the notebooks.
* **predict_page.py**: Model interface.
* **explore_page.py**: Exploration inferface.
* **app.py**: Project application.

### Libraries
* pandas
* NumPy
* scikit-learn
* streamlit
* xgboost

