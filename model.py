# Library
import pandas as pd

# Visualizing
import matplotlib.pyplot as plt

# Model
from sklearn.cluster import KMeans


def find_k(scaled_train, cluster_vars, k_range):
    '''
    Evaluates k running through different values of k on scaled_train (the first dataframe in our list, X) and comparing the Sum of Squared Errors, the change in SSE from one k to the next, and the percent change from one k to the next.
    '''
    sse = []
    for k in k_range:
        kmeans = KMeans(n_clusters=k)

        # scale_set[0] is our scaled_train dataframe..the first dataframe in the list of dataframes stored in scale_set. 
        kmeans.fit(scaled_train[cluster_vars])

        # inertia: Sum of squared distances of samples to their closest cluster center.
        sse.append(kmeans.inertia_) 

    # compute the difference from one k to the next
    delta = [round(sse[i] - sse[i+1],0) for i in range(len(sse)-1)]

    # compute the percent difference from one k to the next
    pct_delta = [round(((sse[i] - sse[i+1])/sse[i])*100, 1) for i in range(len(sse)-1)]

    # create a dataframe with all of our metrics to compare them across values of k: SSE, delta, pct_delta
    k_comparisons_df = pd.DataFrame(dict(k=k_range[0:-1], 
                             sse=sse[0:-1], 
                             delta=delta, 
                             pct_delta=pct_delta))

    # plot k with inertia
    plt.plot(k_comparisons_df.k, k_comparisons_df.sse, 'bx-')
    plt.xlabel('k')
    plt.ylabel('SSE')
    plt.title('The Elbow Method to find the optimal k\nFor which k values do we see large decreases in SSE?')
    plt.show()

    # plot k with pct_delta
    plt.plot(k_comparisons_df.k, k_comparisons_df.pct_delta, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Percent Change')
    plt.title('For which k values are we seeing increased changes (%) in SSE?')
    plt.show()

    # plot k with delta
    plt.plot(k_comparisons_df.k, k_comparisons_df.delta, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Absolute Change in SSE')
    plt.title('For which k values are we seeing increased changes (absolute) in SSE?')
    plt.show()

    return k_comparisons_df


def cluster_maker(scaled_train, k, cluster_vars):
    '''
    Takes the scaled training data and fits it to the K-Means model
    '''    
    # Creates a K-Means object with n = 7 and random state = 14
    kmeans = KMeans(n_clusters=7, random_state = 14)

    # Fits the K-Means obect the scaled training data
    kmeans.fit(scaled_train[cluster_vars])

    return kmeans


def get_centroids(kmeans, cluster_vars, cluster_name):
    '''
    Gets the centroids for each distinct cluster
    '''
    centroid_col_names = ['centroid_' + i for i in cluster_vars]

    centroid_df = pd.DataFrame(kmeans.cluster_centers_, 
                               columns=centroid_col_names).reset_index().rename(columns={'index': cluster_name})

    return centroid_df


def assign_clusters(kmeans, cluster_vars, cluster_name, centroid_df):
    '''
    Labels clusters for each observation in scaled_train, scaled_validate, & scaled_test
    '''
    for i in range(len(scaled_set)):
        clusters = pd.DataFrame(kmeans.predict(scaled_set[i][cluster_vars]), 
                            columns=[cluster_name], index=scaled_set[i].index)

        clusters_centroids = clusters.merge(centroid_df, on=cluster_name, copy=False).set_index(clusters.index.values)

        scaled_set[i] = pd.concat([scaled_set[i], clusters_centroids], axis=1)
    return scaled_set
