"""
Recommendation System Package
Provides content-based movie recommendation functionality
"""

from .data.loader import DataLoader
from .features.preprocess import Preprocessor
from .pipelines.recommend import Recommender

__all__ = [
    'DataLoader',
    'Preprocessor',
    'Recommender'
]