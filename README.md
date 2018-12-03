<h1 align="center">
  <img src="media/review-icon.png" width="20%"><br/>SentiFilm
</h1>

<h4 align="center">
  🎬 Movie Review Sentiment Analytics Django App
</h4>

<div align="center">
    <img src="media/output.gif" width="800" alighn="center">
</div>

## Contents

* [Overview](#overview)
* [Dataset](#dataset)
* [Dependencies](#dependencies)
* [Improvements](#improvements)
* [References](#references)
* [Attribution](#attribution)
* [Contributing](#contributing)
* [License](#license)

## Overview

SentiFilm is a simple web app that gives you the sentiment of a movie review with a polarity score. I will be adding more features to this application in order to improve performace and give more information regarding the text input. For now, Sentifilm uses a lexical model to compute sentiment of a given text.

## Dataset

The dataset that was used was the [IMDB Movie Review dataset](http://ai.stanford.edu/~amaas/data/sentiment/).

## Dependencies

*Note these dependencies are being used for other sentiment analysis methods that are currently not included in the application however will later be added.*

* Spacy
* Django
* NumPy
* NLTK
* Pandas
* Requests
* Gensim
* SciPy
* Matplotlib
* Keras
* Afinn
* Scikit Learn
* Beautiful Soup 4
* Skater

## Improvements

These are some additional features I want to add in order to have this web app give more information regarding the text input.

- [_] Implement supervised methods trained on dataset for better performance
- [_] Implement topic modeling and visualization for text input
- [_] Improve UI

## References

* [Lexicon-Based Methods for Sentiment Analysis](https://www.mitpressjournals.org/doi/pdf/10.1162/COLI_a_00049)

## Attribution

* Icon by [Wichai Wi](https://thenounproject.com/vividzfoto/) from [thenounproject](https://thenounproject.com/)

## Contributing

Contributions are always welcome! For bug reports or requests please submit an issue.

## License

[MIT](https://github.com/moebg/sentifilm/blob/master/LICENSE)