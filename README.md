# Hackathon: Gitcoin Open Data Science Hackathon : [Sybil Slayer](https://gitcoin.co/issue/29389#) 

The data created for the analysis is available here on [Hugging Face](https://huggingface.co/datasets/Poupou/Gitcoin-ODS-Hackhaton-GR15) 

The report is in the github repo **[A time series analysis of gitcoin grants contributors to Grant 15](https://github.com/poupou-web3/GC-ODS-Sybil/blob/main/A%20time%20series%20analysis%20of%20gitcoin%20grants%20contributors%20to%20Grant%2015.pdf)**

To run the jupyter notebook please put the features datasets and the `hackathon-contributions-dataset_v2.csv` as shown in the directory and file structure below:

```
data
  +----features
          +----- eth_polygon
                    +----- features_eth_polygon.csv    
          +----- eth_std
                    +----- features_eth_std.csv      
  +----- hackathon-contributions-dataset_v2.csv
```
    
Use requirements to install the libraries:
`pip install requirements.txt`


The main jupyter notebook used to create the report is **[k_mean_eth](https://github.com/poupou-web3/GC-ODS-Sybil/blob/main/jupyter/10_28_k_mean_eth.ipynb)**.
Be careful before running it is memory heavy because it automatically exports more than 150 charts.

The [k_mean_polygon](https://github.com/poupou-web3/GC-ODS-Sybil/blob/main/jupyter/10_28_k_mean_polygon_new.ipynb) notebook is similar and produces the results for the polygon transactions.

The [agglomerative_eth](https://github.com/poupou-web3/GC-ODS-Sybil/blob/main/jupyter/10_29_agglomerative_eth_new.ipynb) file shows the results in the case of the agglomerative clustering.

An example of clustering for Ethereum is provided in [eth_std_clusters.csv](https://github.com/poupou-web3/GC-ODS-Sybil/blob/main/eth_std_clusters.csv), please mind that it was added after the report writings and thus the seed used for K-means was not the same, thus cluster names are different from the one used in the report. 

## Re-creating the data sets
### For transactions
For Etherscan run `src\main\extract_etherscan_txs.py` 

For Polygon chain run `src\main\extract_polygon_txs.py` 

Parameters are hard coded and should be modified!

### For extracting the features 
run `src\main\features\create_feature_df.py`
Parameters are hard coded and should be modified! You can change the tx_chain parameter to select the network.

