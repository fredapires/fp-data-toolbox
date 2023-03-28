import os

# %% ------


def find_proj_root_path(start_dir='.', marker_file='setup.py'):
    """
    Find the root path of a project by searching for a specified marker file in parent directories.

    Args:
        start_dir (str): The directory to start the search from.
        marker_file (str): The name of the marker file that indicates the root directory.

    Returns:
        str: The path to the root directory if the marker file is found, or None if it is not found.
    """
    curr_dir = os.path.abspath(start_dir)

    while True:
        if marker_file in os.listdir(curr_dir):
            return curr_dir

        parent_dir = os.path.abspath(os.path.join(curr_dir, os.pardir))

        if parent_dir == curr_dir:
            return None

        curr_dir = parent_dir


# %% ------
def find_ydata_yaml(search_path, file_name='ydata_profiling_config.yaml'):
    """
    Search for a file with a specific name in a directory and its subdirectories,
    and return the path to the file if it is found.

    Args:
        file_name (str): The name of the file to search for.
        search_path (str): The directory to start the search from.

    Returns:
        str: The path to the file if it is found, or None if it is not found.
    """
    for root, dirs, files in os.walk(search_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None


# %% ------
def ydata_yaml_setup():
    """
    Set up the ydata_yaml configuration file for data profiling.

    The function searches for the project root path using the `find_proj_root_path()` function.
    It then searches for the ydata_yaml configuration file using the `find_ydata_yaml()` function.
    If the file doesn't exist, the function creates a default configuration file at the project root path.
    The default configuration file includes metadata information about the dataset.

    Returns:
        str: The absolute path to the ydata_yaml configuration file.
    """
    proj_root_path = find_proj_root_path()
    ydata_yaml_path = find_ydata_yaml(proj_root_path)
    if ydata_yaml_path is None:
        ydata_yaml_default_path = proj_root_path + \
            '\\config\\ydata_yaml\\ydata_profiling_config.yaml'
        ydata_yaml_default_str = '''
# Metadata
dataset:
    # description:
    # creator:
    author: Fred Pires
    copyright_holder: 'The Home Depot'
    # copyright_year: ''
    url: 'https://github.com/FXP3365_thdgit'

# variables:    ## defined in function
#     descriptions: {}

# infer dtypes
infer_dtypes: true

# Show the description at each variable (in addition to the overview tab)
show_variable_description: true

# Number of workers (0=multiprocessing.cpu_count())
pool_size: 0

# Show the progress bar
progress_bar: true

# Per variable type description settings
vars:
    num:
        quantiles:
            - 0.05
            - 0.25
            - 0.5
            - 0.75
            - 0.95
        skewness_threshold: 20
        low_categorical_threshold: 20
        # Set to zero to disable
        chi_squared_threshold: 0.999
    cat:
        length: false ## changed for SCF trans version
        characters: false ## changed for SCF trans version
        words: false ## changed for SCF trans version
        cardinality_threshold: 50
        n_obs: 10
        # Set to zero to disable
        chi_squared_threshold: 0.999
        coerce_str_to_date: true
        redact: false
        histogram_largest: 50
        stop_words: []
    bool:
        n_obs: 3
        # string to boolean mapping dict
        mappings:
            t: true
            f: false
            yes: true
            no: false
            y: true
            n: false
            true: true
            false: false
            # 1: true
            # 0: true
    file:
        active: false
    image:
        active: false
        exif: true
        hash: true
    path:
        active: false
    url:
        active: false
    timeseries:
        active: false
        autocorrelation: 0.7
        lags: [1, 7, 12, 24, 30]
        significance: 0.05
        pacf_acf_lag: 100

# Sort the variables. Possible values: "ascending", "descending" or null (leaves original sorting)
sort: null

# which diagrams to show
missing_diagrams:
    bar: true
    matrix: true
    heatmap: true
    dendrogram: true

correlations:
    pearson:
        calculate: false ## changed for SCF trans version
        warn_high_correlations: false
        threshold: 0.9
    spearman:
        calculate: false ## changed for SCF trans version
        warn_high_correlations: false
        threshold: 0.9
    kendall:
        calculate: false ## changed for SCF trans version
        warn_high_correlations: false
        threshold: 0.9
    phi_k:
        calculate: false ## changed for SCF trans version
        warn_high_correlations: false
        threshold: 0.9
    cramers:
        calculate: false ## changed for SCF trans version
        warn_high_correlations: false
        threshold: 0.9
    auto:
        # calculate: true ## changed for SCF trans version
        calculate: false ## changed for SCF trans version
        # warn_high_correlations: true
        warn_high_correlations: false
        threshold: 0.9

# Bivariate / Pairwise relations
interactions:
    # targets: [] ## changed for SCF trans version; defined in function
    continuous: false ## changed for SCF trans version

# For categorical
categorical_maximum_correlation_distinct: 100

report:
    precision: 10

# Plot-specific settings
plot:
    # Image format (svg or png)
    image_format: 'svg'
    dpi: 800

    scatter_threshold: 1000

    correlation:
        cmap: 'RdBu'
        bad: '#000000'

    missing:
        cmap: 'RdBu'
        # Force labels when there are > 50 variables
        # https://github.com/ResidentMario/missingno/issues/93#issuecomment-513322615
        force_labels: true

    cat_frequency:
        show: true # if false, the category frequency plot is turned off
        type: 'bar' # options: 'bar', 'pie'
        max_unique: 30
        colors: null # use null for default or give a list of matplotlib recognised strings

    histogram:
        x_axis_labels: true

        # Number of bins (set to 0 to automatically detect the bin size)
        bins: 0

        # Maximum number of bins (when bins=0)
        max_bins: 250

# The number of observations to show
n_obs_unique: 5
n_extreme_obs: 5
n_freq_table_max: 10

# Use `deep` flag for memory_usage
memory_deep: false

# Configuration related to the duplicates
duplicates:
    head: 5
    key: '# duplicates'

# Configuration related to the samples area
samples:
    head: 10
    tail: 10
    random: 10

# Configuration related to the rejection of variables
reject_variables: true

# When in a Jupyter notebook
notebook:
    iframe:
        height: '800px'
        width: '100%'
        # or 'src'
        attribute: 'srcdoc'

html:
    # Minify the html
    minify_html: true

    # Offline support
    use_local_assets: true

    # If true, single file, else directory with assets
    inline: true

    # Show navbar
    navbar_show: true

    # Assets prefix if inline = true
    assets_prefix: null

    # Styling options for the HTML report
    style:
        theme: 'united'
        primary_color: '#ff5e1f' ## changed for SCF trans version

    full_width: false
        '''
        os.makedirs(os.path.dirname(ydata_yaml_default_path), exist_ok=True)
        with open(ydata_yaml_default_path, "w") as file:
            file.write(ydata_yaml_default_str)
        ydata_yaml_path = ydata_yaml_default_path
    return os.path.abspath(ydata_yaml_path)


# %% ------
