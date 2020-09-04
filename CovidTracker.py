from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Country Wise Data For COVID-19")


def showdata():  #A function which will show the data for the virus threats
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches
    from covid import Covid
    covid = Covid()  #Declare empty Lists to store different data sets
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []

    try:
        root.update()
        #getting name of the countries entered by the user
        countries = data.get()
        #removing white spaces from the start and end of the string
        country_names = countries.strip()
        #Replace white spaces with commas
        country_names = country_names.replace(" ",",")
        #splitting the string to store names of countries as a list
        country_names = country_names.split(",")

        #for loop to get all the data of thr countries

        for x in country_names:
            #Appending countries data 1 by 1 in list of cases
            #the data will be stored in form of dictionary
            #for each country,there will be 1 dictionary in the list, which will contain
        #whole info. of that respected country
            cases.append(covid.get_status_by_country_names(x))
            root.update()

        for y in cases:# a loop to get data stored as dictionary in list for one country
            confirmed.append(y["confirmed"])
            #similarly
            active.append(y["active"])
            deaths.append(y["deaths"])
            recovered.append(y["recovered"])

            #making color info on scale using patches
        confirmed_patch = mpatches.Patch(color='green',label='confirmed')
        recovered_patch = mpatches.Patch(color='red',label='recovered')
        active_patch = mpatches.Patch(color='blue',label='active')
        deaths_patch = mpatches.Patch(color='black',label='deaths')

        #plotting the scale on graph using legend()
        plt.legend(handles=[confirmed_patch , recovered_patch , active_patch , deaths_patch ])
        #show data using graph

        #loop for matplotlib
        for x in range(len(country_names)):
            plt.bar(country_names[x],confirmed[x],color='green')
            if recovered[x] > active[x]:
                plt.bar(country_names[x], recovered[x], color='red')
                plt.bar(country_names[x], active[x], color='blue')
            else:
                plt.bar(country_names[x], active[x], color='blue')
                plt.bar(country_names[x],  recovered[x], color='red')
            plt.bar(country_names[x], deaths[x], color='black')
        #title of graph
        plt.title("Current COVID cases")
        #label for x direction
        plt.xlabel("Country Name")
        #for y direction
        plt.ylabel("Cases (In millions)")
        plt.show()
    except Exception as e:
        data.set("Enter correct details again.")

Label(root, text="Enter all countries names\nfor whow you want to get\nCovid-19 Data?",font="Consolas 15 bold").pack()
Label(root, text="Enter country name:").pack()
data = StringVar()

data.set("Separate country using ',' or 'space' (not both)")
entry = Entry(root, textvariable=data,width=50).pack()


Button(root, text="Get Data",command=showdata).pack()
root.mainloop()
