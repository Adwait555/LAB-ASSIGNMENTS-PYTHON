import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- DATA GENERATION (To make the script runnable immediately) ---
def get_data():
    # Cosmetic Sales Data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales_data = {
        'month': months,
        'face_cream': [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
        'face_wash': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
        'toothpaste': [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
        'total_profit': [211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200]
    }
    
    # Recruitment Data
    recruitment_data = {
        'Company': ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS', 'Amdocs'],
        'Recruits': [450, 500, 600, 350, 400, 550, 300, 250]
    }
    return pd.DataFrame(sales_data), pd.DataFrame(recruitment_data)

# --- LAB ASSIGNMENT 1: COSMETIC COMPANY VISUALIZATION ---
def assignment_1(df_sales):
    print("\nGenerating Visualizations for Assignment 1...")
    
    # a) Line Plot of Total Profit
    plt.figure(figsize=(8, 5))
    plt.plot(df_sales['month'], df_sales['total_profit'], label='Total Profit', marker='o', color='red')
    plt.title('Monthly Total Profit')
    plt.xlabel('Month')
    plt.ylabel('Profit')
    plt.legend()
    plt.show()

    # b) Multiline Plot for all products
    plt.figure(figsize=(8, 5))
    plt.plot(df_sales['month'], df_sales['face_cream'], label='Face Cream', marker='o')
    plt.plot(df_sales['month'], df_sales['face_wash'], label='Face Wash', marker='o')
    plt.plot(df_sales['month'], df_sales['toothpaste'], label='Toothpaste', marker='o')
    plt.title('All Product Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales Units')
    plt.legend()
    plt.show()

    # c) Bar Chart for Face Cream & Face Wash
    plt.figure(figsize=(8, 5))
    x = np.arange(len(df_sales['month']))
    plt.bar(x - 0.2, df_sales['face_cream'], 0.4, label='Face Cream')
    plt.bar(x + 0.2, df_sales['face_wash'], 0.4, label='Face Wash')
    plt.xticks(x, df_sales['month'])
    plt.title('Face Cream vs Face Wash Sales')
    plt.legend()
    plt.show()

    # d) Pie Chart for Total Sales
    plt.figure(figsize=(7, 7))
    labels = ['Face Cream', 'Face Wash', 'Toothpaste']
    totals = [df_sales['face_cream'].sum(), df_sales['face_wash'].sum(), df_sales['toothpaste'].sum()]
    plt.pie(totals, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Total Sales Distribution by Product')
    plt.show()




# --- LAB ASSIGNMENT 2: RECRUITMENT VISUALIZATION ---
def assignment_2(df_rec):
    print("\nGenerating Visualizations for Assignment 2...")

    # a) Bar Chart
    plt.figure(figsize=(10, 5))
    plt.bar(df_rec['Company'], df_rec['Recruits'], color='skyblue')
    plt.title('New Recruitments by Company')
    plt.show()

    # b & c) Customized Pie Chart
    plt.figure(figsize=(7, 7))
    # Explode the largest slice (Amazon in this dummy data)
    explode = [0.1 if x == max(df_rec['Recruits']) else 0 for x in df_rec['Recruits']]
    plt.pie(df_rec['Recruits'], labels=df_rec['Company'], autopct='%1.1f%%', explode=explode, shadow=True)
    plt.title('Recruitment Share (Customized Pie)')
    plt.show()

    # d) Doughnut Chart
    plt.figure(figsize=(7, 7))
    plt.pie(df_rec['Recruits'], labels=df_rec['Company'], autopct='%1.1f%%', pctdistance=0.85)
    # Draw a white circle in the center to make it a doughnut
    centre_circle = plt.Circle((0,0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title('Recruitment Doughnut Chart')
    plt.show()

    # Comparison: IBM vs Amdocs
    plt.figure(figsize=(6, 4))
    comparison = df_rec[df_rec['Company'].isin(['IBM', 'Amdocs'])]
    plt.bar(comparison['Company'], comparison['Recruits'], color=['blue', 'green'])
    plt.title('Comparison: IBM vs Amdocs Recruitments')
    plt.show()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    df_sales, df_rec = get_data()
    
    # Run Assignments
    assignment_1(df_sales)
    assignment_2(df_rec)
