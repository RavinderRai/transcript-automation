# Automated Customized Meeting Summarizer

## Overview

This project automates the process of generating customized meeting summaries from text data. It goes beyond standard transcription services by cleaning, filtering, categorizing, and summarizing meeting content, with a focus on extracting actionable items.

## Features

- Text data ingestion from YouTube transcripts
- Text cleaning and preprocessing
- Filtering of non-relevant information
- Content categorization
- Generation of customized summaries with action items
- Automated workflow using Apache Airflow for seemless deployment

## Technologies Used

- Python
- OpenAI GPT-3 API
- Apache Airflow
- Few-shot learning techniques

## Usage

1. This is just of proof of concept where we pulled meeting data from YouTube
2. Thus, the data ingestion process would need to be adjusted for your use case
3. Otherise, once you have your data ingestion process, make sure it is in a json format
4. Then replace the `captions_without_cats.json` file with a json file containing your meeting text data
5. Also rename `captions_without_cats.json` filename in the src/clean_transcript.py file accordingly
6. Finally, set up Airflow and run the DAG to process the data
7. Retrieve generated summaries and action items from the output markdown file
