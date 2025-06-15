import requests
import os
import streamlit as st
# Fetches weather details by passing a url
def fetchweather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Error fetching weather data"
    except Exception as e:
        return f"Exception occured: {e}"
# Saves search hist data from loadhist and saves it into a file
def savetohist(city):
    history = loadhist()
    if city not in history:
        history.insert(0,city)
    else:
        history.remove(city)
        history.insert(0,city) 
    history = history[:5]
    with open('search_hist.txt', 'w') as f:
        f.write("\n".join(history))
# Reads the file and removes existing white spaces and unwanted lines 
def loadhist():
    if not os.path.exists('search_hist.txt'):
        print("File did not exist, Created now!")
        return []
    with open('search_hist.txt', "r") as f:
        return[line.strip() for line in f.readlines() if line.strip()]
# Displays the search history data
# def showhist():
#     history = loadhist() 
#     if not history:
#         print("No history found")
#         return
#     print("\nSearch history: ")
#     for i,city in enumerate(history,1):
#         print(f"{i}.{city}")
#     try:
#         choice = int(input("Enter the city number you want to search again."))
#         if 1 <=choice <= len(history):
#             selected_city = history[choice-1]
#             print(fetchweather(selected_city))
#             savetohist(selected_city)
#     except ValueError:
#         print("Invalid input")


# --Using streamlit UI--
st.set_page_config(page_title = "Weather App", page_icon="⛅")
st.title("🌦️ Real-Time Weather App")
# Search selection
city = st.text_input("Enter city name","")

if st.button("Get weather"):
    if city.strip():
        weather = fetchweather(city)
        st.success(weather)
        savetohist(city)
    else:
        st.warning("Please enter a city name.")

# History selection
st.subheader("📜 Search History")
history = loadhist()
if history:
    selected_city = st.selectbox("View past search",["--select"] + history)
    if selected_city != "--select":
        weather = fetchweather(selected_city)
        st.info(weather)
        savetohist(selected_city)
else:
    st.text("No previous search history.")
    






# def main():
#     while True:
#         print("\n🌦️  Real-Time Weather CLI")
#         print("1. Search weather by city")
#         print("2. View search history")
#         print("3. Exit")
#         choice = int(input("Enter your choice: ").strip())

#         if choice == 1:
#             city = input("Enter the city name: ")
#             if city:
#                 print(fetchweather(city))
#                 savetohist(city)
#         elif choice == 2:
#             showhist()
#         elif choice == 3:
#             print("tata")
#             break
#         else: 
#             print("Invalid Input")

# if __name__ == "__main__":
#     main()
        
        