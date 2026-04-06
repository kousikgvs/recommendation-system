# Movie Recommendation System

A content-based movie recommendation system built using TF-IDF vectorization and cosine similarity.

## Project Overview

This project implements a movie recommendation system that suggests similar movies based on content features. The system uses the TMDB 5000 Movies dataset and employs text vectorization techniques to find similar movies.

## Features

- **Content-Based Filtering**: Recommends movies based on similar content features
- **TF-IDF Vectorization**: Converts movie titles and tags into numerical vectors
- **Cosine Similarity**: Measures similarity between movies
- **Tag-Based Recommendations**: Uses movie tags for finding similar content

## Project Structure

```
recommendation-system/
├── dataset/
│   ├── tmdb_5000_credits.csv
│   └── tmdb_5000_movies.csv
├── dataset_cleaned/
│   ├── output.csv
│   └── df_reader.py
├── src/
│   ├── main.py
│   └── pipelines/
│       └── recommend.py
├── notebooks/
│   └── code.ipynb
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kousikgvs/recommendation-system.git
cd recommendation-system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the main application:
```bash
python src/main.py
```

2. The recommendation pipeline is located in `src/pipelines/recommend.py`

## Dependencies

- numpy
- pandas
- scikit-learn
- difflib

## Data

The system uses the TMDB 5000 Movies dataset, which includes:
- Movie titles
- Movie tags
- Credits information
- Various metadata

## Recommendation Algorithm

The system uses a content-based filtering approach:

1. **Text Vectorization**: Converts movie titles and tags into TF-IDF vectors
2. **Feature Extraction**: Uses CountVectorizer for tag-based features
3. **Similarity Calculation**: Computes cosine similarity between movie vectors
4. **Recommendation**: Returns movies with highest similarity scores

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.