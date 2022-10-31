# Hackathon: Gitcoin Open Data Science Hackathon : [Sybil Slayer](https://gitcoin.co/issue/29389#) 

The data created for the analysis is available here on [HugginFace](https://huggingface.co/datasets/Poupou/Gitcoin-ODS-Hackhaton-GR15) 

The report is in the github repo [A time series analysis of gitcoin grants contributors to Grant 15](https://github.com/poupou-web3/GC-ODS-Sybil/blob/main/A%20time%20series%20analysis%20of%20gitcoin%20grants%20contributors%20to%20Grant%2015.pdf)

To run the jupyter notebook please put the feature dataset in a data folder as follow as:
And to retrieve the transactions the hackathon-contributions-dataset_v2.csv in the data folder


data

    |___features
         |____ eth_polygon
                  |___features_eth_polygon.csv    
        
         |____eth_std
                  |___features_eth_std.csv      
    |___ hackathon-contributions-dataset_v2.csv


The main jupyter notebook used to create the report is [k_mean_eth](https://github.com/poupou-web3/GC-ODS-Sybil/blob/main/jupyter/10_28_k_mean_eth.ipynb).
Be carefull before running it is memory heavy because it automatically export more than 150 charts.
