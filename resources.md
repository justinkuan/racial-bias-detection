# Resources

*Last updated November 24, 2020 at 4:30 AM*

This file contains a list of files, papers, and links that might be of help with the project.  They are categorized by:

[Data Sources](##data-sources)

[Related Work / Literature](##related-work-literature)

[Reference Guides / Miscellaneous](##reference-guides-miscellaneous)

***NEW!!!***  Recent additions and important sources are **bolded** for convenience.



## Data Sources

- **[2.7 million news articles and essays](https://components.one/datasets/all-the-news-2-news-articles-dataset/)** - An extension of a Kaggle data set *[All the News](https://www.kaggle.com/snapcrack/all-the-news)*.  This set is released by Components, a publication and research group working on large data sets headed by Andrew Thompson.  Download the rather large data set and let's take a group look-see.
- [The GDELT Project](https://www.gdeltproject.org/) - A database of news data from around the world.  Here is an [introduction blog post on Medium](https://medium.com/@atakanguney94/a-brief-introduction-into-gdelt-global-database-of-events-language-and-tone-e96b0c64d03a). 
- [NELA2017 Dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ZCXSKG) - This is the dataset created by the authors of the *Sampling the News Producers* article. NEws LAndscape (NELA2017) is hosted on Harvard Dataverse



## Related Work / Literature

#### Similar Studies

- (*blog*) [ML versus the News](https://towardsdatascience.com/machine-learning-versus-the-news-3b5b479d8e6a) - Took news articles with the same story and identified their 'neutrality' via sentiment.  This project is of particular note because it hews closely to the idea of our project. 
  - (*academic*) [Technical report](https://github.com/jameslucasbaker/Capstone/raw/master/capstoneReportUPDATED.pdf) - I'm still working my way through this, link auto-downloads file. 	
  - [Github Repository](https://github.com/jameslucasbaker/Capstone) 
- (*academic*) **[News Media Trends in the Framing of Immigration and Crime, 1990-2013](https://academic.oup.com/socpro/article-abstract/67/3/452/5545185?redirectedFrom=fulltext)** - This paper just came out this year and I've already reached out to the authors to see if they might share the paper with us.  While their focus is about immigration and crime and how news media frames it, their methodology for studying how media frames things can maybe provide us some clue on how we can as well.
- (*academic*) [Sampling the News Producers: A Large News and Feature Data Set for the Study of the Complex Media Landscape](https://www.aaai.org/ocs/index.php/ICWSM/ICWSM18/paper/viewFile/17796/17044) - a paper I found that talks about crafting "a large political news data set, containing over 136K news articles, from 92 news sources, collected over 7 months of 2017."  The data set may be available as well.  This is included as a similar study because if we need to compile our own data source we may end up having to follow the footsteps of this paper.

#### Bias in Machine Learning / NLP

- (*academic*) [Attenuating Bias in Word Vectors](http://proceedings.mlr.press/v89/dev19a/dev19a.pdf) - 2019 conference publication on bias in word vectors.  

- (*blog*) [Man is to Doctor as Woman is to Nurse: the Gender Bias of Word Embeddings](https://towardsdatascience.com/gender-bias-word-embeddings-76d9806a0e17) - TowardsDataScience post about gender inequality in NLP techniques
- (*periodical*) [Machine Bias](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) - ProPublica article about racial bias in ML, this kind of story is part of the inspiration for our topic.

#### Racial bias (and other bias) literature

- (*blog*) [7 Examples of Racial Bias in Job Descriptions](https://blog.ongig.com/diversity-and-inclusion/racial-bias-in-job-descriptions/) - Good introductory piece into how racial language can still be found in modern job descriptions.  Some are low hanging fruit, but clearly they came from somewhere.
- (*wikipedia*) [Racial Bias in Criminal News in the US](https://en.wikipedia.org/wiki/Racial_bias_in_criminal_news_in_the_United_States#cite_note-Blacks_in_the_News:_Television,_Modern_Racism_and_Cultural_Change-6) - Wikipedia entry
- (*white paper*) [State of the Science: Implicit Bias Review 2014](http://kirwaninstitute.osu.edu/wp-content/uploads/2014/03/2014-implicit-bias.pdf) - White paper by the Kirwan Institute (Ohio State), a follow-up to their 2013 State of the Science paper.   Covers a broad range of
- (*academic*) [Blacks in the News: Television, Modern Racism and Cultural Change](http://www.aejmc.org/home/wp-content/uploads/2012/09/Journalism-Quarterly-1992-Entman-341-611.pdf) - 1992 paper on racism in the news.  I haven't read this yet, but it was referenced on Wikipedia.
- (*white paper*) [Race and Punishment: Racial Perceptions of Crime and Support for Punitive Policies](https://www.sentencingproject.org/wp-content/uploads/2015/11/Race-and-Punishment.pdf) - Referenced paper on Wikipedia by The Sentencing Project group.



## Reference guides / miscellaneous

- (*blog*) [How To Prepare News Articles for Text Summarization](https://machinelearningmastery.com/prepare-news-articles-text-summarization/) - short 5-10 minute read on some basics of text summarization using CNN News Story Dataset (code available) 
- (*white paper*) [The Practical Guide to Managing Data Science at Scale](https://www.dominodatalab.com/wp-content/uploads/domino-managing-ds.pdf) - 30-45 minute read on running a DS project to scale.  It is based on Domino Data Lab's DS process, an evolved form of CRISP-DM and akin to Microsoft's TDSP.  I like this one a bit because it's more of a supplemental read, and I have found myself consistently thinking about how many of the pitfalls our team suffered from last year due to lack of clear direction and weak leadership.

