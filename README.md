# Monthly Top 50 Social Media Accounts Dataset

This project aims to scrape data from Wikipedia pages to retrieve the top 50 accounts or channels on various social media platforms such as TikTok, YouTube, Instagram, and Twitter. The scraped data is then processed and saved as CSV files. The dataset is updated monthly, providing the latest rankings and information on the most followed social media accounts.

## Scraping Process

The scraping process is implemented using Python and the following libraries:

- `requests`: Used for sending HTTP requests to the Wikipedia pages.
- `BeautifulSoup`: Used for parsing the HTML content and extracting data from the tables.
- `pandas`: Used for processing and organizing the scraped data.

The script retrieves the data by sending HTTP requests to the Wikipedia pages and parsing the HTML content using BeautifulSoup. The relevant information, such as usernames, followers, descriptions, and other platform-specific details, is extracted from the tables. The scraped data is then processed and saved as CSV files for further analysis and exploration.


## Directory Structure

The repository follows a monthly directory structure to organize the data. Each month, a new directory is created with the format `YYYY-MM` (e.g., `2023-07` for July 2023). Inside each monthly directory, you will find the CSV files containing the data for that specific month.


## Content

The dataset includes the following information for each social media platform:

### Instagram

- **Rank**: The rank of the account within the top 50.
- **Username**: The username or handle of the account.
- **Owner**: The owner or celebrity associated with the account.
- **Followers (millions)**: The number of followers the account has.
- **Profession/Activity**: The profession or activity associated with the account.
- **Country**: The country of origin or association.

### TikTok

- **Rank**: The rank of the account within the top 50.
- **Username**: The username or handle of the account.
- **Owner**: The owner or celebrity associated with the account.
- **Followers (millions)**: The number of followers the account has.
- **Likes (billions)**: The number of likes received by the account.
- **Description**: A brief description of the account.
- **Country**: The country of origin or association.

### YouTube

- **Rank**: The rank of the channel within the top 50.
- **Name**: The name of the channel.
- **Link**: The link to the channel.
- **Subscribers (millions)**: The number of subscribers the channel has.
- **Primary language**: The primary language used in the channel's content.
- **Category**: The category or genre of the channel.
- **Country**: The country of origin or association.

### Twitter

- **Rank**: The rank of the account within the top 50.
- **Username**: The username or handle of the account.
- **Owner**: The owner or celebrity associated with the account.
- **Followers (millions)**: The number of followers the account has.
- **Description**: A brief description of the account.
- **Country**: The country of origin or association.

## Updates

The dataset is updated monthly on the 3rd of each month to provide the latest rankings, follower/subscriber counts, likes, and other relevant information for the top 50 accounts or channels on each platform.

## Usage

This dataset can be used for various purposes, such as:

- Analyzing trends and changes in the popularity and growth of social media accounts or channels over time.
- Comparing the performance and engagement of accounts or channels across different platforms.
- Conducting research on the influence and impact of social media accounts or channels in different countries and industries.

## Acknowledgements

The data in this dataset is obtained from the Wikipedia pages of the respective social media platforms:

- TikTok: [List of most-followed TikTok accounts](https://en.wikipedia.org/wiki/List_of_most-followed_TikTok_accounts)
- YouTube: [List of most-subscribed YouTube channels](https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels)
- Instagram: [List of most-followed Instagram accounts](https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts)
- Twitter: [List of most-followed Twitter accounts](https://en.wikipedia.org/wiki/List_of_most-followed_Twitter_accounts)

## Accessing the Data on Kaggle

You can access the dataset on Kaggle by visiting the following link:
[Monthly Top 50 Social Media Accounts Dataset](https://www.kaggle.com/datasets/amyrmahdy/monthly-top-50-social-media-accounts)

## License

This project is licensed under the [Apache License 2.0](LICENSE).


---

Author: **amyrmahdy**

Date: **3 Jul 2023**


