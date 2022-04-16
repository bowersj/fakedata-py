# Distributions

A distribution models how data is spread out, for example a distribution can model how many products are in each Amazon category.

## Distribution Applications

* [Probability Distributions in Data Science](https://www.kdnuggets.com/2020/02/probability-distributions-data-science.html)
* [6 Useful Probability Distributions with Applications to Data Science Problems](https://towardsdatascience.com/6-useful-probability-distributions-with-applications-to-data-science-problems-2c0bee7cef28)
* [The most used probability distributions in Data Science](https://towardsdatascience.com/the-most-used-probability-distributions-in-data-science-5b3c11d34bfe)
* [A practical overview on probability distributions](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4387424/)

## Probability Distributions Flow Chart
![](https://miro.medium.com/max/700/1*nOMS0KgevT7YfqtfnhgXUg.png)


## Binomial distribution
* Models binary data
* Did the client buy the product, or not?
* Did the medicine help the patient to recover, or not?
* Was the online ad clicked on, or not?

> Two key elements of the binomial model are a set of trials (binary experiments) and the probability of success (success is the "yes" outcome: an ad clicked on or a patient cured).
[source](https://towardsdatascience.com/6-useful-probability-distributions-with-applications-to-data-science-problems-2c0bee7cef28)

The binomial distribution may serve as an anomaly detector.

## Poisson distribution
Only returns natural numbers
The Poisson distribution has one parameter, which denotes the rate at which events are happening.

>Poisson distribution describes events that occur at some rate over time od space. It can be used to conduct queueing simulations that help allocate resources.
[source](https://towardsdatascience.com/6-useful-probability-distributions-with-applications-to-data-science-problems-2c0bee7cef28#:~:text=Poisson%20distribution%20describes%20events%20that%20occur%20at%20some%20rate%20over%20time%20od%20space.%20It%20can%20be%20used%20to%20conduct%20queueing%20simulations%20that%20help%20allocate%20resources.)

## Exponential distribution

in Python's scipy package, the exponential distribution is parametrized with a scale, which is the __inverse of a rate)).