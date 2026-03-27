import pandas as pd
import os

# --- PRE-REQUISITE: CREATE SAMPLE DATA IF NOT EXISTS ---
def create_sample_csv():
    if not os.path.exists("books.csv"):
        data = {
            'title': ['The Alchemist', 'Python Basics', 'Data Science', 'Deep Learning', 'Java Core'],
            'author': ['Paulo Coelho', 'John Smith', 'Jane Doe', 'John Smith', 'Jane Doe'],
            'edition': ['1st', '4th', '2nd', '3rd', '1st'],
            'publication_year': [1988, 2021, 2019, 2023, 2015],
            'publishing_house': ['HarperCollins', 'TechPress', 'Academic', 'TechPress', 'Oxford'],
            'price': [450, 1200, 850, 2100, 550]
        }
        pd.DataFrame(data).to_csv("books.csv", index=False)
        print("Created sample 'books.csv' for testing.")

# --- LAB ASSIGNMENT 1: PANDAS DATAFRAME (BOOKS) ---
def assignment_1():
    print("\n" + "="*40)
    print("LAB ASSIGNMENT 1: BOOK DATA ANALYSIS")
    print("="*40)
    
    try:
        df = pd.read_csv("books.csv")
        
        # a) Print complete report
        print("\na) Complete Report of Books:")
        print(df.to_string(index=False))

        # b) Books of a given author
        author_name = input("\nb) Enter Author name to search: ")
        author_books = df[df['author'].str.contains(author_name, case=False)]
        print(author_books if not author_books.empty else "No books found for this author.")

        # c) Books of a given publishing house
        pub_house = input("\nc) Enter Publishing House to search: ")
        pub_books = df[df['publishing_house'].str.contains(pub_house, case=False)]
        print(pub_books if not pub_books.empty else "No books found for this publisher.")

        # d) Cheapest & Costliest books
        print("\nd) Cheapest and Costliest Books:")
        cheapest = df.loc[df['price'].idxmin()]
        costliest = df.loc[df['price'].idxmax()]
        print(f"Cheapest: {cheapest['title']} (Price: {cheapest['price']})")
        print(f"Costliest: {costliest['title']} (Price: {costliest['price']})")

        # e) Sorting based on year of publication
        print("\ne) Books sorted by Publication Year:")
        sorted_df = df.sort_values(by='publication_year')
        print(sorted_df.to_string(index=False))

    except FileNotFoundError:
        print("Error: 'books.csv' not found. Please run the script again.")





# --- LAB ASSIGNMENT 2: STATE DATA ANALYSIS ---
def assignment_2():
    print("\n" + "="*40)
    print("LAB ASSIGNMENT 2: STATE DATA ANALYSIS")
    print("="*40)
    
    # Create Table (DataFrame) for 5 states
    state_data = {
        'State_Name': ['Maharashtra', 'Rajasthan', 'Goa', 'Uttar Pradesh', 'Sikkim'],
        'Area': [307713, 342239, 3702, 240928, 7096], # Area in sq km
        'Population': [112374333, 68548437, 1458545, 199812341, 610577]
    }
    df_states = pd.DataFrame(state_data)

    # a) Complete information
    print("\na) Complete Information of States:")
    print(df_states.to_string(index=False))

    # b) State with largest Area
    largest_area_state = df_states.loc[df_states['Area'].idxmax(), 'State_Name']
    print(f"\nb) State having largest Area: {largest_area_state}")

    # c) State with largest Population
    largest_pop_state = df_states.loc[df_states['Population'].idxmax(), 'State_Name']
    print(f"c) State having largest Population: {largest_pop_state}")

    # d) Calculate Population Density (Population / Area)
    df_states['Density'] = df_states['Population'] / df_states['Area']
    print("\nd) Population Density calculated (Population per sq km):")
    print(df_states[['State_Name', 'Density']].to_string(index=False))

    # e) State with highest population density
    highest_density_state = df_states.loc[df_states['Density'].idxmax(), 'State_Name']
    print(f"\ne) State with highest Population Density: {highest_density_state}")

# --- MAIN MENU ---
if __name__ == "__main__":
    create_sample_csv()
    while True:
        print("\n--- PRACTICAL NO: 10 MENU ---")
        print("1. Run Assignment 1 (Books CSV)")
        print("2. Run Assignment 2 (State Reports)")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == '1':
            assignment_1()
        elif choice == '2':
            assignment_2()
        elif choice == '3':
            break
        else:
            print("Invalid Choice.")
