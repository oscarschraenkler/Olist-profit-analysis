# How can Olist increase its profit margin?
Analysis by Oscar Schraenkler

Olist is an e-commerce service similar to Amazon that connects merchants to main marketplaces in Brazil. The company has made a dataset available with information about 100k orders from 2016 to 2018. Read more about Olist on their website: www.olist.com

The dataset can be found on Kaggle: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
## Problem Statement

The CEO of Olist would like to increase the company’s profit margin.
As an analyst, I will see whether I can find inefficiencies in Olists business and make a data-driven recommendation on how they can increase their profit margin.

## Approach:

The dataset includes reviews for each product sold on the platform. We can assume that negative experiences discourage customers from returning to Olist. By making assumptions about the financial cost of negative reviews on the platform, I will be able to identify the underperforming sellers and find the optimal number of underperforming sellers to remove in order to increase Olists profit.

**We are seeking to answer this question:**

❓ How many underperforming sellers should Olist remove to improve its profit, given that it has:

- Some revenue per seller per months
- Some revenue per order
- Some reputation costs (estimated) per bad review
- Some operational costs of the IT system that grows with number of orders, but not linearly (scale effects)

❗️ Check out the analysis and my recommendation in the jupyter notebook [here](olist_analysis.ipynb) ❗️

## About Olist 🇧🇷

<img src="https://wagon-public-datasets.s3.amazonaws.com/data-science-images/best-practices/olist.png" width="500"/>

Olist is a leading e-commerce service that connects merchants to main marketplaces in Brazil. They provide a wide range of offers including inventory management, dealing with reviews and customer contacts to logistic services.

Olist charges sellers a monthly fee. This fee is progressive with the volume of orders.

Here are the seller and customer workflows:

**Seller:**

- Seller joins Olist
- Seller uploads products catalogue
- Seller gets notified when a product is sold
- Seller hands over an item to the logistic carrier

👉 Note that multiple sellers can be involved in one customer order!

**Customer:**

- Browses products on the marketplace
- Purchases products from Olist.store
- Gets an expected date for delivery
- Receives the order
- Leaves a review about the order

👉 A review can be left as soon as the order is sent, meaning that a customer can leave a review for a product he did not receive yet!
