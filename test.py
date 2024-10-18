from factcheckexplorer.factcheckexplorer import FactCheckLib

# Initialize the library with your query and desired settings
fact_check = FactCheckLib(query="Israel says it has killed Hamas leader Yahya Sinwar in Gaza", language="en", num_results=200)

# Fetch the data
fact_check.process()

# Check the CSV file in your directory for the output