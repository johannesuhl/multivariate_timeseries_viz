# Visualization techniques for multivariate time series data using Python + matplotlib

## multivariate_time_series_visualization.py

For high-dimensional time series data, using line plots for integrated visualization can be messy. Thus, for quick visual mining of large multivariate time series datasets, a heatmap can be useful, showing time (x) versus the intensity of each variable of the multivariate time series data.

The script multivariate_time_series_visualization.py reads exemplary multivariate time series data (i.e., the Ozone Level Detection Data Set (Zhang et al.) from the UCI Machine Learning Repository) and generates a heatmap.
Each variable is scaled into the range (0,1) for visualization purposes.

<img width="1000" alt="java 8 and prio java 8  array review example" src="https://github.com/johannesuhl/multivariate_timeseries_viz/blob/main/multivariate_timeseries_8hr.jpg">

## References:
##### Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
Ozone Level Detection Data Set (Zhang et al.): https://archive.ics.uci.edu/ml/datasets/ozone+level+detection
