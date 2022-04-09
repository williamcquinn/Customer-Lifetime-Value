# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.8.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Home Alarm CLV
#
# Prepare "Home Alarm, Inc.: Assessing Customer Lifetime Value" for class discussion and as an individual assignment and submit the assignment through GitLab. Be VERY clear about where results are coming from and what assumptions you are making in your Python code. It is in your best interest that we do not have to struggle to figure out where your numbers came from. The assignment (pdf) is on Canvas (week2/homealarm-clv.pdf). Example Excel calculations are also on Canvas (week1/aws-clv.xlsx and week1/notflix-cls.xlsx).
#
# ## Setup
#
# Create a Jupyter notebook in which you calculate the CLV for a customer that uses auto-pay and for a customer that does not use auto-pay and answer question 1 through 4 in the assignment PDF.
#
# ## Hints
#
# Add text motivating your work in Markdown format. Markdown is a simple formatting syntax for authoring HTML. For more details on using markdown go to http://commonmark.org/help/ for a 10-minute interactive Markdown tutorial
#
# Please generate an HTML (Notebook) with your answers to all the questions listed in the homealarm-clv.pdf file on Canvas. When you have finished editing the jupyter notebook and havengenerated the HTML report make sure to save, commit, and push to GitLab. We will collect all files from GitLab after the due date.
#
# Use File > Export Notebook As... > Export Notebook to HTML to get the html report and include to the jupyter notebook file and the HTML file in your submission.
#
# ## Analysis
#
# The python dictionary below contains information about attrition notifications from the table on page 3 of the assignment PDF.
#
# Note: GitLab will automatically tests if your work is fully reproducible each time you "push" changes (see .gitlab-ci.yml for the configuration). If you get an email from GitLab stating that there was an error, it suggests a problem in your code. Note that the setup for the Home Alarm assignment will *not* test if your analysis is correct. GitLab will only check if the code is valid and runs without issue in the docker container.

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# %%
churn = pd.DataFrame(
    {
        "autopay": [0.032, 0.070, 0.097, 0.103, 0.095, 0.078, 0.069, 0.059, 0.053],
        "no_autopay": [0.084, 0.122, 0.162, 0.154, 0.134, 0.120, 0.111, 0.096, 0.086],
    }
)

# %% [markdown]
# ### Calculate CLV for autopay customers

# %%
# list your assumptions here

# %%
# calculate clv here

# %% [markdown]
# ### Calculate CLV for non-autopay customers

# %%
# list your assumptions here

# %%
# calculate clv here

# %% [markdown]
# ### Create a line graph of CLV for both autopay and non-autopay customer 

# %%
# enter your code here

# %% [markdown]
# ### Create a line graph of the retention rate for both autopay and non-autopay customer 

# %%
# enter your code here

# %% [markdown]
# ### Calculate the maximum amount to spend on autopay incentives

# %%
max_pay = # insert your code here
print(f"Maxium amount to spend on autopay incentives is {max_pay.round(2)}")

# %% [markdown]
# ### Suggested marketing actions
#
# Suggest three marketing actions Home Alarm should consider to convert existing customers to autopay who are about to start their second year with Home Alarm. Be specific about incentive amounts you recommend using (if any)

# %% [markdown]
# ... enter suggested marketing actions here ...
