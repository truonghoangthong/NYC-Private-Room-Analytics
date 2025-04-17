# NYC Private Room Cleaning + Analytics

## Project Overview
As a "consultant" for a real estate start-up, I put together this project to dig into the short-term rental market in New York City using Airbnb listing data. My goal was to provide actionable insights about private room listings to help the company make smart decisions. I had a blast working with real-world data and uncovering trends that could shape their strategy!

This project answers key questions:
- When were the earliest and most recent reviews posted for these listings?
- How many listings are private rooms?
- What’s the average price for these listings?
- How can we summarize these findings in a clean, single-row DataFrame?

## Dataset
The raw data lives in the `data/` folder and includes three files:
- `airbnb_price.csv`: Pricing info for the listings.
- `airbnb_room_type.xlsx`: Details on room types (e.g., private rooms, entire homes).
- `airbnb_last_review.tsv`: Review dates for each listing.

## Analysis
I used Python to tackle the analysis, breaking it down into these steps:
1. **Earliest and Most Recent Review Dates**:
   - Pulled from `airbnb_last_review.tsv` and stored as `first_reviewed` and `last_reviewed`.
   - Had to clean up some messy date formats!
2. **Count of Private Room Listings**:
   - Filtered `airbnb_room_type.xlsx` to count private room listings.
   - Saved the result in `nb_private_rooms`.
3. **Average Listing Price**:
   - Calculated from `airbnb_price.csv` and rounded to two decimal places for clarity.
   - Stored in `avg_price`.
4. **Summary DataFrame**:
   - Combined everything into a DataFrame called `review_dates` with four columns: `first_reviewed`, `last_reviewed`, `nb_private_rooms`, and `avg_price`.
   - Kept it to one row for a concise summary.

## Repository Structure
- `data/`: Holds the raw data files (`airbnb_price.csv`, `airbnb_room_type.xlsx`, `airbnb_last_review.tsv`).
- `main.py`: My Python script for the full analysis
- `final_result.csv`: File of Summary Results

## Results
The script outputs:
- The earliest and most recent review dates.
- The total number of private room listings.
- The average listing price (rounded to two decimals).
- A neat DataFrame (`review_dates`) summarizing everything in one row.

