import pandas as pd
from nltk.corpus import stopwords
from nltk import word_tokenize
import re
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import uuid
from nltk.stem import 	WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()


# --------------------------------------- Data Preparation ---------------------------------------#
dff = pd.read_csv("job_data_description_2.csv")[["Job.ID","Title", "Position", "Company", "City"]]
job_ids = []
for job in dff["Job.ID"]:
     unique_id = str(uuid.uuid4())
     job_ids.append(unique_id)
dff["jobId"] = pd.Series(job_ids)
dff[["jobId", "Title", "Position", "Company", "City"]].to_csv("job_data_filtered.csv", index = False)

class JobRecommender:

     def __init__(self, jobs_data_path, new_text, K):
        self.jobs_data_path=jobs_data_path
        self.new_text = new_text
        self.K = K
        self.dataPreprocessing()
        self.get_text_length()
        self.count_vectorization()
        self.getSimilarities()
        self.getTopKJobs()

     '''Getting the Data'''
     def dataPreprocessing(self):
        df_jobs = pd.read_csv(jobs_data_path).sample(10000).reset_index(drop=True)
        df_jobs['combined_features'] = pd.Series(df_jobs['Title'].map(str) + ' ' + df_jobs['Position'].map(str) + ' ' + df_jobs['Company'].map(str) + df_jobs['City'].map(str))
        print(df_jobs["combined_features"])
        # clean the text
        df_jobs['text'] = df_jobs['combined_features'].apply(self.clean_text)
        self.df_jobs = pd.DataFrame(df_jobs[['jobId', 'text']])
        print(df_jobs["text"])
        # clean the input text
        self.new_text = pd.Series(self.clean_text(self.new_text))

     '''Getting text length, and cleaning rows with too much and too little text'''
     def get_text_length(self):
         self.df_jobs["text_length"] = self.df_jobs["text"].apply(len)
         self.df_jobs= self.df_jobs[(self.df_jobs["text_length"] < 300) & (self.df_jobs["text_length"] > 10)]

     '''Cleaning the data'''
     def clean_text(self, text):
        text = text.lower()
        text = re.sub("\d+", " ", text)
        text = re.sub("\W+", " ", text)
        text = set(word_tokenize(text))
        stopWords = stopwords.words("English")
        text = [word for word in text if word not in stopWords]
        text = [word for word in text if word not in string.punctuation]
        text = [wordnet_lemmatizer.lemmatize(word) for word in text]
        return ' '.join(text)

     '''Counting Words & Vetorization'''
     def count_vectorization(self):
           cv = CountVectorizer()
           cv_fit = cv.fit_transform(self.df_jobs['text'])
           self.countMatrix_jobs = cv_fit.toarray()
           self.new_text_count = cv.transform(self.new_text).toarray()
           print("New Text Vectorization:\n", self.new_text_count)
           self.df_jobs_CV = pd.DataFrame(self.countMatrix_jobs, columns=cv.get_feature_names_out(), index=self.df_jobs['jobId'])

     '''Cosine Similarity'''
     def getSimilarities(self):
         self.similarityWords = cosine_similarity(self.countMatrix_jobs, self.new_text_count)
         self.df_jobs["score"] = pd.DataFrame(self.similarityWords)
         print(self.df_jobs["score"])

     '''Get most similar K jobs'''
     def getTopKJobs(self):
         # sort the df based on score
         self.df_jobs = self.df_jobs.sort_values(by = 'score', ascending = False)
         self.TopK_jobs =  pd.DataFrame(self.df_jobs[:self.K]).reset_index(drop = True)
         print("Top {} Job Recommendations".format(self.K))
         print("matching keywords: '{}'".format(self.new_text))
         print(self.TopK_jobs["text"])

jobs_data_path = "job_data_filtered.csv"
JobRecommender(jobs_data_path, "retail sale", 10)
