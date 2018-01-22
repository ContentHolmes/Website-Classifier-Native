# Website-Classification

In the given classifier, Machine-Learning techniques have been used to classify a website into one of the given categories in **Real Time** without even the need to download the webpage. The URL of the website is used to extract its contents. Text processing libraries available in python are used to lemmatize the words. The text classification technique using **Bag-of-Words** model is applied to extract the feature vector from the text in the website. This feature vector is then fed into an **SVM** which accordingly classifies the website into one of the following categories:
- Adult
- Arts
- Business
- Computers
- Games
- Health
- Home
- Kids
- News
- Recreation
- Reference
- Science
- Shopping
- Society
- Sports

## Dataset
The DMOZ dataset has been used for the training purpose. The dataset contains the URLs for each category. A web crawler is used on these URLs to get the keywords and the description of the website.