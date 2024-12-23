# Yu-Gi-oh--Card-Game

## Overview
This project provides a Python application that allows users to analyze and manage data related to Yu-Gi-Oh! trading cards. 
The application can read card data from CSV files, perform searches, display stats, and manage user decklists.
## Features
- **Data Loading**: Users can load card data from any properly formatted CSV file. The tool ensures robust handling of data parsing errors and provides clear prompts to re-enter file paths if files are not found.
- **Comprehensive Search Functionality**: Offers the ability to search for cards by multiple attributes:
  - **Card ID**: Locate a card using its unique identifier.
  - **Name**: Search for cards by full or partial names.
  - **Type and Race**: Filter cards based on their type (e.g., monster, spell, trap) and race.
  - **Description**: Find cards containing specific terms or phrases within their descriptions.
  - **Archetype**: Search for cards belonging to specific archetypes, crucial for players focusing on thematic decks.
  - **Card Price**: Allows searching and sorting cards based on their market price, useful for budgeting and investment considerations.
- **Statistical Analysis**: Automatically calculates key statistics for any set of cards:
  - **Price Analysis**: Determine the minimum, maximum, and median prices within any subset of cards to help with financial planning and trading decisions.
  - **Distribution Stats**: Get a detailed view of card distribution by type, race, and archetype, which is essential for deck building and strategy development.
- **Decklist Management**: Users can load their decklists for detailed analysis, viewing comprehensive stats and individual card details, enabling better strategic adjustments and deck optimization.
- **Interactive Menu**: The tool uses a clear, straightforward menu-driven interface that lets users navigate through options without prior experience, making it accessible even for beginners.

- ### Enhanced Display Options
- **Formatted Output**: All card data is displayed in a well-structured format, making it easy to read and understand. Users can see card details aligned in columns with headers such as Name, Type, Race, Archetype, and Price.
- **Limited Display**: For large datasets, the tool initially presents a manageable subset of data, specifically the first 50 cards sorted by the selected criteria, preventing information overload.
- **Statistical Summaries**: When viewing search results or the entire dataset, the tool provides a summary of relevant statistics, enhancing the analytical value of the displayed information.

### Designed for Extensibility
- **Modular Code**: The application is designed with modularity in mind, allowing easy updates and additions of new features, such as additional search criteria or improved statistical computations.
- **Community Contributions**: The open design invites community involvement for further development, including feature enhancements, bug fixes, and updates based on the evolving needs of Yu-Gi-Oh! TCG players.

## Prerequisites
- Python 3.x
- CSV files with card data formatted with the following headers:
  - ID, Name, Type, Description, Race, Archetype, Card Price
