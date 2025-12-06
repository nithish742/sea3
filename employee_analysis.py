import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
departments = ["R&D","Sales","Marketing","HR","Finance"]
data = {
    "Employee ID": range(1, 101),
    "Department": [departments[i % 5] for i in range(100)],
    "Region": ["North","South","East","West","North"]*20
}

df = pd.DataFrame(data)

# Calculate R&D frequency
rd_count = df[df["Department"] == "R&D"].shape[0]
print(f"Frequency count for R&D department: {rd_count}")  # should print 16

# Create Seaborn chart
sns.set_style("whitegrid")
plt.figure(figsize=(8,8))  # 512x512 pixels approx
sns.countplot(x="Department", data=df, palette="Set2")
plt.title("Employee Distribution Across Departments")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.savefig("chart.png", dpi=64, bbox_inches='tight')  # saved chart
plt.close()

# Create HTML with embedded frequency
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Employee Department Distribution</title>
</head>
<body>
    <h1>Employee Distribution Across Departments</h1>
    <p>Email: 25f1001910@ds.study.iitm.ac.in</p>
    <p>Frequency count for "R&D" department: {rd_count}</p>
    <img src="chart.png" alt="Department Distribution">
</body>
</html>
"""

with open("employee_distribution.html", "w") as f:
    f.write(html_content)
