# Welcome to our Missing Persons Project!!
This project was created as part of a Data Wrangling assignment at Dartmouth College.

## Link to our website
[Missing Persons Project Website](https://plambert777.github.io/MissingPersonsProject/index.html)

## Project Overview
### Folder Breakdown
- **main:** All website files.
- **code:** Code used for creating graphs and web scraping.
- **plots:** Plotly interactive maps created in R.
- **img:** Images used for the website.

## Collaborators and Links

- **Parker Lambert:**
  - [Github](https://github.com/plambert777)
  - [LinkedIn](https://www.linkedin.com/in/parkerjosephgreenlambert/)

- **Riya Mehta:**
  - [Github](https://github.com/riyamehta18)
  - [LinkedIn](https://www.linkedin.com/in/riyamehta18/)

- **Sai Priya Lakkireddy:**
  - [Github](https://github.com/saipriya0209)
  - [LinkedIn](https://www.linkedin.com/in/sai-priya-lakkireddy-sp/)
  
## Colaborators and our Links:
<details>
  <summary>Parker Lambert</summary>
  <p><a href="https://github.com/plambert777" target="_blank">Github</a></p>
  <p><a href="https://www.linkedin.com/in/parkerjosephgreenlambert/" target="_blank">LinkedIn</a></p>
</details>
<details>
  <summary>Riya Mehta</summary>
  <p><a href="https://github.com/riyamehta18" target="_blank">Github</a></p>
  <p><a href="https://www.linkedin.com/in/riyamehta18/" target="_blank">LinkedIn</a></p>
</details>
<details>
  <summary>Sai Priya Lakkireddy</summary>
  <p><a href="https://github.com/saipriya0209">Github</a></p>
  <p><a href="https://www.linkedin.com/in/sai-priya-lakkireddy-sp/" target="_blank">LinkedIn</a></p>
</details>

## Documentation

### Data:
1. Missing Persons data from National Missing and Unidentified Persons System (NAMUS): https://namus.nij.ojp.gov/
State-Crime data from the Unified Crime Reporting Statistics and under the collaboration of the U.S. Department of Justice and the Federal Bureau of Investigation: https://corgis-edu.github.io/corgis/csv/state_crime/
2. Substate Region Shapefile from Substrate Abuse and Mental Health Services Administration: https://www.samhsa.gov/data/report/2016-2018-nsduh-substate-region-shapefile
3. GeoJSON boundary files for US counties and states: https://eric.clst.org/tech/usgeojson/

### Data Cleaning and Transformation
We initiated a thorough data cleaning and transformation process for three datasets: missing_data, state_crime, and state_mapping. First, we standardized state names in each dataset for consistency, incorporating both abbreviations and full names. Utilizing the state_mapping dataframe, a left-join aligned state names between missing_data and state_crime. The "DLC" column in missing_data was parsed into month, date, and year. Following state mapping, NAs were removed from relevant columns to ensure data integrity. Substrate shapefile data (.dbf) was converted to .csv using R, maintaining cleanliness with both state abbreviations and full names. Cleaned datasets were exported (missing_data_cleaned.csv, substrate_data_cleaned.csv, and state_crime_cleaned.csv) for subsequent steps. Our decision to exclusively use R for cleaning, leveraging the tidyverse, enabled efficient data manipulation and integration of spatial data processing, a task unfeasible in Excel.

We made a decision to employ all cleaning techniques within R rather than using a combination of Excel and R. This allowed us to leverage the tidyverse, which was helpful data manipulation, and to interact with shapefiles and integrate spatial data processing, which would not have been possible in Excel.

### Mapping and Visualizing Trends
To visualize missing persons data, we created a choropleth map (missing_counts_tab) with counts per state, merging missing_final with state_mapping. We also incorporated mental health metrics from substrate_final, constructing averaged_mental_illness with average values grouped by state. Geographical data for cities was obtained using the Google Maps API, merging with missing_counts_cities for city-level visualization. Further analysis involved calculating missing persons per state and year, joining state_crime_final data, and focusing on 2016-2018 for visualizations. Average proportions of missing persons were computed, integrating mental health metrics and crime rates at the state level.

### Choropleths
Choropleth maps were generated for missing persons distribution, illicit drug use (ILLMON), and Any Mental Illness (AMIYR). Maps highlighted average proportions of missing persons per 100,000 state population, providing spatial insights. Filtering out Alaska ensured visibility into the distribution for other state ratios, and maps were created for both inclusive and exclusive datasets. Additional maps visualized the ratio of average illicit drug use and Any Mental Illness to missing persons.

### State-wise Distribution of Missing Persons:
We created a choropleth visualizing the distribution of missing persons across U.S. states. Each state was color-coded based on the count of missing individuals, providing an intensity gradient corresponding to the count.

### Visualization of Missing Persons by City and State:
We used the Google Maps API to obtain latitude and longitude coordinates for unique city and state combinations in missing_final. We created a summarized dataframe (missing_counts_cities) with counts of missing persons grouped by city, state, and state abbreviation and merged city-level data with overall state-level missing persons count, visualizing the distribution at the city level with an interactive map.

#### Missing Persons per 100,000 State Population
We focused on the years 2016-2018 and created a GeoJSON-based choropleth map using averaged_data to visualize the average proportion of missing persons per 100,000 state population. Alaska was filtered out to visualize the proportions of the remaining states.

#### State-wise Distribution of Average Illicit Drug Use (ILLOM):
Illicit Drug Use Distribution Choropleth:
We generated choropleth maps to visualize state-wise distribution of average illicit drug use (ILLMON) based on averaged_data, both inclusive and exclusive of Alaska.

#### Average Illicit Drug Use by Missing Persons Ratio:
We calculated the product of average illicit drug use and the average proportion of missing persons, creating choropleth maps illustrating the drug-missing persons ratio across U.S. states, both including and excluding Alaska.

#### State-wise Distribution of Average Any Mental Illness (AMIYR) Score:
Similar to illicit drug use, we created a choropleth map visualizing the state-wise distribution of the average Any Mental Illness (AMIYR) score.

#### Average Mental Health Illness by Missing Persons Ratio:
We calculated the product of the average AMIYR score and the average proportion of missing persons, generating choropleth maps visualizing the mental health-missing persons ratio, both including and excluding Alaska.

#### State-wise Distribution of Average Violent Crime (per 100,000 population):
We conducted a left-join between averaged_data and averaged_crimes_state, creating a choropleth map showing the state-wise distribution of average violent crime rates per 100,000 population across the United States. This visualization was presented both with and without Alaska.

### Other Visualizations
#### Distribution of Missing Persons by Gender, State, and Sex:
We created an interactive donut chart showing the distribution of missing persons based on biological sex and a stacked bar chart to show the distribution of missing persons across states and biological sexes.

### Scatter Plots and Line Plot:
We created scatter plots to explore relationships between illicit drug use, mental health metrics, and the proportion of missing persons in the state population. We also created a line plot showing average violent crime rates from 1960 to 2018, with a focus on the years 2016-2018.
Top Missing Persons News with Web Scraping
We also wanted to receive present data on Missing Persons by Current News, hence we developed a Python script dedicated to retrieval and organization of news articles related to missing persons in the last month from the current timestamp. We used the capabilities of the News API (https://newsapi.org/). Firstly, we acquired an API key, which served as the gateway to accessing timely and pertinent information surrounding cases of missing individuals. Our script extracts details such as headlines, description, language, location of the collected articles, presenting the data in a meticulously organized format for subsequent, in-depth analysis.

Upon obtaining a diverse array of articles within the last month, each containing critical keywords such as "Missing Person," "Missing Child," "Unsolved Disappearance," "Amber Alert," "Human Trafficking," "Family Appeals," and "Vanishing Without a Trace," the next very important step involves refining the dataset. We achieved this by employing a text similarity model from HuggingFace. The model evaluates the contextual similarity between the news articles and predefined phrases like "Missing Person" or "A person is missing." 

Before this step, it is also crucial to ensure the cleanliness of the gathered information from the scraped data. This involved the removal of common stop words and extra line breaks. By addressing unnecessary line breaks, the cleaned text became easier for subsequent sentence similarity calculation. Post this step, we then applied a sentence similarity model to get vectorized scores of each description of a news article. The resulting cosine sentence similarity values are then methodically sorted. The ultimate output showcases the top 10 headlines for a specific month. This step was included in an effort to refine the scraped articles further as APIs generally do not check the semantic textual similarity.

This methodology combines the application of web APIs and the efficiency of advanced text similarity analysis, resulting in a selection of top news articles that mention missing persons.

### Website
When determining how to showcase our results, we aimed for something more engaging than a traditional PowerPoint presentation. Ensuring our work remains easily accessible for potential employers on platforms like LinkedIn, we chose to host a website through GitHub. Figma, a collaborative design tool, played a pivotal role in shaping the website's visual identity before the coding process began. This approach facilitated collaborative design and prevented lazy coding, resulting in a more refined web design.

Once the design was finalized, we reached a consensus on the pages to include: a landing page, an inspiration page, a latest headlines page, an about us page, and a results page. In terms of coding, HTML was employed for page elements, CSS added aesthetic appeal, and a bit of JavaScript enhanced mobile accessibility, although there are more optimizations in this area.

